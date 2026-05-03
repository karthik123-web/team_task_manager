from flask import Flask, request, jsonify, render_template
import sqlite3
import os

app = Flask(__name__)

# ---------- DATABASE ----------
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT,
            role TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            status TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            created_by INTEGER
        )
    """)

    conn.commit()
    conn.close()


# ---------- PAGES ----------
@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/signup_page")
def signup_page():
    return render_template("signup.html")


@app.route("/dashboard_page")
def dashboard_page():
    return render_template("dashboard.html")


@app.route("/projects")
def projects_page():
    return render_template("projects.html")


# ---------- AUTH ----------
@app.route("/signup", methods=["POST"])
def signup():
    data = request.json

    try:
        conn = get_db()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)",
            (data["name"], data["email"], data["password"], data["role"])
        )

        conn.commit()
        conn.close()

        return jsonify({"success": True})

    except Exception:
        return jsonify({"success": False, "message": "Email already exists"})


@app.route("/login", methods=["POST"])
def login():
    data = request.json

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (data["email"], data["password"])
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({"success": True, "user": dict(user)})

    return jsonify({"success": False})


# ---------- TASK ----------
@app.route("/create_task", methods=["POST"])
def create_task():
    data = request.json

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)",
        (
            data.get("title"),
            data.get("description"),
            "To Do"
        )
    )

    conn.commit()
    conn.close()

    return jsonify({"success": True})


@app.route("/get_tasks")
def get_tasks():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    conn.close()

    return jsonify([dict(t) for t in tasks])


@app.route("/update_task", methods=["POST"])
def update_task():
    data = request.json

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET status=? WHERE id=?",
        (data["status"], data["task_id"])
    )

    conn.commit()
    conn.close()

    return jsonify({"success": True})


# ---------- DASHBOARD ----------
@app.route("/dashboard")
def dashboard():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM tasks")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tasks WHERE status='Done'")
    done = cursor.fetchone()[0]

    conn.close()

    return jsonify({
        "total": total,
        "completed": done,
        "pending": total - done
    })


# ---------- PROJECT ----------
@app.route("/create_project", methods=["POST"])
def create_project():
    data = request.json

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO projects (name, created_by) VALUES (?, ?)",
        (
            data.get("name"),
            data.get("created_by")
        )
    )

    conn.commit()
    conn.close()

    return jsonify({"success": True})


@app.route("/get_projects")
def get_projects():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()

    conn.close()

    return jsonify([dict(p) for p in projects])


@app.route("/test")
def test():
    return "Flask is working"

import os

if __name__ == "__main__":
    # Railway provides the port via environment variables
    port = int(os.environ.get("PORT", 5000))
    # '0.0.0.0' is required to make the server reachable externally
    app.run(host='0.0.0.0', port=port)
