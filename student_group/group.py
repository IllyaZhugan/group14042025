from student_group.exceptions import GroupFullException
from student import Student


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Можна додавати лише студентів")
        if len(self.group) >= 10:
            raise GroupFullException()
        if student in self.group:
            print(
                f"Студент з номером залікової книжки {student.record_book} вже є у групі."
            )
        else:
            self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = "\n".join(
            str(student) for student in sorted(self.group, key=lambda s: s.last_name)
        )
        return f"Number: {self.number}\n{all_students}"
