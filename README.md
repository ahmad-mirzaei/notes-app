# Notes App

A simple Notes application built with Django following modular and scalable architecture principles.

Features

- Create notes
- List notes
- Update notes (planned)
- Delete notes (planned)

Tech Stack

- Python
- Django
- SQLite
- Class-Based Views (CBV)
- Django Forms

Project Structure

notes_app/
├── config/
├── notes/
├── manage.py
├── requirements.txt
└── README.md

Installation

Clone the repository

git clone <repository-url>
cd notes_app

Create and activate virtual environment

python -m venv venv

Windows:

venv\Scripts\activate

Linux/macOS:

source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Apply migrations

python manage.py migrate

Run development server

python manage.py runserver

Open:

http://127.0.0.1:8000/notes/

Current Progress

- [x] Django project setup
- [x] Notes app creation
- [x] Note model
- [x] Database migrations
- [x] Note list view
- [x] Note creation form
- [ ] Note update
- [ ] Note delete
- [ ] Authentication
- [ ] Production deployment

Learning Goals

This project is being developed to practice:

- Django architecture
- ORM
- Class-Based Views
- Forms and Validation
- CRUD operations
- Clean project structure

License

This project is for educational purposes.