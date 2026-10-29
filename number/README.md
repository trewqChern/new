# Web Based Result Publication System (Subject-Wise Marks & Grades)

A pixel-perfect, responsive HTML and CSS implementation of the Bangladesh Education Boards **Web Based Result Publication System** (`eboardresults.com` layout) featuring subject-wise marks and grades.

## Structure

- [**`index.html`**](file:///c:/Users/USER/Downloads/GoogleChromePortable/NewDownloads/new/number/index.html): The main document with student credential tables, header banner, action buttons, and subject-wise grade/marks table.
- [**`style.css`**](file:///c:/Users/USER/Downloads/GoogleChromePortable/NewDownloads/new/number/style.css): Full stylesheet including typography, colors, table borders, and print styling (`@media print`).
- [**`bd_logo.png`**](file:///c:/Users/USER/Downloads/GoogleChromePortable/NewDownloads/new/number/bd_logo.png): High-resolution official circular emblem of the Government of the People's Republic of Bangladesh.
- [**`logo.webp`**](file:///c:/Users/USER/Downloads/GoogleChromePortable/NewDownloads/new/number/logo.webp): WebP format emblem asset.

## Features

1. **Exact Typography and Color Palette**:
   - Header banner: Dark green gradient (`#067239` to `#02592b`) with rounded corners.
   - Action buttons: "Search Again" (`#5bc0de`) and "Print" (`#5cb85c`).
   - Subject-wise table: Green header (`#5cb85c`) with white bold text.
2. **Interactive Controls**:
   - **Search Again**: Refreshes / resets the result query.
   - **Print**: Triggers the browser print dialog (`window.print()`).
3. **Print-Ready**:
   - Configured with `-webkit-print-color-adjust: exact` and button hiding for clean A4 printing or PDF export.
