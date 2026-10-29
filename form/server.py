#!/usr/bin/env python3
"""
Local server for Bangladesh Education Board Results (v2/home).
Run: python server.py [port]
Default port: 8080
"""
import http.server
import socketserver
import urllib.parse
import json
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class BoardResultHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        # Route / and /v2/home to index.html
        if path in ('/', '/v2/home', '/home', '/form', '/form/', '/form/index.html'):
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            with open(os.path.join(BASE_DIR, 'index.html'), 'rb') as f:
                self.wfile.write(f.read())
            return

        # Route /result.html and /result
        if path in ('/result.html', '/result', '/v2/result.html', '/v2/result', '/form/result.html'):
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            with open(os.path.join(BASE_DIR, 'result.html'), 'rb') as f:
                self.wfile.write(f.read())
            return

        # Route /busy.html and /busy
        if path in ('/busy.html', '/busy', '/v2/busy.html', '/v2/busy', '/server_busy.html', '/form/busy.html'):
            self.send_response(504)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            with open(os.path.join(BASE_DIR, 'busy.html'), 'rb') as f:
                self.wfile.write(f.read())
            return

        # Route /v2/list
        if path == '/v2/list':
            list_id = query.get('id', [''])[0]
            if list_id == 'dlist':
                board = query.get('board', ['dhaka'])[0].lower()
                dist_file = os.path.join(BASE_DIR, 'data', 'districts.json')
                data = []
                if os.path.exists(dist_file):
                    with open(dist_file, 'r', encoding='utf-8') as f:
                        all_d = json.load(f)
                        data = all_d.get(board, all_d.get('dhaka', []))
                self.send_json(data)
                return

            elif list_id == 'clist':
                data = [
                    {"code":"101","name":"DHAKA COLLEGE"},
                    {"code":"102","name":"GOVT. SCIENCE COLLEGE"},
                    {"code":"103","name":"VIQARUNNISA NOON SCHOOL & COLLEGE"},
                    {"code":"104","name":"NOTRE DAME COLLEGE"},
                    {"code":"105","name":"DHAKA RESIDENTIAL MODEL COLLEGE"}
                ]
                self.send_json(data)
                return

            elif list_id == 'btree':
                inst_file = os.path.join(BASE_DIR, 'data', 'institutions_sample.json')
                if os.path.exists(inst_file):
                    with open(inst_file, 'rb') as f:
                        self.send_response(200)
                        self.send_header('Content-Type', 'application/json')
                        self.end_headers()
                        self.wfile.write(f.read())
                        return
                self.send_json({"data": []})
                return

        # Fallback to standard static file serving
        return super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path in ('/v2/getres', '/getres'):
            content_length = int(self.headers.get('Content-Length', 0))
            post_body = self.rfile.read(content_length).decode('utf-8')
            params = urllib.parse.parse_qs(post_body)
            
            board = params.get('board', ['dhaka'])[0]
            exam = params.get('exam', ['ssc'])[0]
            year = params.get('year', ['2024'])[0]
            roll = params.get('roll', ['123456'])[0]
            reg = params.get('reg', ['1234567890'])[0]
            eiin = params.get('eiin', ['108088'])[0]
            result_type = params.get('result_type', ['1'])[0]
            captcha = params.get('captcha', [''])[0]

            is_number_user = (roll in ('201174', '122932') or reg == '2121066865')

            if is_number_user:
                stud_name = "Ishmam Farhan Rhyme"
                f_name = "Gulam Faruque Liton"
                m_name = "Nazmun Nahar"
                sess = "2024-25"
                board = "MYMENSINGH"
                gpa = "GPA=4.83"
                inst = "Mymensingh Govt. College"
                disp_details = "101+102:153=A,107+108:157=A,275:87=A+,174+175:156=A,176+177:168=A+,265+266:170=A+,178+179:155=A"
            else:
                stud_name = "MOHAMMAD RAHMAN"
                f_name = "ABDUL KARIM"
                m_name = "FATEMA BEGUM"
                sess = f"{int(year)-2}-{int(year)-1}"
                gpa = "GPA=5.00"
                inst = "DHAKA RESIDENTIAL MODEL COLLEGE"
                disp_details = "101:A+,107:A+,109:A+,136:A+,137:A+,138:A+,126:A+,150:A+,154:A+,111:A+"

            response_data = {
                "status": 0,
                "msg": "Success",
                "showmarks": 1 if is_number_user else 0,
                "res": {
                    "roll_no": roll,
                    "regno": reg,
                    "name": stud_name,
                    "fname": f_name,
                    "mname": m_name,
                    "board_name": board.upper(),
                    "session": sess,
                    "stud_group": "SCIENCE",
                    "stud_type": "Regular",
                    "stud_sex": "Male",
                    "res_detail": gpa,
                    "dob": f"15/01/{int(year)-16}",
                    "inst_name": inst,
                    "eiin": eiin,
                    "display_details": disp_details
                },
                "sub_details": [
                    {"SUB_CODE": "101", "SUB_NAME": "BANGLA"},
                    {"SUB_CODE": "107", "SUB_NAME": "ENGLISH"},
                    {"SUB_CODE": "109", "SUB_NAME": "MATHEMATICS"},
                    {"SUB_CODE": "136", "SUB_NAME": "PHYSICS"},
                    {"SUB_CODE": "137", "SUB_NAME": "CHEMISTRY"},
                    {"SUB_CODE": "138", "SUB_NAME": "BIOLOGY"},
                    {"SUB_CODE": "126", "SUB_NAME": "HIGHER MATHEMATICS"},
                    {"SUB_CODE": "150", "SUB_NAME": "BANGLADESH & GLOBAL STUDIES"},
                    {"SUB_CODE": "154", "SUB_NAME": "ICT"},
                    {"SUB_CODE": "111", "SUB_NAME": "ISLAM & MORAL EDUCATION"}
                ],
                "extra": {
                    "content": f"<div class='alert alert-success text-center'><b>Result successfully loaded for Roll {roll}</b></div>"
                }
            }
            self.send_json(response_data)
            return

        self.send_response(404)
        self.end_headers()

    def send_json(self, data):
        body = json.dumps(data).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), BoardResultHandler) as httpd:
        print(f"Local Education Board Results server running at:")
        print(f"http://localhost:{PORT}/")
        print(f"http://localhost:{PORT}/v2/home")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
