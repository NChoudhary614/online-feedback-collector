Online Feedback Collector with Admin Dashboard
A complete full-stack web application for collecting user feedback and displaying analytics in an interactive admin dashboard. Built with Flask, SQLite, and Bootstrap.

https://img.shields.io/badge/Python-3.8%252B-blue
https://img.shields.io/badge/Flask-2.3.3-green
https://img.shields.io/badge/License-MIT-yellow
https://img.shields.io/badge/Status-Completed-brightgreen

🎯 Project Overview
This project is a comprehensive feedback management system that allows users to submit feedback through a web form and provides administrators with tools to analyze the collected data through an interactive dashboard with charts and statistics.

✨ Features
User-Facing Features
📝 Feedback Form: Clean, responsive form with fields for name, email, rating (1-5 stars), and comments

✅ Real-time Validation: Client-side validation with instant feedback

🔄 AJAX Submission: Form submission without page reload

🎨 Responsive Design: Works on all devices (mobile, tablet, desktop)

Admin Features
🔐 Secure Login System: Password-protected admin dashboard

📊 Interactive Dashboard: Visual statistics and analytics

📈 Rating Distribution Chart: Visual representation using Chart.js

📋 Feedback Management: View all submissions in a sortable table

📥 Data Export: Export feedback data as CSV

🔌 REST API: JSON endpoint for programmatic access (/api/feedback)

Technical Features
💾 Database Integration: SQLite database with proper schema

🔄 CRUD Operations: Full Create, Read operations

🛡️ Form Security: Input validation and sanitization

📁 Project Structure: Organized MVC-like structure

🛠️ Tech Stack
Technology	Purpose
Python	Backend programming language
Flask	Web framework and routing
SQLite	Database for storing feedback
HTML/CSS	Frontend structure and styling
JavaScript	Frontend interactivity and AJAX
Bootstrap 5	Responsive UI components
Chart.js	Data visualization for charts
Jinja2	Template engine for Flask
📁 Project Structure
text
OnlineFeedbackCollector/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── database.db              # SQLite database (auto-generated)
├── README.md                # Project documentation
├── static/
│   ├── css/
│   │   └── style.css        # Custom CSS styles
│   └── js/
│       └── script.js        # JavaScript utilities
└── templates/
    ├── layout.html          # Base template with navigation
    ├── index.html           # Home page with feedback form
    └── admin.html           # Admin dashboard
🚀 Quick Start
Prerequisites
Python 3.8 or higher

pip (Python package manager)

Installation
Clone the repository

bash
git clone https://github.com/YOUR_USERNAME/online-feedback-collector.git
cd online-feedback-collector
Install dependencies

bash
pip install -r requirements.txt
Run the application

bash
python app.py
Access the application

Open your browser and navigate to: http://localhost:5000

Default Admin Credentials
Username: admin

Password: admin123

Note: Change these credentials in production!

📊 Features in Detail
1. Feedback Submission
https://screenshots/form.png

User-friendly form with star rating system

Email validation

Real-time feedback on submission

2. Admin Dashboard
https://screenshots/dashboard.png

Statistics Cards: Total feedback, average rating, recent submissions

Interactive Chart: Rating distribution visualization

Feedback Table: View all submissions with sorting

Export Tools: One-click CSV export

3. Data Export
Export all feedback data to CSV format

Compatible with Excel, Google Sheets, and data analysis tools

4. REST API
http
GET /api/feedback
Returns all feedback data in JSON format for integration with other applications.

🔧 API Endpoints
Method	Endpoint	Description	Authentication
GET	/	Home page with feedback form	Public
POST	/submit-feedback	Submit new feedback	Public
GET	/admin-dashboard	Admin dashboard	Admin only
GET	/api/feedback	JSON API for feedback data	Admin only
GET	/export-csv	Export data as CSV	Admin only
GET/POST	/login	Admin login	Public
📸 Screenshots
Home Page
text
http://localhost:5000/
The landing page with feedback form and project information.

Admin Dashboard
text
http://localhost:5000/admin-dashboard
Login required. Features statistics, charts, and data management.

🗄️ Database Schema
sql
CREATE TABLE Feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
    comments TEXT NOT NULL,
    date_submitted TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);
🧪 Testing the Application
Submit Sample Feedback
Navigate to http://localhost:5000

Fill out the form:

Name: John Doe

Email: john@example.com

Rating: 5 stars

Comments: "Great service! Very helpful."

Click "Submit Feedback"

Access Admin Dashboard
Navigate to http://localhost:5000/admin-dashboard

Login with credentials:

Username: admin

Password: admin123

View submitted feedback and statistics

Export Data
From the admin dashboard, click "Export CSV"

Open the downloaded file in Excel or any spreadsheet software

🤝 Contributing
Contributions are welcome! Here's how you can contribute:

Fork the repository

Create a feature branch

bash
git checkout -b feature/AmazingFeature
Commit your changes

bash
git commit -m 'Add some AmazingFeature'
Push to the branch

bash
git push origin feature/AmazingFeature
Open a Pull Request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Flask Documentation - For excellent framework documentation

Bootstrap - For responsive UI components

Chart.js - For beautiful data visualization

Font Awesome - For icons

Check the Issues page

Create a new issue if your problem isn't already listed

📈 Future Enhancements
Planned features for future versions:

Email notifications for new feedback

Advanced filtering and search in admin panel

User registration system

Feedback categories/tags

Sentiment analysis on comments

Monthly reports generation

Multi-language support

Docker containerization

🏆 Learning Outcomes
Technical Skills Developed
Full-stack web development with Flask

Database design and SQL operations

REST API development

Frontend-backend integration

Form handling and validation

Data visualization with Chart.js

User authentication and sessions

Project structure and organization

Industry-Relevant Skills
Connecting frontend and backend systems

Handling POST requests and form data

Implementing CRUD operations

Creating responsive user interfaces

Building real-world web applications

Version control with Git/GitHub

<div align="center">
Built with ❤️ for Educational Purposes
⭐ Star this repo if you found it helpful!

</div>
👨‍💻 Author
Your Name

Neha Choudhary
