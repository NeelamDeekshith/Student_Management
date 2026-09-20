
# 🎓 Flask Student Management System

A simple and user-friendly **Student Management System** built with **Python Flask and SQLite** for managing student records through a web-based interface.

The application provides complete **CRUD (Create, Read, Update, Delete)** functionality, allowing users to efficiently add, search, update, and delete student information.

---

## 📌 Project Overview

Managing student records manually can be time-consuming and difficult to maintain. This project provides a lightweight web-based solution for maintaining student information in a structured database.

The application demonstrates the implementation of:

- 🌐 Web application development using Flask
- 🗄️ Database management using SQLite
- 🔄 CRUD operations
- 🔍 Student search and filtering
- 🎨 Server-side HTML rendering using Jinja2
- 📱 User-friendly web interface

---

## ✨ Features

### 👨‍🎓 Student Management

- ➕ Add new student records
- 👁️ View student information
- 🔍 Search students by:
  - Student ID
  - Name
  - Age
  - Course
- ✏️ Update existing student details
- 🗑️ Delete student records by ID

### 🗄️ Database

- Persistent student data storage using **SQLite**
- Simple relational database structure
- Data retrieval and modification through Flask

### 🎨 User Interface

- Clean and simple web interface
- Reusable Flask/Jinja2 templates
- CSS-based styling
- Easy navigation between different operations

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python 3** | Backend programming |
| **Flask** | Web application framework |
| **SQLite** | Database |
| **HTML5** | Web page structure |
| **CSS3** | User interface styling |
| **Jinja2** | Dynamic HTML templating |

---

## 🏗️ Application Architecture


┌─────────────────────────────┐
│          Web Browser        │
│       HTML / CSS / UI       │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│        Flask Web App        │
│          app.py             │
│                             │
│  ┌───────┐ ┌───────┐        │
│  │  Add  │ │ Search│        │
│  ├───────┤ ├───────┤        │
│  │ Update│ │ Delete│        │
│  └───────┘ └───────┘        │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       SQLite Database       │
│   Student Records Storage   │
└─────────────────────────────┘

###  Live Demo  
 [DEMO](https://student-management-system-flask.onrender.com/)


##
