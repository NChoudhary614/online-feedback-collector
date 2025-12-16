# Online Feedback Collector with Admin Dashboard

A complete full-stack web application for collecting user feedback and displaying analytics in an admin dashboard.

## Features

### Frontend (User Interface)
- **Home Page** with project introduction
- **Feedback Form Page** with:
  - Name field (text input)
  - Email field (email validation)
  - Rating selection (1-5 stars)
  - Comments field (textarea)
- **AJAX form submission** without page reload
- **Form validation** with real-time feedback
- **Responsive design** using Bootstrap 5

### Backend (Python + Flask)
- **POST request handling** for feedback submission
- **SQLite database** for data storage
- **Admin dashboard** with authentication
- **REST API endpoint** (`/api/feedback`) for JSON data
- **CSV export** functionality
- **Jinja2 templates** for server-side rendering

### Database (SQLite)
- **Feedback table** with columns:
  - id (primary key)
  - name (user name)
  - email (user email)
  - rating (1-5)
  - comments (feedback text)
  - date_submitted (timestamp)

### Admin Dashboard Features
- **View all feedback entries** in a table
- **Count total feedback** submissions
- **Calculate average rating**
- **Show feedback trends** with Chart.js charts
- **Export data** to CSV format
- **Basic login system** for admin access

## Project Structure
