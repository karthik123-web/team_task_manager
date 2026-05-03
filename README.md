# 🧑‍💻 Team Task Manager

A full-stack web application for managing team projects and tasks. Users can register, log in, create projects, assign tasks, and track task progress using a dashboard.

---

## 🚀 Features

- User Signup and Login
- Create and Manage Projects
- Create Tasks with Title and Description
- Update Task Status (To Do / Done)
- Dashboard showing:
  - Total Tasks
  - Completed Tasks
  - Pending Tasks
- SQLite database integration
- REST API using Flask

---

## 🛠️ Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Flask (Python)
- Database: SQLite

---

## 📁 Project Structure

```

team-task-manager/
│
├── app.py
├── database.db
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── projects.html
├── requirements.txt
├── README.md

````

---

## ⚙️ Installation & Setup

### 1. Clone repository
```bash
git clone https://github.com/your-username/team-task-manager.git
````

---

### 2. Go to project folder

```bash
cd team-task-manager
```

---

### 3. Create virtual environment

```bash
python -m venv venv
```

---

### 4. Activate virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

---

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 6. Run the application

```bash
python app.py
```

---

### 7. Open in browser

```
http://127.0.0.1:5000
```

---

## 📌 API Endpoints

* `POST /signup` → Register user
* `POST /login` → Login user
* `POST /create_task` → Create task
* `GET /get_tasks` → Get all tasks
* `POST /update_task` → Update task status
* `GET /dashboard` → Dashboard stats
* `POST /create_project` → Create project
* `GET /get_projects` → Get projects

---

## 🎯 Future Improvements

* Role-based access (Admin / Member)
* Assign tasks to users
* Project-wise task filtering
* Due date tracking
* Kanban board UI
* Deployment on Railway / Render
