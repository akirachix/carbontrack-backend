<h1>
 Carbon Track
</h1>

---
<h3>
 Overview
</h3>
<br>
Carbon Track is system that leverages IoT sensors to continuously collect emissions and energy usage data across multiple factory. The project features a Django REST Framework backend API with endpoints for user energy entry, emissions, compliance, factory, and MCU devices. Interactive API documentation is provided via Swagger and Redoc.

---
<h3>
 Features 
</h3>

*   User registration, login, and authentication <br>
*   CRUD operations on energy entry, emissions, compliance, factory, and MCU devices <br>
*   API documentation with Swagger UI and Redoc <br>
*   Modular architecture for easy extension and maintenance <br>
*   Secure endpoints with configurable authentication and permissions <br>
---
<h3>
 Technology Stack 
</h3>

*  Django 4.2+ <br>
*  Django REST Framework <br>
*  drf-yasg (Swagger / Redoc API docs) <br>
*  PostgreSQL <br>
*  Token authentication <br>
*  Getting Started <br>
*  Prerequisites <br>
*  Python 3.13 or higher <br>
*  pip package manager <br>
*  Virtual environment tool <br>
*  Database <br>
---
<h3>
 Installation<br>
</h3>
Clone this repository: <br>

```sh
  git clone https://github.com/akirachix/carbontrack-backend.git 
```
cd carbontrack <br>
---
<h3>
  Create and activate a virtual environment: <br>
</h3>
*  Linux/macOS: <br>
*  python -m venv venv <br>
*  source venv/bin/activate <br>
*  Windows: <br>
*  python -m venv venv <br>
*  venv\Scripts\activate <br>

---
<h3>
  Install dependencies <br>
</h3>

```sh
 uv pip install -r requirements.txt 
 ```
 Set environment variables and update settings.py <br>
-Configure your database, secret keys, and static/media paths <br>
-Run database migrations: <br>

```sh
-python manage.py migrate 
```
 Create a superuser for admin access: <br>
 ```sh
 python manage.py createsuperuser
 ```
-Collect static files: <br>
```sh
 python manage.py collectstatic 
 ```
 Start the development server: <br>
 ```sh
  python manage.py runserver 
```

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
