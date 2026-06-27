Django Notes App

A clean and maintainable Notes application built with Django using Class-Based Views (CBVs) and modern Django development practices.

- ### **Translated versions**
    - [Persian Version - فارسی](READMEir.md)

---

✨ Features

- Create new notes
- Browse all notes
- View note details
- Update existing notes
- Delete notes with confirmation
- Search notes by title
- Automatic timestamps ("created_at" / "updated_at")
- Form validation with Django "ModelForm"
- Secure forms using CSRF protection
- Clean architecture based on Django CBVs

---

🛠️ Tech Stack

- Python 3
- Django
- SQLite
- HTML5
- Django Template Language (DTL)

---

📂 Project Structure

notes-app/
├── config/
├── notes/
│   ├── migrations/
│   ├── templates/
│   │   └── notes/
│   ├── templatetags/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
└── README.md

---

📌 Implemented Features

CRUD Operations

- ✅ CreateView
- ✅ ListView
- ✅ DetailView
- ✅ UpdateView
- ✅ DeleteView

Search

Search notes by title using Django ORM filtering.

Forms

- Django ModelForm
- Custom widgets
- Placeholder support
- Built-in validation

Security

- CSRF Protection
- Safe Delete Confirmation
- Django Form Validation

---

🚀 Getting Started

Clone the repository

git clone https://github.com/<your-username>/notes-app.git

Create a virtual environment

python -m venv .venv

Activate the virtual environment

Windows

.venv\Scripts\activate

Linux / macOS

source .venv/bin/activate

Install dependencies

pip install -r requirements.txt

Apply migrations

python manage.py migrate

Run the development server

python manage.py runserver

---

🎯 Learning Goals

This project is designed to practice and understand:

- Django Models
- Django ORM
- Class-Based Views
- ModelForms
- URL Routing
- Template Inheritance
- CRUD Operations
- Search Functionality
- Git & GitHub Workflow

---

🔮 Future Improvements

- User Authentication
- Bootstrap UI
- Pagination
- Categories & Tags
- Rich Text Editor
- REST API (Django REST Framework)
- Docker Support
- Automated Testing
- Deployment

---

📄 License

This project is created for learning purposes and is open for educational use.