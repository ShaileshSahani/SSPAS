# import tkinter as tk
# from db import create_database_and_tables
# from functions import add_student, add_subject, add_semester, add_marks, get_transcript, get_top_performers, get_subject_rankings
#
# # Main App Window
# app = tk.Tk()
# app.title("SSPAS - Student Performance System")
# app.geometry("400x600")
# create_database_and_tables()
#
# # ---- Frame Functions ----
# def open_add_student():
#     window = tk.Toplevel(app)
#     window.title("Add Student")
#
#     tk.Label(window, text="Name").pack()
#     name = tk.Entry(window)
#     name.pack()
#
#     tk.Label(window, text="Email").pack()
#     email = tk.Entry(window)
#     email.pack()
#
#     tk.Label(window, text="Department").pack()
#     dept = tk.Entry(window)
#     dept.pack()
#
#     tk.Label(window, text="Batch").pack()
#     batch = tk.Entry(window)
#     batch.pack()
#
#     def submit():
#         add_student(name.get(), email.get(), dept.get(), int(batch.get()))
#         tk.Label(window, text="Student added!", fg="green").pack()
#
#     tk.Button(window, text="Submit", command=submit).pack()
#
# def open_add_subject():
#     window = tk.Toplevel(app)
#     window.title("Add Subject")
#
#     tk.Label(window, text="Name").pack()
#     name = tk.Entry(window)
#     name.pack()
#
#     tk.Label(window, text="Credits").pack()
#     credits = tk.Entry(window)
#     credits.pack()
#
#     tk.Label(window, text="Department").pack()
#     dept = tk.Entry(window)
#     dept.pack()
#
#     def submit():
#         add_subject(name.get(), int(credits.get()), dept.get())
#         tk.Label(window, text="Subject added!", fg="green").pack()
#
#     tk.Button(window, text="Submit", command=submit).pack()
#
# def open_add_semester():
#     window = tk.Toplevel(app)
#     window.title("Add Semester")
#
#     tk.Label(window, text="Student ID").pack()
#     student_id = tk.Entry(window)
#     student_id.pack()
#
#     tk.Label(window, text="Semester Number").pack()
#     sem_num = tk.Entry(window)
#     sem_num.pack()
#
#     tk.Label(window, text="Year").pack()
#     year = tk.Entry(window)
#     year.pack()
#
#     def submit():
#         add_semester(int(student_id.get()), int(sem_num.get()), int(year.get()))
#         tk.Label(window, text="Semester added!", fg="green").pack()
#
#     tk.Button(window, text="Submit", command=submit).pack()
#
# def open_add_marks():
#     window = tk.Toplevel(app)
#     window.title("Add Marks")
#
#     tk.Label(window, text="Student ID").pack()
#     student_id = tk.Entry(window)
#     student_id.pack()
#
#     tk.Label(window, text="Subject ID").pack()
#     subject_id = tk.Entry(window)
#     subject_id.pack()
#
#     tk.Label(window, text="Semester ID").pack()
#     semester_id = tk.Entry(window)
#     semester_id.pack()
#
#     tk.Label(window, text="Marks Obtained").pack()
#     marks = tk.Entry(window)
#     marks.pack()
#
#     tk.Label(window, text="Max Marks").pack()
#     max_marks = tk.Entry(window)
#     max_marks.pack()
#
#     def submit():
#         add_marks(int(student_id.get()), int(subject_id.get()), int(semester_id.get()), float(marks.get()), float(max_marks.get()))
#         tk.Label(window, text="Marks added!", fg="green").pack()
#
#     tk.Button(window, text="Submit", command=submit).pack()
#
# def open_transcript():
#     window = tk.Toplevel(app)
#     window.title("Transcript")
#
#     tk.Label(window, text="Student ID").pack()
#     student_id = tk.Entry(window)
#     student_id.pack()
#
#     def submit():
#         report = get_transcript(int(student_id.get()))
#         tk.Label(window, text=report, justify=tk.LEFT, wraplength=350).pack()
#
#     tk.Button(window, text="Get Transcript", command=submit).pack()
#
# def open_top_performers():
#     window = tk.Toplevel(app)
#     window.title("Top Performers")
#
#     tk.Label(window, text="Department").pack()
#     dept = tk.Entry(window)
#     dept.pack()
#
#     tk.Label(window, text="Semester Number").pack()
#     sem = tk.Entry(window)
#     sem.pack()
#
#     tk.Label(window, text="Top N Students").pack()
#     n = tk.Entry(window)
#     n.pack()
#
#     def submit():
#         results = get_top_performers(dept.get(), int(sem.get()), int(n.get()))
#         tk.Label(window, text=results, justify=tk.LEFT, wraplength=350).pack()
#
#     tk.Button(window, text="Show Top Performers", command=submit).pack()
#
# def open_subject_ranking():
#     window = tk.Toplevel(app)
#     window.title("Subject Rankings")
#
#     tk.Label(window, text="Subject ID").pack()
#     subject_id = tk.Entry(window)
#     subject_id.pack()
#
#     def submit():
#         results = get_subject_rankings(int(subject_id.get()))
#         tk.Label(window, text=results, justify=tk.LEFT, wraplength=350).pack()
#
#     tk.Button(window, text="Show Rankings", command=submit).pack()
#
# # ---- Main Menu ----
# tk.Label(app, text="SSPAS Dashboard", font=("Arial", 16)).pack(pady=10)
#
# tk.Button(app, text="Add Student", width=30, command=open_add_student).pack(pady=5)
# tk.Button(app, text="Add Subject", width=30, command=open_add_subject).pack(pady=5)
# tk.Button(app, text="Add Semester", width=30, command=open_add_semester).pack(pady=5)
# tk.Button(app, text="Add Marks", width=30, command=open_add_marks).pack(pady=5)
# tk.Button(app, text="View Transcript", width=30, command=open_transcript).pack(pady=5)
# tk.Button(app, text="Top Performers", width=30, command=open_top_performers).pack(pady=5)
# tk.Button(app, text="Subject Rankings", width=30, command=open_subject_ranking).pack(pady=5)
#
# app.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox
from functions import add_student, add_subject, add_semester, add_marks, get_transcript, get_top_performers, get_subject_rankings

