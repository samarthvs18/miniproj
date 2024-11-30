import json
from models import Student

def save_to_file(grade_system, filename="students.json"):
    """Save student data to a file"""
    with open(filename, 'w') as file:
        data = {student_id: student.__dict__ for student_id, student in grade_system.students.items()}
        json.dump(data, file)


def load_from_file(grade_system, filename="students.json"):
    """Load student data from a file"""
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            for student_id, student_data in data.items():
                student = Student(student_data['student_id'], student_data['name'])
                student.grades = student_data['grades']
                grade_system.students[student_id] = student
    except FileNotFoundError:
        print("File not found, starting with empty data.")