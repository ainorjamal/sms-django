SMS-Django Application

Overview

The SMS-Django application is a Django-based project designed to send earthquake alerts via SMS. The application uses the Twilio API to send automated messages to a predefined recipient whenever a new earthquake magnitude entry is recorded in the database. This system provides critical updates to ensure the safety of individuals during emergency situations.

---

Installation Guide

Follow these steps to set up and run the SMS-Django application on your local machine:

Step 1: Clone the Repository

```bash
git clone https://github.com/ainorjamal/sms-django
```

Step 2: Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # For Linux/MacOS
.venv\Scripts\activate    # For Windows
```

Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Step 4: Configure Environment Variables

Create a `.env` file in the root directory and add your Twilio credentials:

```
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
```

Step 5: Apply Migrations

```bash
python manage.py migrate
```

Step 6: Run the Development Server

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`.

---

Features

- Automated SMS Alerts: Sends an SMS notification when a new earthquake magnitude entry is added to the database.
- Twilio Integration: Utilizes the Twilio API for reliable message delivery.
- Admin Interface: Allows easy management of earthquake magnitude records through Django's admin panel.
- Error Logging: Logs the success or failure of SMS delivery.

Usage Instructions

1. Log in to the Django admin panel at `http://127.0.0.1:8000/admin/`.
2. Add a new entry under the `Magnitude` model, specifying the earthquake magnitude.
3. Upon saving the entry, an SMS alert is automatically sent to the predefined recipient number.

Tech Stack

- Backend Framework: Django 5.1.3
- Programming Language: Python 3.12.1
- API Integration: Twilio API for SMS delivery
- Database: SQLite (default setup, configurable)

Configuration Notes

Twilio Setup

To enable SMS functionality, ensure you have a Twilio account. Follow these steps to set up Twilio:

1. Visit [Twilio's website](https://www.twilio.com/) and sign up for an account.
2. Retrieve your **Account SID**, **Auth Token**, and **Twilio Phone Number** from the Twilio console.
3. Add these credentials to your `.env` file as described above.

Environment Variables

To ensure security, sensitive information such as Twilio credentials is managed using the `python-decouple` library. Ensure your `.env` file is properly configured.

Admin Panel

- Access the Django admin interface at `http://127.0.0.1:8000/admin/`.
- Default database entries can be managed through the `Magnitude` model.

