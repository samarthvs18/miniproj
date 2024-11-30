class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}  

    def add_grade(self, course, grade):
        """Add or update the grade for a specific course."""
        self.grades[course] = grade

    def get_average(self):
        """Calculate and return the average grade."""
        if len(self.grades) == 0:
            return 0  
        total = sum(self.grades.values())  
        return total / len(self.grades)  

    def get_letter_grade(self):
        """Return the letter grade based on the average grade."""
        average = self.get_average()  
        if average >= 95:
            return 'A+'
        elif average >= 90:
            return 'A'
        elif average >= 85:
            return 'B+'
        elif average >= 80:
            return 'B'
        elif average >= 75:
            return 'C+'
        elif average >= 60:
            return 'C'
        else:
            return 'F'

class GradeSystem:
    def __init__(self):
        self.students = {} 

    def add_student(self, student):
        """Add a student to the system."""
        self.students[student.student_id] = student

    def get_student(self, student_id):
        """Retrieve a student by their student ID."""
        return self.students.get(student_id)

    def get_all_students(self):
        """Return all students in the system."""
        return self.students