# ---- Role Flags ----
is_staff = False

# ---- Login Window ----
def login():
    def verify():
        global is_staff
        username = user_entry.get()
        password = pass_entry.get()

        if username == "st" and password == "1111":
            is_staff = True
            login_win.destroy()
            main_menu()
        elif username == "sd" and password == "0000":
            is_staff = False
            login_win.destroy()
            main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    login_win = tk.Tk()
    login_win.title("Login")
    login_win.geometry("300x200")

    tk.Label(login_win, text="Username").pack(pady=5)
    user_entry = tk.Entry(login_win)
    user_entry.pack(pady=5)

    tk.Label(login_win, text="Password").pack(pady=5)
    pass_entry = tk.Entry(login_win, show='*')
    pass_entry.pack(pady=5)

    tk.Button(login_win, text="Login", command=verify).pack(pady=20)
    login_win.mainloop()

# ---- Feature Windows ----
def open_add_student():
    if not is_staff:
        messagebox.showwarning("Access Denied", "Students cannot add students.")
        return
    window = tk.Toplevel()
    window.title("Add Student")

    tk.Label(window, text="Name").pack()
    name = tk.Entry(window)
    name.pack()

    tk.Label(window, text="Email").pack()
    email = tk.Entry(window)
    email.pack()

    tk.Label(window, text="Department").pack()
    dept = tk.Entry(window)
    dept.pack()

    tk.Label(window, text="Batch").pack()
    batch = tk.Entry(window)
    batch.pack()

    def submit():
        add_student(name.get(), email.get(), dept.get(), int(batch.get()))
        tk.Label(window, text="Student added!", fg="green").pack()

    tk.Button(window, text="Submit", command=submit).pack()

def open_add_subject():
    if not is_staff:
        messagebox.showwarning("Access Denied", "Students cannot add subjects.")
        return
    window = tk.Toplevel()
    window.title("Add Subject")

    tk.Label(window, text="Name").pack()
    name = tk.Entry(window)
    name.pack()

    tk.Label(window, text="Credits").pack()
    credits = tk.Entry(window)
    credits.pack()

    tk.Label(window, text="Department").pack()
    dept = tk.Entry(window)
    dept.pack()

    def submit():
        add_subject(name.get(), int(credits.get()), dept.get())
        tk.Label(window, text="Subject added!", fg="green").pack()

    tk.Button(window, text="Submit", command=submit).pack()

