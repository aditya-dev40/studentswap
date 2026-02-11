# StudentSwap

A Django-based student marketplace for buying, selling, and exchanging second-hand items.

StudentSwap allows users to list products, manage a shopping cart, and securely register with email verification. The project demonstrates full-stack fundamentals including authentication, cart logic, environment configuration, and modern frontend–backend communication.

---

## Current Features

- Add, update, and delete cart items
- Product listing and detail pages
- User registration & login system
- Email verification during registration
- Secure environment variable management using `.env`

---

## Features In Progress / Planned

- Order placement system
- Shipping information & tracking
- Payment gateway integration
- Cloud storage integration (e.g., AWS S3)
- Production database setup (PostgreSQL / MySQL)
- Item exchange with price difference adjustment

---

## 🛠️ Tech Stack

- Python
- Django
- HTML / CSS / Bootstrap
- JavaScript (Fetch API)
- SQLite (Development Database)
- SMTP (Email Verification)

---

## ⚙️ Installation & Setup Guide

### Clone the Repository

```bash
git clone https://github.com/yourusername/studentswap.git
cd studentswap
```

---

### Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

**Windows**
```bash
.venv\Scripts\activate
```

**Mac/Linux**
```bash
source .venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file in the project root directory.

You can copy the provided `.env.example` file and fill in your credentials.

Example configuration:

```
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

### Gmail Setup Instructions

- Enable 2-Step Verification in your Google account.
- Generate an **App Password**.
- Use that App Password instead of your actual Gmail password.

Do NOT commit your `.env` file to version control.

---

### 5️Apply Database Migrations

```bash
python manage.py migrate
```

---

### Run the Development Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

## Email Verification

- When a new user registers, a verification email is sent.
- The user must click the verification link to activate the account.
- SMTP credentials must be configured in the `.env` file for this feature to work.

---

## Security Notes

- Sensitive credentials are stored in `.env`
- `.env.example` is included for reference
- `.env` is excluded via `.gitignore`

---

## Future Improvements

- Full order lifecycle management
- Shipping module integration
- Cloud storage for media files
- Production-ready database configuration
- Deployment to AWS / Render

---

## Author

Aditya Thorat  
B.Tech (CSE) | Aspiring Software Developer
