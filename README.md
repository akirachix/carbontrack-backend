
<h1>
  Carbon Track
</h1>


---
<h3>
Overview<br>
</h3>
<br>
Carbon Track is system that leverages IoT sensors to continuously collect emissions and energy usage data across multiple factory. The project features a Django REST Framework backend API with endpoints for user energy entry, emissions, compliance, factory, and MCU devices. Interactive API documentation is provided via Swagger and Redoc.

---

**Features**<br>

*User registration, login, and authentication <br>
*CRUD operations on energy entry, emissions, compliance, factory, and MCU devices <br>
*API documentation with Swagger UI and Redoc <br>
*Modular architecture for easy extension and maintenance <br>
*Secure endpoints with configurable authentication and permissions <br>

---

**Technology Stack** <br>
<lu>
-Python 3.13+ <br>
-Django 4.2+ <br>
-Django REST Framework <br>
-drf-yasg (Swagger / Redoc API docs) <br>
-PostgreSQL <br>
-Token authentication <br>
-Getting Started <br>
-Prerequisites <br>
-Python 3.13 or higher <br>
-pip package manager <br>
-Virtual environment tool <br>
-Database <br>

---

**Installation** <br>
Clone this repository: <br>
git clone https://github.com/akirachix/carbontrack-backend.git <br>
cd carbontrack <br>

---

**Create and activate a virtual environment:** <br>
-Linux/macOS: <br>
-python -m venv venv <br>
-source venv/bin/activate <br>
-Windows: <br>
-python -m venv venv <br>
-venv\Scripts\activate <br>

---

**Install dependencies:** <br>
-uv pip install -r requirements.txt <br>
-Set environment variables and update settings.py <br>
-Configure your database, secret keys, and static/media paths <br>
-Run database migrations: <br>
-python manage.py migrate <br>
-Create a superuser for admin access: <br>
-python manage.py createsuperuser <br>
-Collect static files: <br>
-python manage.py collectstatic <br>
-Start the development server: <br>
-python manage.py runserver <br>

---

**API Documentation** <br>
Swagger UI:[Link](https://carbon-track-680e7cff8d27.herokuapp.com/api/schema/swagger-ui/) <br>
Redoc: [Link](https://carbon-track-680e7cff8d27.herokuapp.com/api/schema/redoc/) <br>
Postman Documentation: [Link](https://documenter.getpostman.com/view/45609889/2sB3HooJrj)

---

**Usage** <br>
Access API root at [Link](https://carbon-track-680e7cff8d27.herokuapp.com/api/) to explore available endpoints.
Use /register/, /login/, and other API endpoints for user authentication and resource management.
Modify authentication and permission settings in settings.py according to your needs.

---

About <br>
-No description, website, or topics provided. <br>
-Resources<br>
-Readme<br>
-Activity <br>
-Custom properties <br>
-Stars <br>
-0 stars <br>
-Watchers <br>
-0 watching <br>
-Forks <br>
-0 forks <br>
-Releases <br>
-No releases published <br>
-Create a new release <br>
-Packages <br>
-No packages published <br>
-Publish your first package <br>

**Contributors** <br>
 6

---

**Languages** <br>
Python <br>
99.7% <br>

Procfile <br>
0.3% <br>


---

<p align="center">
 © 2025 GitHub, Inc.
</p>
