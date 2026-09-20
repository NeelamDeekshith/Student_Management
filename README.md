#  Flask Student Management System

A web-based **Student Management System** built using **Flask** and **SQLite**. This application provides basic functionality to **Add**, **Search**, **Update**, and **Delete** student records through a clean and responsive HTML interface.

---

##  Features

-  Add new student with **ID, Name, Age, and Course**
-  Search for students by **ID, Name, Age, or Course**
-  Update student details (ID, Name, Age, Course)
-  Delete a student by **ID**
-  Persistent storage using **SQLite**
-  Clean and modular interface using **Flask templates (Jinja2)**

---

 ##  Use Cases

- College mini projects    
- Beginner Flask practice    
- CRUD app demonstration    
- Student record maintenance for small institutions    


##  Technologies Used

- **Python 3**
- **Flask** Web Framework
- **SQLite** Database
- **HTML5/CSS3** with **Jinja2** Templating

---

##  Project Structure

Student-Management-System/  
│ ├── app.py # Main Flask application  
├── Student_database_file.db # SQLite database file  
│ ├── templates/ # HTML templates for UI  
│ ├── base.html  
│ ├── add_student.html  
│ ├── search_student.html  
│ ├── update_student.html  
│ └── delete_student.html  
│ └── static/ # Static files (CSS, images, JS)  
└── style.css # Main CSS styling for the app  
##

##  Setup Instructions

###  Clone the Repository

    git clone https://github.com/YOUR_USERNAME/flask-student-management-system.git
    cd flask-student-management-system


 Create Virtual Environment (optional but recommended)

    python -m venv venv
    source venv/bin/activate      # Linux/macOS
    venv\Scripts\activate         # Windows
    
 Install Dependencies

    pip install flask
 Run the Application

    python app.py
Now open your browser and navigate to:

    http://localhost:5000


---

###  Live Demo  
 [DEMO](https://student-management-system-flask.onrender.com/)

---
    
 **Future Enhancements** 
 Add user authentication (Login/Register)  
 Add student image upload  
 Add pagination, search filters & better sorting  
 Export student data as Excel/PDF  
 Improve UI using Bootstrap or TailwindCSS  

##

 Author  
Made with ❤️ by Manju  
 Contact: manjuguru814@gmail.com
