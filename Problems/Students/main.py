class Student:

    def __init__(self, name: str, last_name: str, birth_year: int) -> None:
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the student_id here
        self.student_id = name[0] + last_name + str(birth_year)


student_name = input().strip()
student_last_name = input().strip()
student_birth_year = int(input().strip())

john = Student(student_name, student_last_name, student_birth_year)

print(john.student_id)
