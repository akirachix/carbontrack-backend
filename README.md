
#Carbon Track


---

##Overview

<br>
Carbon Track is system that leverages IoT sensors to continuously collect emissions and energy usage data across multiple factory. The project features a Django REST Framework backend API with endpoints for user energy entry, emissions, compliance, factory, and MCU devices. Interactive API documentation is provided via Swagger and Redoc.

---

 ##Features   <br>

* **User registration, login, and authentication <br>
* **CRUD operations on energy entry, emissions, compliance, factory, and MCU devices <br>
* **API documentation with Swagger UI and Redoc <br>
* **Modular architecture for easy extension and maintenance <br>
* **Secure endpoints with configurable authentication and permissions <br>

---

 ##Technology Stack <br>
 
* **Django 4.2+ 
* **Django REST Framework 
* **drf-yasg (Swagger / Redoc API docs) 
* **PostgreSQL 
* **Token authentication 
* **Getting Started 
* **Prerequisites 
* **Python 3.13 or higher 
* **pip package manager 
* **Virtual environment tool 
*Database 

---
<h3>
 Installation<br>
</h3>
Clone this repository: <br>
git clone https://github.com/akirachix/carbontrack-backend.git <br>
cd carbontrack <br>

---
<h3>
  Create and activate a virtual environment: <br>
</h3>
-Linux/macOS: <br>
-python -m venv venv <br>
-source venv/bin/activate <br>
-Windows: <br>
-python -m venv venv <br>
-venv\Scripts\activate <br>

---
<h3>
  Install dependencies <br>
</h3>
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
<h3>
  API Documentation<br>
</h3>

Swagger UI: [Link](https://carbon-track-680e7cff8d27.herokuapp.com/api/schema/swagger-ui/) <br>
Redoc: [Link](https://carbon-track-680e7cff8d27.herokuapp.com/api/schema/redoc/) <br>
Postman Documentation: [link](https://documenter.getpostman.com/view/45609889/2sB3HooJrj)

---
<h3>
  Usage <br>
</h3>

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
<h3>
**Contributors**</h3>
<br>
 6

---
<h3>
 Languages <br>
</h3>
Python <br>
99.7% <br>

Procfile <br>
0.3% <br>


---

<p align="center">
 © 2025 GitHub, Inc.
</p>
