# Zizo Jobs

A professional and minimalistic job board built with Django.

## Features

- User authentication and profiles
- Company registration and management
- Job posting and application
- Notifications system
- Payment integration
- Search functionality

## Requirements

- Python 3.10+
- Django 4.2+
- PostgreSQL

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/CHepplethwaite/zizo-jobs.git
cd zizo-jobs

2. Create a virtual environment

python -m venv venv

3. Activate the virtual environment

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

5. Apply migrations

python manage.py migrate

6. Create a superuser

python manage.py createsuperuser

7. Run the development server

python manage.py runserver

Visit http://127.0.0.1:8000/ to access the application.

Project Structure

accounts/         # User accounts and authentication
applications/     # Job applications
companies/        # Employer and recruiter management
core/             # Shared utilities and base configurations
dashboard/        # User dashboards
jobs/             # Job listing and management
notifications/    # System notifications
payments/         # Payment processing
search/           # Search functionality
manage.py         # Django management script
requirements.txt  # Project dependencies
README.md         # Documentation
License

This project is licensed under the MIT License.
