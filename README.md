<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Carbon Track Overview</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- Font Awesome CDN for icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
  <style>
    body {
      font-family: 'Segoe UI', Arial, sans-serif;
      background: #f7fafc;
      color: #22223b;
      margin: 0;
      padding: 0;
    }
    .container {
      max-width: 820px;
      margin: 32px auto;
      background: #fff;
      border-radius: 16px;
      box-shadow: 0 4px 18px rgba(0,0,0,0.08);
      padding: 32px 40px;
    }
    h1, h2, h3 {
      margin-top: 1.5em;
      margin-bottom: 0.7em;
      font-weight: 700;
      color: #30475e;
      display: flex;
      align-items: center;
      gap: 0.5em;
    }
    h1 {
      font-size: 2.2em;
    }
    h2 {
      font-size: 1.5em;
      border-bottom: 2px solid #ececec;
      padding-bottom: 0.1em;
    }
    h3 {
      font-size: 1.13em;
      color: #4f7396;
    }
    ul, ol {
      margin-left: 1.8em;
      margin-bottom: 1em;
    }
    a {
      color: #0077b6;
      text-decoration: none;
      transition: color 0.2s;
    }
    a:hover {
      color: #023e8a;
      text-decoration: underline;
    }
    code, pre {
      background: #f0f0f0;
      border-radius: 4px;
      padding: 2px 6px;
      font-size: 1em;
    }
    .api-links {
      display: flex;
      flex-wrap: wrap;
      gap: 0.8em;
      margin: 0.5em 0 1.2em 0;
    }
    .api-links a {
      background: #f1f6f9;
      padding: 6px 12px;
      border-radius: 8px;
      border: 1px solid #e3e7ed;
      font-size: 0.97em;
      display: flex;
      align-items: center;
      gap: 0.5em;
      transition: background 0.2s;
    }
    .api-links a:hover {
      background: #e8f0fe;
    }
    .stats {
      display: flex;
      gap: 2em;
      flex-wrap: wrap;
      margin: 1.5em 0;
      font-size: 0.97em;
      color: #5f6c7b;
    }
    .footer {
      text-align: center;
      color: #8d99ae;
      margin-top: 32px;
      font-size: 0.97em;
    }
    @media (max-width: 600px) {
      .container { padding: 16px 5vw; }
      h1 { font-size: 1.4em; }
      h2 { font-size: 1.1em; }
    }
  </style>
</head>
<body>
  <div class="container">
    <h1><i class="fa-solid fa-leaf"></i> Carbon Track</h1>
    <h2><i class="fa-solid fa-circle-info"></i> Overview</h2>
    <p>
      Carbon Track is a system that leverages IoT sensors to continuously collect emissions and energy usage data across multiple factories.<br>
      The project features a Django REST Framework backend API with endpoints for user energy entry, emissions, compliance, factory, and MCU devices.<br>
      Interactive API documentation is provided via Swagger and Redoc.
    </p>
    <h2><i class="fa-solid fa-star"></i> Features</h2>
    <ul>
      <li>User registration, login, and authentication</li>
      <li>CRUD operations on energy entry, emissions, compliance, factory, and MCU devices</li>
      <li>API documentation with Swagger UI and Redoc</li>
      <li>Modular architecture for easy extension and maintenance</li>
      <li>Secure endpoints with configurable authentication and permissions</li>
    </ul>

    <h2><i class="fa-solid fa-microchip"></i> Technology Stack</h2>
    <ul>
      <li>Python 3.13+</li>
      <li>Django 4.2+</li>
      <li>Django REST Framework</li>
      <li>drf-yasg (Swagger/Redoc API docs)</li>
      <li>PostgreSQL</li>
      <li>Token authentication</li>
    </ul>

    <h2><i class="fa-solid fa-rocket"></i> Getting Started</h2>
    <h3><i class="fa-solid fa-toolbox"></i> Prerequisites</h3>
    <ul>
      <li>Python 3.13 or higher</li>
      <li>pip package manager</li>
      <li>Virtual environment tool</li>
      <li>PostgreSQL database</li>
    </ul>

    <h3><i class="fa-solid fa-download"></i> Installation</h3>
    <ol>
      <li>Clone this repository:<br>
        <code>git clone https://github.com/akirachix/carbontrack-backend.git</code><br>
        <code>cd carbontrack</code>
      </li>
      <li>Create and activate a virtual environment:<br>
        <b>Linux/macOS:</b>
        <code>python -m venv venv</code><br>
        <code>source venv/bin/activate</code><br>
        <b>Windows:</b>
        <code>python -m venv venv</code><br>
        <code>venv\Scripts\activate</code>
      </li>
      <li>Install dependencies:<br>
        <code>uv pip install -r requirements.txt</code>
      </li>
      <li>Set environment variables and update <code>settings.py</code>.<br>
        Configure your database, secret keys, and static/media paths.
      </li>
      <li>Run database migrations:<br>
        <code>python manage.py migrate</code>
      </li>
      <li>Create a superuser for admin access:<br>
        <code>python manage.py createsuperuser</code>
      </li>
      <li>Collect static files:<br>
        <code>python manage.py collectstatic</code>
      </li>
      <li>Start the development server:<br>
        <code>python manage.py runserver</code>
      </li>
    </ol>

    <h2><i class="fa-solid fa-book"></i> API Documentation</h2>
    <div class="api-links">
      <a href="https://carbon-track-680e7cff8d27.herokuapp.com/api/schema/swagger-ui/" target="_blank"><i class="fa-brands fa-swagger"></i> Swagger UI</a>
      <a href="https://carbon-track-680e7cff8d27.herokuapp.com/api/schema/redoc/" target="_blank"><i class="fa-solid fa-book-open"></i> Redoc</a>
      <a href="https://documenter.getpostman.com/view/45609889/2sB3HooJrj" target="_blank"><i class="fa-solid fa-flask"></i> Postman Docs</a>
    </div>

    <h2><i class="fa-solid fa-play"></i> Usage</h2>
    <ul>
      <li>Access API root at <a href="https://carbon-track-680e7cff8d27.herokuapp.com/api/" target="_blank">API Root</a> to explore available endpoints.</li>
      <li>Use <code>/register/</code>, <code>/login/</code>, and other API endpoints for user authentication and resource management.</li>
      <li>Modify authentication and permission settings in <code>settings.py</code> according to your needs.</li>
    </ul>

    <h2><i class="fa-solid fa-circle-question"></i> About</h2>
    <ul>
      <li>No description, website, or topics provided.</li>
      <li>6 contributors</li>
    </ul>

    <h2><i class="fa-solid fa-chart-pie"></i> Stats</h2>
    <div class="stats">
      <div><i class="fa-regular fa-star"></i> 0 stars</div>
      <div><i class="fa-regular fa-eye"></i> 0 watchers</div>
      <div><i class="fa-solid fa-code-branch"></i> 0 forks</div>
      <div><i class="fa-solid fa-code"></i> Python 99.7%</div>
      <div><i class="fa-solid fa-file-lines"></i> Procfile 0.3%</div>
    </div>

    <div class="footer">
      &copy; 2025 GitHub, Inc.
    </div>
  </div>
</body>
</html>
