# Encryption and Decryption App

This repository contains a simple encryption and decryption application implemented in Python using Tkinter and base64 library. This application allows users to encrypt and decrypt text using a secret key. Users can open text files, encrypt or decrypt their contents, and save the results to a new file.

![Encryption and Decryption App](https://user-images.githubusercontent.com/103423072/236072966-6901ca6e-32fa-4b44-9242-298c4b89f7ca.png)

## Features

- Encrypt and decrypt text using a secret key
- Open and save text files
- Reset functionality to clear input fields
- User-friendly GUI built with Tkinter

## Prerequisites

To run the application, you need to have Python and Tkinter installed on your system. Tkinter is included in the standard Python distribution. If you are using Python 3.x, you should already have Tkinter installed.

## Running the Application

To run the application, navigate to the repository directory and execute the following command:

```python main.py```

## Usage

1. Enter the text you want to encrypt or decrypt in the "Enter text for encryption and decryption" field.
2. Enter a secret key in the "Enter secret key for encryption and decryption" field.
3. Click "ENCRYPT" to encrypt the text, or "DECRYPT" to decrypt the text.

   ![Encrypt](https://user-images.githubusercontent.com/103423072/236072966-6901ca6e-32fa-4b44-9242-298c4b89f7ca.png)
   
   ![Decrypt](https://user-images.githubusercontent.com/103423072/236072967-67056648-15e8-4b3a-a876-1b794af35218.png)

4. You can click "RESET" to clear the input fields.
5. Click "OPEN" to open a text file, and the contents of the file will be loaded into the text field.
6. Click "SAVE" to save the contents of the text field to a new text file.

## Code Structure

The code is contained in a single file, `main.py`. This file contains the `EncryptDecryptApp` class, which defines the application's behavior, and a `main` function, which initializes and runs the Tkinter main loop.

## Acknowledgements

This project uses the [Tkinter](https://docs.python.org/3/library/tkinter.html) library for building the graphical user interface.

Made by ❤️ by Edison<br>
www.Edisonwhale.com

Have any question?  
Email me!  
Edison@gatech.edu
