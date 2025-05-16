from db import get_connection

def check_exists(table, id):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"SELECT 1 FROM {table} WHERE id = %s"
    cursor.execute(query, (id,))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists

def add_student(name, email, department, batch):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Student (name, email, department, batch)
        VALUES (%s, %s, %s, %s)
    """, (name, email, department, batch))
    conn.commit()
    conn.close()

def add_subject(name, credits, department):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Subject (name, credits, department)
        VALUES (%s, %s, %s)
    """, (name, credits, department))
    conn.commit()
    conn.close()

def add_semester(student_id, semester_number, year):
    if not check_exists('Student', student_id):
        raise ValueError(f"Student ID {student_id} does not exist.")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Semester (student_id, semester_number, year)
        VALUES (%s, %s, %s)
    """, (student_id, semester_number, year))
    conn.commit()
    conn.close()

def add_marks(student_id, subject_id, semester_id, marks_obtained, max_marks):
    # Validate foreign keys before insert
    if not check_exists('Student', student_id):
        raise ValueError(f"Student ID {student_id} does not exist.")
    if not check_exists('Subject', subject_id):
        raise ValueError(f"Subject ID {subject_id} does not exist.")
    if not check_exists('Semester', semester_id):
        raise ValueError(f"Semester ID {semester_id} does not exist.")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Mark (student_id, subject_id, semester_id, marks_obtained, max_marks)
        VALUES (%s, %s, %s, %s, %s)
    """, (student_id, subject_id, semester_id, marks_obtained, max_marks))
    conn.commit()
    conn.close()

def get_transcript(student_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT m.marks_obtained, m.max_marks, sub.credits, sub.name AS subject_name
        FROM Mark m
        JOIN Subject sub ON m.subject_id = sub.id
        WHERE m.student_id = %s
    """, (student_id,))

    rows = cursor.fetchall()
    if not rows:
        conn.close()
        return "No records found for this student."

    total_weighted_score = 0
    total_credits = 0
    report_lines = []

    for r in rows:
        percentage = (r['marks_obtained'] / r['max_marks']) * 100 if r['max_marks'] else 0
        if percentage >= 90:
            grade = 'A'
            points = 4.0
        elif percentage >= 80:
            grade = 'B'
            points = 3.0
        elif percentage >= 70:
            grade = 'C'
            points = 2.0
        elif percentage >= 60:
            grade = 'D'
            points = 1.0
        else:
            grade = 'F'
            points = 0.0

        weighted_points = points * r['credits']
        total_weighted_score += weighted_points
        total_credits += r['credits']

        report_lines.append(
            f"Subject: {r['subject_name']}, Marks: {r['marks_obtained']}/{r['max_marks']}, Grade: {grade}"
        )

    cgpa = round(total_weighted_score / total_credits, 2) if total_credits else 0.0

    report = f"CGPA: {cgpa}\n" + "\n".join(report_lines)
    conn.close()
    return report

def get_top_performers(department, semester_number, top_n):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT st.id, st.name, SUM((m.marks_obtained/m.max_marks) * sub.credits) AS total_weighted_score
        FROM Mark m
        JOIN Semester sem ON m.semester_id = sem.id
        JOIN Student st ON m.student_id = st.id
        JOIN Subject sub ON m.subject_id = sub.id
        WHERE st.department = %s AND sem.semester_number = %s
        GROUP BY st.id
        ORDER BY total_weighted_score DESC
        LIMIT %s
    """, (department, semester_number, top_n))

    rows = cursor.fetchall()
    if not rows:
        conn.close()
        return "No performers found."

    result_lines = [
        f"{i+1}. {row['name']} - Score: {round(row['total_weighted_score'], 2)}"
        for i, row in enumerate(rows)
    ]
    conn.close()
    return "\n".join(result_lines)

def get_subject_rankings(subject_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT st.id, st.name, m.marks_obtained, m.max_marks,
               (m.marks_obtained/m.max_marks)*100 AS percentage
        FROM Mark m
        JOIN Student st ON m.student_id = st.id
        WHERE m.subject_id = %s
        ORDER BY percentage DESC
    """, (subject_id,))

    rows = cursor.fetchall()
    if not rows:
        conn.close()
        return "No rankings available."

    result_lines = []
    rank = 1
    for row in rows:
        result_lines.append(
            f"{rank}. {row['name']} - {round(row['percentage'], 2)}% ({row['marks_obtained']}/{row['max_marks']})"
        )
        rank += 1

    conn.close()
    return "\n".join(result_lines)
