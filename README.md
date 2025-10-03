# 🐍 DjangoApp

## 📖 Description
`DjangoApp` is a **Django project** named `testdjango`, designed for learning and practicing web development with Python and the Django framework.  
The application allows managing **students** and **courses**, provides forms for adding or editing data, and displays information through HTML templates.  
It also integrates with the Django admin panel for easy data administration.

## 🗂️ Project Structure
- `manage.py` – script for Django administrative commands (runserver, migrate, etc.).
- `db.sqlite3` – local SQLite database (auto-generated; stores student and course data).
- `testdjango/` – main Django project folder.
  - `settings.py` – project configuration (database, installed apps, middleware).
  - `urls.py` – main routing file for project-level URLs.
  - `asgi.py` / `wsgi.py` – deployment entry points.
- `aplicatietest/` – Django application containing core functionality:
  - `models.py` – defines the **Student** and **Course** models.
  - `forms.py` – defines Django forms for data entry/editing.
  - `views.py` – contains views to list students, display forms, and show student courses.
  - `urls.py` – app-level routing to map URLs to views.
  - `admin.py` – registers models in the Django admin panel.
  - `migrations/` – database migrations (initial table creation).
  - `templates/aplicatietest/` – HTML templates:
    - `studenti.html` – displays the list of students.
    - `formular.html` – form template for adding/editing students or courses.
    - `cursuri_student.html` – shows courses for a specific student.
- `__pycache__/` – Python cache files (should be ignored in Git).

## ⚙️ Features
- Manage **students** and **courses** through Django models.
- Add or edit entries using Django forms.
- List students and their enrolled courses.
- Integrated Django admin panel for easy data management.
- Simple and clean HTML templates for user-friendly interaction.

## 🛠️ Technologies Used
- **Python 3** – programming language.
- **Django** – web framework.
- **SQLite** – default database for development.
- **HTML** – template structure for the UI.

## 🚀 How to Run the Project
1. Clone the repository:
   git clone https://github.com/Axinte8543/DjangoApp.git
2. Install dependencies (make sure Python and pip are installed):
   pip install django
3. Run the development server:
   python manage.py runserver
4. Open your browser and go to:
   http://127.0.0.1:8000/

## 🔮 Future Improvements
- Add user authentication (login/register) for students or admin.
- Create a dashboard for managing courses and student enrollments.
- Implement data import/export (CSV, Excel) for easy data handling.
- Improve the UI design using Bootstrap or React for a modern look.
- Add automated tests for views, models, and forms.

## 👤 Author
Project created by **Axinte**.
