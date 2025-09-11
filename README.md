
**Carbon Track**
Overview
Carbon Track is system that leverages IoT sensors to continuously collect emissions and energy usage data across multiple factory. The project features a Django REST Framework backend API with endpoints for user energy entry, emissions, compliance, factory, and MCU devices. Interactive API documentation is provided via Swagger and Redoc.


**Features**
User registration, login, and authentication
CRUD operations on energy entry, emissions, compliance, factory, and MCU devices
API documentation with Swagger UI and Redoc
Modular architecture for easy extension and maintenance
Secure endpoints with configurable authentication and permissions

**Technology Stack**
Python 3.13+
Django 4.2+
Django REST Framework
drf-yasg (Swagger / Redoc API docs)
PostgreSQL
Token authentication
Getting Started
Prerequisites
Python 3.13 or higher
pip package manager
Virtual environment tool
Database

**Installation**
Clone this repository:
git clone https://github.com/akirachix/carbontrack-backend.git
cd carbontrack

**Create and activate a virtual environment:**
Linux/macOS:
python -m venv venv
source venv/bin/activate
Windows:
python -m venv venv
venv\Scripts\activate

**Install dependencies:**
uv pip install -r requirements.txt
Set environment variables and update settings.py
Configure your database, secret keys, and static/media paths
Run database migrations:
python manage.py migrate
Create a superuser for admin access:
python manage.py createsuperuser
Collect static files:
python manage.py collectstatic
Start the development server:
python manage.py runserver

**API Documentation**
Swagger UI: https://carbon-track-680e7cff8d27.herokuapp.com/api/schema/swagger-ui/
Redoc: https://carbon-track-680e7cff8d27.herokuapp.com/api/schema/redoc/

**Usage**
Access API root at https://carbon-track-680e7cff8d27.herokuapp.com/api/ to explore available endpoints.
Use /register/, /login/, and other API endpoints for user authentication and resource management.
Modify authentication and permission settings in settings.py according to your needs.

About
No description, website, or topics provided.
Resources
Readme
Activity
Custom properties
Stars
0 stars
Watchers
0 watching
Forks
0 forks
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Contributors
6

**Languages**
Python
99.7%
 
Procfile
0.3%
Footer
© 2025 GitHub, Inc.






