## 💻 Project Title: Computer-Based Test Portal (CBP) with Django REST API
#### 🧾 Project Description
The Computer-Based Portal (CBP) is a web-based platform developed using Django REST Framework (DRF) that serves as a modular and scalable backend system for managing user accounts, roles like student and admin, Multiple Choice Questions(MCQ) exam functionality for courses,Final Score of students.

#### 🛠️ Tech Stack

Backend: Django, Django REST Framework

Database: SQLite

Authentication: Token-based (DRF Tokens or JWT)

API Testing: Postman / Swagger (DRF schema)

Frontend: Not yet Done

#### ✨ Key Features
**✅ User Authentication & Role Management**

User registration and login APIs (Students, Admin)

Role-based access control (RBAC)

Throttling to limit no. of request

Password hashing and token authentication

**📚 Exam Management Module**

Admin/staff can create courses, exams, question banks,questions choices,department,marks,duration of exam

Students can able to login access their exam for perticular course ,attempt the MCQ exam ,see their results 


**📊 Results & Evaluation**
Auto-evaluation for MCQs

Result APIs per exam,student

**⚙️ Admin Panel APIs**

Create/view/update/delete users, courses, exams, questions and choices


**📂 Description of various component/apps of CBT Project**
1. **accounts**:
    Models are Admin,Student,User
    Serializer for Login,Signup,Student,Admin
    Views for serializer


2. **Courses:**

    registration of courses and exams 

3. **questions**

    questions for exams and choices for questions

4. **results**

    Exam Results and Student Attempt

**🎯 Use Case Scenarios**

Online student assessments

Training evaluation systems

Internal company knowledge testing

Coaching center exam platforms

#### ✅ Status
 Only Backend API Completed

 

#### 🔐 Security

DRF token-based or JWT authentication

Login & rate limiting access to endl-points

Student-Only access for students who are registered and authenticated.


#### Documentation
drf-spectacular for documentation
Or can use Postman for documentation

## How to Run Code 

cd section-06

drfenv\scripts\activate

cd cbt_portal

python manage.py runserver

python manage.py createsuperuser
