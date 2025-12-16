from flask import Flask, render_template, request, jsonify, redirect, url_for, session, make_response
import sqlite3
from datetime import datetime
import csv
import io
import hashlib

app = Flask(__name__)
app.secret_key = 'feedback-system-secret-key-2024'
app.config['DATABASE'] = 'database.db'

def init_db():
    """Initialize the database with required tables"""
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    
    # Create Feedback table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
            comments TEXT NOT NULL,
            date_submitted TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create Admin table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Admin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    
    # Insert default admin user if not exists
    cursor.execute("SELECT * FROM Admin WHERE username = 'admin'")
    if not cursor.fetchone():
        password_hash = hashlib.sha256('admin123'.encode()).hexdigest()
        cursor.execute("INSERT INTO Admin (username, password_hash) VALUES (?, ?)", 
                      ('admin', password_hash))
    
    conn.commit()
    conn.close()

def get_db_connection():
    """Get database connection"""
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

# Initialize database on startup
init_db()

@app.route('/')
def home():
    """Home page with feedback form"""
    return render_template('index.html')

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    """Handle feedback submission"""
    try:
        data = request.form
        
        # Validate required fields
        if not data.get('name') or not data.get('email') or not data.get('rating') or not data.get('comments'):
            return jsonify({'error': 'All fields are required'}), 400
        
        # Validate rating
        try:
            rating = int(data['rating'])
            if rating < 1 or rating > 5:
                return jsonify({'error': 'Rating must be between 1 and 5'}), 400
        except ValueError:
            return jsonify({'error': 'Invalid rating value'}), 400
        
        # Insert into database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Feedback (name, email, rating, comments)
            VALUES (?, ?, ?, ?)
        ''', (data['name'], data['email'], rating, data['comments']))
        conn.commit()
        feedback_id = cursor.lastrowid
        conn.close()
        
        return jsonify({
            'success': True,
            'message': 'Thank you for your feedback!',
            'id': feedback_id
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Admin login page"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Validate credentials
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT password_hash FROM Admin WHERE username = ?", (username,))
        admin = cursor.fetchone()
        conn.close()
        
        if admin and admin['password_hash'] == hashlib.sha256(password.encode()).hexdigest():
            session['admin_logged_in'] = True
            session['admin_username'] = username
            return redirect(url_for('admin_dashboard'))
        else:
            return render_template('admin.html', login_error='Invalid credentials')
    
    return redirect(url_for('admin_dashboard'))

@app.route('/admin-dashboard')
def admin_dashboard():
    """Admin dashboard page"""
    # Check if user is logged in
    if not session.get('admin_logged_in'):
        return render_template('admin.html', show_login=True)
    
    # Get all feedback
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Get feedback data
    cursor.execute("SELECT * FROM Feedback ORDER BY date_submitted DESC")
    feedback_list = [dict(row) for row in cursor.fetchall()]
    
    # Get statistics
    cursor.execute("SELECT COUNT(*) as total FROM Feedback")
    total_feedback = cursor.fetchone()['total']
    
    cursor.execute("SELECT AVG(rating) as avg_rating FROM Feedback")
    avg_rating = cursor.fetchone()['avg_rating']
    avg_rating = round(avg_rating, 2) if avg_rating else 0
    
    # Get rating distribution
    rating_dist = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    cursor.execute("SELECT rating, COUNT(*) as count FROM Feedback GROUP BY rating")
    for row in cursor.fetchall():
        rating_dist[row['rating']] = row['count']
    
    conn.close()
    
    return render_template('admin.html', 
                         feedback=feedback_list,
                         total_feedback=total_feedback,
                         avg_rating=avg_rating,
                         rating_dist=rating_dist,
                         show_login=False,
                         admin_username=session.get('admin_username'))

@app.route('/api/feedback')
def api_feedback():
    """API endpoint to get all feedback in JSON format"""
    if not session.get('admin_logged_in'):
        return jsonify({'error': 'Unauthorized'}), 401
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Feedback ORDER BY date_submitted DESC")
    feedback_list = [dict(row) for row in cursor.fetchall()]
    conn.close()
    
    return jsonify(feedback_list)

@app.route('/export-csv')
def export_csv():
    """Export feedback data as CSV"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_dashboard'))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Feedback ORDER BY date_submitted DESC")
    feedback_list = [dict(row) for row in cursor.fetchall()]
    conn.close()
    
    # Create CSV in memory
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Write header
    writer.writerow(['ID', 'Name', 'Email', 'Rating', 'Comments', 'Date Submitted'])
    
    # Write data
    for fb in feedback_list:
        writer.writerow([
            fb['id'],
            fb['name'],
            fb['email'],
            fb['rating'],
            fb['comments'],
            fb['date_submitted']
        ])
    
    output.seek(0)
    response = make_response(output.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=feedback_data.csv'
    response.headers['Content-type'] = 'text/csv'
    return response

@app.route('/logout')
def logout():
    """Logout admin user"""
    session.pop('admin_logged_in', None)
    session.pop('admin_username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)