def open_add_semester():
    if not is_staff:
        messagebox.showwarning("Access Denied", "Students cannot add semesters.")
        return
    window = tk.Toplevel()
    window.title("Add Semester")

    tk.Label(window, text="Student ID").pack()
    student_id = tk.Entry(window)
    student_id.pack()

    tk.Label(window, text="Semester Number").pack()
    sem_num = tk.Entry(window)
    sem_num.pack()

    tk.Label(window, text="Year").pack()
    year = tk.Entry(window)
    year.pack()

    def submit():
        add_semester(int(student_id.get()), int(sem_num.get()), int(year.get()))
        tk.Label(window, text="Semester added!", fg="green").pack()

    tk.Button(window, text="Submit", command=submit).pack()

def open_add_marks():
    if not is_staff:
        messagebox.showwarning("Access Denied", "Students cannot add marks.")
        return
    window = tk.Toplevel()
    window.title("Add Marks")

    tk.Label(window, text="Student ID").pack()
    student_id = tk.Entry(window)
    student_id.pack()

    tk.Label(window, text="Subject ID").pack()
    subject_id = tk.Entry(window)
    subject_id.pack()

    tk.Label(window, text="Semester ID").pack()
    semester_id = tk.Entry(window)
    semester_id.pack()

    tk.Label(window, text="Marks Obtained").pack()
    marks = tk.Entry(window)
    marks.pack()

    tk.Label(window, text="Max Marks").pack()
    max_marks = tk.Entry(window)
    max_marks.pack()

    def submit():
        add_marks(int(student_id.get()), int(subject_id.get()), int(semester_id.get()), float(marks.get()), float(max_marks.get()))
        tk.Label(window, text="Marks added!", fg="green").pack()

    tk.Button(window, text="Submit", command=submit).pack()

def open_transcript():
    window = tk.Toplevel()
    window.title("Transcript")

    tk.Label(window, text="Student ID").pack()
    student_id = tk.Entry(window)
    student_id.pack()

    def submit():
        report = get_transcript(int(student_id.get()))
        tk.Label(window, text=report, justify=tk.LEFT, wraplength=350).pack()

    tk.Button(window, text="Get Transcript", command=submit).pack()

def open_top_performers():
    window = tk.Toplevel()
    window.title("Top Performers")

    tk.Label(window, text="Department").pack()
    dept = tk.Entry(window)
    dept.pack()

    tk.Label(window, text="Semester Number").pack()
    sem = tk.Entry(window)
    sem.pack()

    tk.Label(window, text="Top N Students").pack()
    n = tk.Entry(window)
    n.pack()

    def submit():
        results = get_top_performers(dept.get(), int(sem.get()), int(n.get()))
        tk.Label(window, text=results, justify=tk.LEFT, wraplength=350).pack()

    tk.Button(window, text="Show Top Performers", command=submit).pack()

def open_subject_ranking():
    window = tk.Toplevel()
    window.title("Subject Rankings")

    tk.Label(window, text="Subject ID").pack()
    subject_id = tk.Entry(window)
    subject_id.pack()

    def submit():
        results = get_subject_rankings(int(subject_id.get()))
        tk.Label(window, text=results, justify=tk.LEFT, wraplength=350).pack()

    tk.Button(window, text="Show Rankings", command=submit).pack()

# ---- Main Menu ----
def main_menu():
    app = tk.Tk()
    app.title("SSPAS Dashboard")
    app.geometry("400x600")

    tk.Label(app, text="SSPAS Dashboard", font=("Arial", 16)).pack(pady=10)

    if is_staff:
        tk.Button(app, text="Add Student", width=30, command=open_add_student).pack(pady=5)
        tk.Button(app, text="Add Subject", width=30, command=open_add_subject).pack(pady=5)
        tk.Button(app, text="Add Semester", width=30, command=open_add_semester).pack(pady=5)
        tk.Button(app, text="Add Marks", width=30, command=open_add_marks).pack(pady=5)

    tk.Button(app, text="View Transcript", width=30, command=open_transcript).pack(pady=5)
    tk.Button(app, text="Top Performers", width=30, command=open_top_performers).pack(pady=5)
    tk.Button(app, text="Subject Rankings", width=30, command=open_subject_ranking).pack(pady=5)

    app.mainloop()

# ---- Launch Login ----
login()