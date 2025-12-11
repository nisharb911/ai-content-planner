# AI Content Planner – Django + Supabase Web Application

A simple, production-ready web application built with **Django**, **Django REST Framework**, and **Supabase PostgreSQL**.

This project was created as part of a Social Media Marketing Company assignment and demonstrates:

- ✔ Full CRUD (Create, Read, Update, Delete) via REST APIs  
- ✔ PostgreSQL database hosted on **Supabase**  
- ✔ Admin panel for managing content  
- ✔ Modern Python project structure  
- ✔ Ready to deploy on Render / Railway / Supabase Edge  

---

## 🚀 Features

### 🟦 1. CRUD API (Django REST Framework)
The application exposes REST endpoints:

| Method | Endpoint              | Description            |
|--------|------------------------|------------------------|
| GET    | `/api/posts/`         | List all posts        |
| POST   | `/api/posts/`         | Create a new post     |
| GET    | `/api/posts/<id>/`    | Retrieve a post       |
| PUT    | `/api/posts/<id>/`    | Update a post         |
| DELETE | `/api/posts/<id>/`    | Delete a post         |

---

### 🟩 2. Supabase PostgreSQL Integration
The `DATABASES` config in `settings.py` connects Django directly to a **Supabase-hosted PostgreSQL** instance.

---

### 🟧 3. Admin Dashboard
Visit:

http://127.0.0.1:8000/admin/


Here you can:
- Add new posts
- Edit existing content
- Manage users

---

## 📁 Project Structure

backend/
├── backend/ # Project settings
│ ├── settings.py
│ ├── urls.py
├── planner/ # App for CRUD operations
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── admin.py
├── manage.py


---

## 🛠 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd backend

2. Create a Virtual Environment
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

(If requirements.txt isn’t included, install manually:)
pip install django djangorestframework psycopg2-binary supabase python-dotenv

4. Apply Migrations
python manage.py makemigrations
python manage.py migrate

5. Create Superuser
python manage.py createsuperuser

6. Run Server
python manage.py runserver

Open in browser:
http://127.0.0.1:8000/api/posts/
http://127.0.0.1:8000/admin/
