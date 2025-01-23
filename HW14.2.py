class TooManyStudentsError(Exception):
    def __init__(self, message="Група не може містити більше 10 студентів"):
        self.message = message
        super().__init__(self.message)


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} років, {self.gender}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"Студент: {self.first_name} {self.last_name}, Залікова: {self.record_book}"

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise TooManyStudentsError()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f"Група: {self.number}\nСтуденти:\n{all_students}"


try:
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    gr = Group('GroupA')

    gr.add_student(st1)
    found_student = gr.find_student('Jobs')
    assert found_student == st1, f"Error: Expected {st1}, but got {found_student}"
    print("Тест на поиск студента пройден!")

    for i in range(9):  # Теперь добавляем только 9 студентов, чтобы вместе с `st1` их стало 10
        gr.add_student(Student('Male', 20 + i, f'Student{i}', f'LastName{i}', f'Book{i}'))
    print(gr)

    gr.add_student(st2)

except TooManyStudentsError as e:
    print(f"Ошибка: {e}")



