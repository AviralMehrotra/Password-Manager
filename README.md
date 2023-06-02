# Password Manager

This is a simple password manager program implemented using Python and Tkinter GUI library. It allows you to store and retrieve passwords for different websites.

## Features

- **Master Password:** The program requires a master password to access the password manager. Only users who know the correct master password can view and manage the stored passwords.

- **Password Prompt:** When the program starts, it displays a password prompt window where users can enter the master password. If the entered password matches the master password, the password prompt window closes, and the password manager window opens. Otherwise, an error message is displayed, and the program exits.

- **Password Encryption:** The program uses a simple encryption algorithm (Caesar cipher) to encrypt the passwords before storing them. The encrypted passwords are then saved in a JSON file.

- **Search Password:** Users can search for a stored password by entering the website name in the corresponding input field and clicking the "Search" button. If the website is found in the stored data, the associated email and decrypted password are displayed in a message box. Otherwise, an error message is shown.

- **Generate Password:** The program provides a password generator feature. Clicking the "Generate" button generates a random password consisting of letters, numbers, and symbols. The generated password is displayed in the password input field and automatically copied to the clipboard for easy use.

- **Add Password:** Users can add new passwords to the manager by entering the website, email/username, and password in the respective input fields. Clicking the "Add" button saves the password information to a JSON file (`dat.json`). If the file doesn't exist, it is created. The stored passwords can be later retrieved using the search feature.

## Getting Started

To run the program, you need to have Python installed on your system. Follow the steps below to get started:

1. Clone the repository or download the code files.

2. Install the required dependencies by running the following command:
   ```
   pip install tkinter pyperclip
   ```

3. Open a terminal or command prompt and navigate to the directory where the code files are located.

4. Run the following command to start the password manager:
   ```
   python password_manager.py
   ```

## Usage

Upon running the program, a password prompt window will appear. Enter the master password to access the password manager. The default master password is '123'. You can change it by modifying the code (`entered_master_password == '123'`) in the `check_password` function.

### Password Prompt

The password prompt window asks for the master password to gain access to the password manager. If the entered password matches the master password, the window will close, and the password manager window will open. Otherwise, an error message will be displayed, and the program will exit.

### Password Manager

The password manager window allows you to perform the following actions:

- **Search Password:** Enter a website name and click the "Search" button to retrieve the corresponding email and password from the stored data. If the website is found, the email and password will be displayed in a message box. Otherwise, an error message will be shown.

- **Generate Password:** Click the "Generate" button to generate a random password. The generated password will be displayed in the password input field and automatically copied to the clipboard.

- **Add Password:** Enter the website, email/username, and password in the respective input fields. Click the "Add" button to store the password information. The data will be saved in a JSON file (`dat.json`). If the file doesn't exist, it will be created.

Note: You can customize the file path by modifying the `file_path` variable in the code.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. Feel free to use and modify the code as per your needs.
