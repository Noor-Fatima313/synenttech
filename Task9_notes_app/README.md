# Full Stack Python Notes App

A simple full-stack web application built with **Flask, SQLite, HTML, CSS, and Jinja2**. The application allows users to create an account, securely log in, and manage their personal notes.

## Objective

The objective of this project is to build a fully working web application using Python and Flask with:

* User authentication
* Session handling
* Database storage
* CRUD functionality
* Responsive frontend
* User-specific data

## Technologies Used

* **Python**
* **Flask**
* **SQLite**
* **HTML5**
* **CSS3**
* **Jinja2**
* **Werkzeug**

## Features

### Authentication

* User registration
* User login
* User logout
* Session-based authentication
* Password hashing
* Login protection for private pages

### Notes Management

Users can:

* Create new notes
* View their notes
* Edit existing notes
* Delete notes
* Manage multiple notes

Each user's notes are connected to their account, so users can only access their own notes.

### Database

The application uses SQLite to store:

* User accounts
* Hashed passwords
* Notes
* Note creation timestamps

The database is created automatically when the application starts.

### User Interface

The application includes:

* Login page
* Registration page
* Dashboard
* Add Note page
* Edit Note page
* Navigation bar
* Success and error messages
* Responsive design for smaller screens

## Installation

Make sure Python is installed on your computer.

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Run the Flask application:

```bash
python app.py
```

After starting the application, Flask will display a local address such as:

```text
http://127.0.0.1:5000
```

Open the address in your web browser.

## How to Use

### 1. Create an Account

Open the application and select **Register**.

Enter:

* Username
* Password

The password must contain at least 6 characters.

### 2. Login

After registration, go to the Login page and enter your account details.

### 3. Create a Note

After logging in:

1. Open the Dashboard.
2. Click **Add Note**.
3. Enter a title.
4. Enter the note content.
5. Click **Save Note**.

### 4. Edit a Note

From the Dashboard, click **Edit** on any note.

Make your changes and click **Update Note**.

### 5. Delete a Note

Click **Delete** on the note you want to remove and confirm the deletion.

### 6. Logout

Click **Logout** in the navigation bar to end your session.

## Example

A user can register with:

```text
Username: student01
Password: password123
```

Then create a note such as:

```text
Title: Python Project

Content:
Complete the Flask Notes App and prepare the README file.
```

The note will appear on the user's dashboard.

## Security

The application includes basic security features:

* Passwords are stored using Werkzeug password hashing.
* User sessions are used to control authentication.
* Private pages require login.
* Database queries use parameterized SQL statements.
* Users can only edit or delete their own notes.

## Database

SQLite is used because it is lightweight and does not require a separate database server.

The application automatically creates the required database tables:

* `users`
* `notes`

## Task Requirements

This project satisfies the requirements of **Task 9: Full Stack Python Project**.

| Requirement           | Implementation |
| --------------------- | -------------- |
| Flask / Django        | Flask          |
| SQLite / MongoDB      | SQLite         |
| HTML                  | HTML5          |
| CSS                   | CSS3           |
| User Registration     | Implemented    |
| User Login            | Implemented    |
| Session Handling      | Implemented    |
| Core Functionality    | Notes App      |
| Add Records           | Implemented    |
| Edit Records          | Implemented    |
| Delete Records        | Implemented    |
| User Data Storage     | SQLite         |
| Responsive UI         | Implemented    |
| Fully Working Web App | Yes            |

## Future Improvements

Possible improvements include:

* Search notes
* Note categories
* Tags
* Dark mode
* Password reset
* Email verification
* Profile management
* Note timestamps for updates
* Pagination
* Deployment to a cloud platform

## Author

Developed as part of a Python full-stack development project.
