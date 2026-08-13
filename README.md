# smart-agriculture-farm-management
Smart Agriculture &amp; Farm Management System built with FastAPI, SQLAlchemy, PostgreSQL, JWT Authentication, and role-based authorization.
# Smart Agriculture & Farm Management System

A backend application for managing farms, fields, crops, irrigation, treatments, harvests, sales, crop health, alerts, and user authentication.

The application is built using FastAPI, SQLAlchemy, PostgreSQL, Pydantic, and JWT authentication.



## Features

- User registration and login
- JWT-based authentication
- Role-based user registration
- Farm management
- Field management
- Crop management
- Irrigation management
- Treatment management
- Harvest management
- Sales management
- Crop health monitoring
- Crop alerts
- Input validation
- Error handling
- PostgreSQL database integration
- Interactive Swagger API documentation



## Technology Stack

- Python 3.x
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- JWT Authentication
- Uvicorn
- Pytest



## Project Structure

```text
smart-agriculture-farm-management/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── tests/
│   ├── utils/
│   ├── config.py
│   ├── database.py
│   ├── init_db.py
│   └── main.py
│
├── Swagger Screen Shots/
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt

Main Modules
Authentication
POST /auth/register
POST /auth/login
GET  /auth/me

Supports user registration, login, JWT token generation, and current-user authentication.

Farms
POST   /farms/
GET    /farms/
GET    /farms/{farm_id}
PUT    /farms/{farm_id}
Fields
POST   /fields/
GET    /fields/
GET    /fields/{field_id}
PUT    /fields/{field_id}
DELETE /fields/{field_id}
Crops
POST   /crops/
GET    /crops/
GET    /crops/{crop_id}
PUT    /crops/{crop_id}
DELETE /crops/{crop_id}
Irrigation
POST   /irrigation/
GET    /irrigation/
GET    /irrigation/{irrigation_id}
PUT    /irrigation/{irrigation_id}
DELETE /irrigation/{irrigation_id}
Treatment
POST   /treatments/
GET    /treatments/
GET    /treatments/{treatment_id}
PUT    /treatments/{treatment_id}
DELETE /treatments/{treatment_id}
Harvest
POST   /harvests/
GET    /harvests/
GET    /harvests/{harvest_id}
PUT    /harvests/{harvest_id}
DELETE /harvests/{harvest_id}
Sales
POST   /sales/
GET    /sales/
GET    /sales/{sale_id}
PUT    /sales/{sale_id}
DELETE /sales/{sale_id}
Crop Health
POST   /crop-health/
GET    /crop-health/
GET    /crop-health/{health_id}
PUT    /crop-health/{health_id}
DELETE /crop-health/{health_id}
Alerts
POST   /alerts/
GET    /alerts/
GET    /alerts/{alert_id}
PUT    /alerts/{alert_id}
DELETE /alerts/{alert_id}
Database Setup

This project uses PostgreSQL.
