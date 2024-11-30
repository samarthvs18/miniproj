from gui import Application
from models import GradeSystem
from persistence import load_from_file, save_to_file

def main():
    grade_system = GradeSystem()
    load_from_file(grade_system)

    app = Application(grade_system)
    app.mainloop()

    save_to_file(grade_system)

if __name__ == "__main__":
    main()