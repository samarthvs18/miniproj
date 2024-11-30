import tkinter as tk
from tkinter import messagebox
from models import GradeSystem, Student
from persistence import save_to_file, load_from_file

class Application(tk.Tk):
    def __init__(self, grade_system):
        super().__init__()
        self.grade_system = grade_system
        self.title("Student Grading System")
        self.geometry("400x300")

        self.student_name_label = tk.Label(self, text="Student Name:")
        self.student_name_label.pack()
        self.student_name_entry = tk.Entry(self)
        self.student_name_entry.pack()

        self.student_id_label = tk.Label(self, text="Student ID:")
        self.student_id_label.pack()
        self.student_id_entry = tk.Entry(self)
        self.student_id_entry.pack()

        self.course_label = tk.Label(self, text="Course Name:")
        self.course_label.pack()
        self.course_entry = tk.Entry(self)
        self.course_entry.pack()

        self.grade_label = tk.Label(self, text="Grade:")
        self.grade_label.pack()
        self.grade_entry = tk.Entry(self)
        self.grade_entry.pack()

        self.add_student_button = tk.Button(self, text="Add Student", command=self.add_student)
        self.add_student_button.pack()

        self.add_grade_button = tk.Button(self, text="Add Grade", command=self.add_grade)
        self.add_grade_button.pack()

        self.show_all_button = tk.Button(self, text="Show All Students", command=self.show_all_students)
        self.show_all_button.pack()

        self.reset_button = tk.Button(self, text="Reset", command=self.reset_fields)
        self.reset_button.pack()

    def add_student(self):
        name = self.student_name_entry.get()
        student_id = self.student_id_entry.get()

        if name and student_id:
            student = Student(student_id, name)
            self.grade_system.add_student(student)
            messagebox.showinfo("Success", f"Student {name} added.")
        else:
            messagebox.showerror("Error", "Please enter both name and ID.")

    def add_grade(self):
        student_id = self.student_id_entry.get()
        course = self.course_entry.get()
        grade = self.grade_entry.get()

        if student_id and course and grade:
            student = self.grade_system.get_student(student_id)
            if student:
                student.add_grade(course, float(grade))
                messagebox.showinfo("Success", f"Grade for {course} added.")
            else:
                messagebox.showerror("Error", "Student not found.")
        else:
            messagebox.showerror("Error", "Please fill out all fields.")

    def show_all_students(self):
        students_info = ""
        for student in self.grade_system.students.values():
            students_info += f"{student.name} (ID: {student.student_id}) - Average: {student.get_average()} - Grade: {student.get_letter_grade()}\n"

        if students_info:
            messagebox.showinfo("All Students", students_info)
        else:
            messagebox.showinfo("No Students", "No students in the system yet.")

    
    def reset_fields(self):
        """Resets all input fields."""
        self.student_name_entry.delete(0, tk.END)
        self.student_id_entry.delete(0, tk.END)
        self.course_entry.delete(0, tk.END)
        self.grade_entry.delete(0, tk.END)
