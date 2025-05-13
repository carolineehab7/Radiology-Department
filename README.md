# Radiology-Department

## Overview

This project is a comprehensive digital health platform for a radiology department, designed to streamline patient registration, and diagnostic imaging services. The system provides access to various radiology services including MRI, CT scans, Ultrasound, and Digital X-rays.

## Features

### 🧑‍⚕️ User Authentication
- Patient registration and login
- Secure session management

### 🏥 Diagnostic Services
- MRI scheduling and information
- CT scan services
- Ultrasound examinations
- Digital X-ray imaging

### 👤 Patient Management
- Secure patient data storage
- Medical history tracking

### 💻 Interactive UI
- Responsive design across all device types
- Intuitive navigation
- Service-specific information pages

### 🛠️ Administrative Features
- Founders information page
- Working hours display
- Contact information section

---

## 🧰 Technologies Used

### Backend
- Python 3.x
- Flask web framework
- PostgreSQL database

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap (responsive design)
- Boxicons (icon library)

### Database
- PostgreSQL 
- psycopg2 for database connections

---

## 📁 Folder Structure
```
Final Project/
├── app.py                   # Main Flask application
├── static/                  # Static files (CSS, JS, images)
│   ├── images/              # Image assets
│   ├── homepage.css         # CSS for homepage
│   ├── x-ray.css            # CSS for X-ray page
│   ├── x-ray.js             # JavaScript for X-ray page
│   ├── homepage.js          # JavaScript for homepage
│   └── founders.css         # CSS for founders page
├── templates/               # HTML templates
│   ├── homepage.html        # Homepage template
│   ├── x-ray.html           # X-ray service page
│   ├── MRI.html             # MRI service page
│   ├── CT.html              # CT scan service page
│   ├── Ultrasound.html      # Ultrasound service page
│   ├── Founders.html        # Founders information page
│   ├── loginPA.html         # Patient login page
│   └── registerPA.html      # Patient registration page
```

---

## 🗃️ Database Schema

**`patient`**  
Stores patient information, including:
- Personal details (name, DOB, contact)
- Medical history

---

## 🚀 Usage

1. Register as a new patient using the **Sign Up** page.
2. Log in with your credentials.
3. Browse and access available radiology services.

---

## 🔒 Security Features

- Password protection with hashing
- Form input validation
- Secure session handling
- Parameterized database queries to prevent SQL injection

---

## 📬 Contact

For any inquiries or feedback, refer to the contact section on the website.

---

## Team Members

| Name               | 
| ------------------ | 
| Caroline Ehab      | 
| Habiba Mamdouh     | 
| Khadija Elfeky     | 
| Mohamed Abdelrazik | 

## Screenshots
### Homepage
![image](https://github.com/user-attachments/assets/d60f9cca-0953-45d3-aafd-dd2cd7e11626)
![image](https://github.com/user-attachments/assets/e3c65a19-eaef-490c-9511-6438d4109446)

### MRI 
![image](https://github.com/user-attachments/assets/fc6b5180-1efa-40e9-80f0-04c65a2fbbaa)

### Meet Our Founders
![image](https://github.com/user-attachments/assets/e60312b8-7038-4cd9-837a-7968d5e56405)

### Login
![image](https://github.com/user-attachments/assets/c6fcdefe-cc01-4b47-bd61-097d5425bafa)

### Register
![image](https://github.com/user-attachments/assets/214f9615-54a0-4f37-ba78-5f7b7646f71a)




