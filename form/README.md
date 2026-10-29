# Web Based Result Publication System for Education Board (Local Implementation)

This is a local, self-contained implementation of the Bangladesh Education Board Result Publication System (`https://www.educationboardresults.gov.bd/v2/home`).

## Structure

```
form/
├── index.html                 # Main result publication system web page
├── server.py                  # Optional local Python backend server
├── assets/
│   ├── css/
│   │   ├── bootstrap.min.css         # Bootstrap 3.4.0 styling
│   │   ├── bootstrap-dialog.min.css  # Modal & dialog styling
│   │   └── jquery.dataTables.min.css # DataTables CSS for EIIN list
│   ├── js/
│   │   ├── jquery.min.js             # jQuery 3.4.0
│   │   ├── bootstrap.min.js          # Bootstrap 3.4.0 JS
│   │   ├── bootstrap-dialog.min.js   # Dialog plugin
│   │   ├── jquery.dataTables.min.js  # DataTables JS
│   │   └── d3.min.js                 # D3.js for tree visualization
│   ├── fonts/
│   │   ├── glyphicons-halflings-regular.woff2
│   │   ├── glyphicons-halflings-regular.woff
│   │   └── glyphicons-halflings-regular.ttf
│   └── img/
│       ├── logo.png                  # Bangladesh Education Board Emblem
│       ├── favicon.png               # Portal favicon
│       └── loading.gif               # Government portal loading spinner
├── app/
│   └── stud/
│       ├── btbl.html                 # Institution Table Finder
│       └── btree.html                # Institution Tree Finder
└── data/
    ├── districts.json                # All districts across all 11 education boards
    ├── centers_dhaka.json            # Centers list
    ├── institutions_sample.json      # Authentic Bangladesh institutions database (EIIN, codes, names, upazillas)
    └── subjects.json                 # Complete SSC/HSC subject code mapping
```

## Features

1. **Exact Government Design & UI**: Matches the authentic Bangladesh Education Board results portal layout, colors (`#14A44D`), emblem, typography, tables, and responsiveness.
2. **Interactive Form Controls**:
   - Board, Examination, and Year selectors.
   - Result Type switcher:
     - **Individual/Detailed Result**: reveals Roll and Registration fields.
     - **Institution Result**: reveals EIIN input with Tree and List finders.
     - **Center Result & District Result**: dynamically loads districts for the selected board and centers.
3. **Interactive Local CAPTCHA Generator**:
   - Generates authentic 4-digit distorted numeric CAPTCHAs on an HTML5 canvas.
   - Features real-time "Click to load another image" reload button.
   - Validates user input before allowing result access.
4. **Complete Result Sheets**:
   - **Student Information Summary**: Roll No, Registration No, Student Name, Parents' names, Board, Session, Group, GPA, DOB, Institute.
   - **Subject-wise Grade/Marks Table**: Subject codes, Subject names, and letter grades.
   - **Institution Summary Sheet**: Pass percentage, GPA 5 count, total appeared, and student roll list.
5. **Print & Search Again**:
   - Dedicated print styles (`@media print`) for clean printing/export to PDF.
   - "Search Again" button smoothly resets the form for the next query.
6. **EIIN Finders (List & Tree)**:
   - Searchable DataTables list of institutions with click-to-select support.
   - D3.js interactive collapsible tree of boards, districts, and institutions.

## How to Run

### Option 1: Directly in Any Browser (No Server Required)
Simply double-click or open `index.html` in Google Chrome, Microsoft Edge, or Firefox:
```
file:///C:/Users/USER/Downloads/GoogleChromePortable/NewDownloads/new/form/index.html
```

### Option 2: Run with Local Python Server
Open a terminal in the `form` directory and run:
```bash
python server.py
```
Then visit:
```
http://localhost:8080/
# or
http://localhost:8080/v2/home
```
