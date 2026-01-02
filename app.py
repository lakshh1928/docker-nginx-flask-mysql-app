import time
import os
from flask import Flask, request, jsonify, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# --- Database Configuration (Loaded from .env) ---
# We use os.getenv('KEY', 'default_value')
# The defaults act as a fallback if the .env file is missing
db_config = {
    'host': os.getenv('MYSQL_HOST', 'db'),
    'user': os.getenv('MYSQL_USER', 'root'),
    'password': os.getenv('MYSQL_PASSWORD'),  # No default password for security
    'database': os.getenv('MYSQL_DB', 'list_app')
}

def get_db_connection():
    """
    Retry logic: Loops 5 times to wait for the MySQL container 
    to fully initialize before giving up.
    """
    retries = 5
    while retries > 0:
        try:
            print(f"Connecting to database at {db_config['host']}...")
            conn = mysql.connector.connect(**db_config)
            print("✅ Database connected successfully!")
            return conn
        except Error as e:
            print(f"⏳ Database not ready yet... Error: {e}")
            retries -= 1
            time.sleep(5) # Wait 5 seconds before trying again
    
    print("❌ Could not connect to database after 5 retries.")
    return None

# --- Routes ---

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tasks ORDER BY id DESC")
        tasks = cursor.fetchall()
        return jsonify(tasks)
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

@app.route('/add', methods=['POST'])
def add_task():
    data = request.json
    task_content = data.get('content')
    
    if task_content:
        conn = get_db_connection()
        if conn is None:
            return jsonify({"error": "Database connection failed"}), 500

        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tasks (content) VALUES (%s)", (task_content,))
            conn.commit()
            return jsonify({"message": "Task added!"}), 201
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
                
    return jsonify({"error": "Empty task"}), 400

if __name__ == '__main__':
    # host='0.0.0.0' is required for the container to accept external traffic
    app.run(host='0.0.0.0', port=5000)
