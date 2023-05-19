# QR Code Generator

QR Code Generator is a Python-based GUI application using the Tkinter module. It allows the user to generate QR codes for any URL, and also maintain a history of the recent QR codes generated.


![bcd5991328cde35f0e36a826de8effc](https://github.com/EdisonWhale/Personal_Pratice_Small_Projects/assets/103423072/a9521d68-6b6c-4fc7-b06c-ffaf10c20450)

## Features

- **QR Code Generation**: Generate QR codes from URLs provided by the user. Each QR code is saved as a PNG file.
- **History**: The application keeps a history of the last three URLs for which QR codes were generated. Users can copy these URLs to their clipboard.
- **Link Opening**: Open the most recently used link in a default web browser.
- **Resize QR Code**: Resize the generated QR code to a standard 200x200 pixel size.

## Usage

1. Run the Python file `main.py`.
2. On the GUI, enter the name of the link and the URL for which you want to generate the QR code.
3. Click on the "Generate QR code" button to generate the QR code. The QR code will be displayed on the GUI.
4. To open the most recent link in a web browser, click on the "Open QR code" button.
5. To copy a link from the history to the clipboard, click on the "Copy Link" button next to the corresponding history entry.

## Dependencies

- Python 3
- Tkinter
- pyqrcode
- pyperclip
- PIL
- os
- webbrowser

Install dependencies with pip:

```
pip install pyqrcode pyperclip pillow
```

## Contact


Made with ❤️ by Edison  
[www.Edisonwhale.com](http://www.edisonwhale.com)

Have any questions?  
Email me!  
Edison@gatech.edu
