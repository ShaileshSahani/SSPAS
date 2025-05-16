import mysql.connector

def get_connection():
    # This will be imported and used by your functions.py for queries
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root@123",
        database="sspas_db"  # Assumes the DB exists
    )

def create_database_and_tables():
    # Run this once to create DB and tables
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root@123"
    )
    cursor = con.cursor()

    # Create database if not exists
    cursor.execute("CREATE DATABASE IF NOT EXISTS sspas_db")
    cursor.execute("USE sspas_db")

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Student (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        department VARCHAR(50),
        batch INT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subject (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        credits INT,
        department VARCHAR(50)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Semester (
        id INT AUTO_INCREMENT PRIMARY KEY,
        student_id INT,
        semester_number INT,
        year INT,
        FOREIGN KEY (student_id) REFERENCES Student(id) ON DELETE CASCADE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Mark (
        id INT AUTO_INCREMENT PRIMARY KEY,
        student_id INT,
        subject_id INT,
        semester_id INT,
        marks_obtained FLOAT,
        max_marks FLOAT,
        FOREIGN KEY (student_id) REFERENCES Student(id) ON DELETE CASCADE,
        FOREIGN KEY (subject_id) REFERENCES Subject(id),
        FOREIGN KEY (semester_id) REFERENCES Semester(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS GradePrediction (
        student_id INT,
        subject_id INT,
        predicted_score FLOAT,
        confidence_score FLOAT,
        PRIMARY KEY (student_id, subject_id),
        FOREIGN KEY (student_id) REFERENCES Student(id) ON DELETE CASCADE,
        FOREIGN KEY (subject_id) REFERENCES Subject(id)
    )
    """)

    con.commit()
    con.close()
    print("✅ Database and tables created successfully.")

