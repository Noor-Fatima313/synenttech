from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = "notes-app-secret-key"

DATABASE = "database.db"


# -----------------------------
# Database Connection
# -----------------------------

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# -----------------------------
# Initialize Database
# -----------------------------

def init_db():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()


# -----------------------------
# Login Required Decorator
# -----------------------------

def login_required(route):
    @wraps(route)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            flash("Please login first.", "error")
            return redirect(url_for("login"))

        return route(*args, **kwargs)

    return decorated_function


# -----------------------------
# Home
# -----------------------------

@app.route("/")
def home():
    if "user_id" in session:
        return redirect(url_for("dashboard"))

    return redirect(url_for("login"))


# -----------------------------
# Register
# -----------------------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"].strip()
        password = request.form["password"]

        if not username or not password:
            flash("Username and password are required.", "error")
            return redirect(url_for("register"))

        if len(password) < 6:
            flash("Password must be at least 6 characters.", "error")
            return redirect(url_for("register"))

        hashed_password = generate_password_hash(password)

        conn = get_db()

        try:
            conn.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password)
            )

            conn.commit()

        except sqlite3.IntegrityError:
            conn.close()
            flash("Username already exists.", "error")
            return redirect(url_for("register"))

        conn.close()

        flash("Registration successful. Please login.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


# -----------------------------
# Login
# -----------------------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"].strip()
        password = request.form["password"]

        conn = get_db()

        user = conn.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()

        conn.close()

        if user and check_password_hash(user["password"], password):

            session["user_id"] = user["id"]
            session["username"] = user["username"]

            flash("Login successful!", "success")

            return redirect(url_for("dashboard"))

        flash("Invalid username or password.", "error")

    return render_template("login.html")


# -----------------------------
# Logout
# -----------------------------

@app.route("/logout")
def logout():

    session.clear()

    flash("You have been logged out.", "success")

    return redirect(url_for("login"))


# -----------------------------
# Dashboard
# -----------------------------

@app.route("/dashboard")
@login_required
def dashboard():

    conn = get_db()

    notes = conn.execute(
        """
        SELECT * FROM notes
        WHERE user_id = ?
        ORDER BY created_at DESC
        """,
        (session["user_id"],)
    ).fetchall()

    conn.close()

    return render_template("dashboard.html", notes=notes)


# -----------------------------
# Add Note
# -----------------------------

@app.route("/add", methods=["GET", "POST"])
@login_required
def add_note():

    if request.method == "POST":

        title = request.form["title"].strip()
        content = request.form["content"].strip()

        if not title or not content:
            flash("Title and content are required.", "error")
            return redirect(url_for("add_note"))

        conn = get_db()

        conn.execute(
            """
            INSERT INTO notes (user_id, title, content)
            VALUES (?, ?, ?)
            """,
            (session["user_id"], title, content)
        )

        conn.commit()
        conn.close()

        flash("Note added successfully!", "success")

        return redirect(url_for("dashboard"))

    return render_template("add_note.html")


# -----------------------------
# Edit Note
# -----------------------------

@app.route("/edit/<int:note_id>", methods=["GET", "POST"])
@login_required
def edit_note(note_id):

    conn = get_db()

    note = conn.execute(
        """
        SELECT * FROM notes
        WHERE id = ? AND user_id = ?
        """,
        (note_id, session["user_id"])
    ).fetchone()

    if note is None:
        conn.close()
        flash("Note not found.", "error")
        return redirect(url_for("dashboard"))

    if request.method == "POST":

        title = request.form["title"].strip()
        content = request.form["content"].strip()

        if not title or not content:
            conn.close()
            flash("Title and content are required.", "error")
            return redirect(url_for("edit_note", note_id=note_id))

        conn.execute(
            """
            UPDATE notes
            SET title = ?, content = ?
            WHERE id = ? AND user_id = ?
            """,
            (title, content, note_id, session["user_id"])
        )

        conn.commit()
        conn.close()

        flash("Note updated successfully!", "success")

        return redirect(url_for("dashboard"))

    conn.close()

    return render_template("edit_note.html", note=note)


# -----------------------------
# Delete Note
# -----------------------------

@app.route("/delete/<int:note_id>", methods=["POST"])
@login_required
def delete_note(note_id):

    conn = get_db()

    conn.execute(
        """
        DELETE FROM notes
        WHERE id = ? AND user_id = ?
        """,
        (note_id, session["user_id"])
    )

    conn.commit()
    conn.close()

    flash("Note deleted successfully!", "success")

    return redirect(url_for("dashboard"))


# -----------------------------
# Run Application
# -----------------------------

if __name__ == "__main__":
    init_db()
    app.run(debug=True)