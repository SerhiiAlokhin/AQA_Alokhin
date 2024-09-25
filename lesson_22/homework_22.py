import random

from sqlalchemy import Column, Integer, String, create_engine, Table, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

# Подключение к базе данных PostgreSQL
engine = create_engine('postgresql+psycopg2://sergey:qaz321wsx@localhost:5432/postgres')
Base = declarative_base()

try:
    # Проверим подключение
    connection = engine.connect()
    print("Connected successfully!")
finally:
    # Закрываем подключение
    connection.close()

# Закрываем подключение
connection.close()

enrollment_table = Table('enrollment', Base.metadata,
                         Column('student_id', Integer, ForeignKey('students.id')),
                         Column('course_id', Integer, ForeignKey('courses.id'))
                         )

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    courses = relationship('Course', secondary=enrollment_table, back_populates='students')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    students = relationship('Student', secondary=enrollment_table, back_populates='courses')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

courses_list = ['Math', 'History', 'Physics', 'Biology', 'Computer Science']
courses = [Course(title=title) for title in courses_list]
session.add_all(courses)
session.commit()

students_names = ['Anna', 'John', 'Alex', 'Maria', 'Olga', 'Ivan', 'Sergey', 'Dmitry', 'Elena', 'Nina',
                  'Igor', 'Vladimir', 'Ekaterina', 'Maxim', 'Nikolay', 'Oleg', 'Andrey', 'Tatyana', 'Mikhail', 'Sofia']
students = [Student(name=name, age=random.randint(18, 30)) for name in students_names]

session.add_all(students)
session.commit()

for student in students:
    student_courses = random.sample(courses, random.randint(1, 3))
    student.courses.extend(student_courses)
session.commit()
def add_student(name, age):
    new_student = Student(name=name, age=age)
    session.add(new_student)
    session.commit()
    print(f"Student {name} added successfully.")

def enroll_student_to_course(student_name, course_title):
    student = session.query(Student).filter_by(name=student_name).first()
    course = session.query(Course).filter_by(title=course_title).first()
    if student and course:
        student.courses.append(course)
        session.commit()
        print(f"Student {student_name} enrolled in {course_title}.")
    else:
        print("Student or course not found.")

def get_students_in_course(course_title):
    course = session.query(Course).filter_by(title = course_title).first()
    if course:
        print(f'Students in course {course_title}:')
        for student in course.students:
            print(student.name)
        else:
            print(f"Course {course_title} not found.")

def get_courses_for_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()
    if student:
        print(f'Courses for student {student_name}:')
        for course in student.courses:
            print(course.title)
    else:
        print(f"Student {student_name} not found.")

def update_student_name(old_name, new_name):
    student = session.query(Student).filter_by(name=old_name).first()
    if student:
        student.name = new_name
        session.commit()
        print(f"Student name updated from {old_name} to {new_name}.")
    else:
        print(f"Student {old_name} not found.")

def delete_student(name):
    student = session.query(Student).filter_by(name=name).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"Student {name} deleted from database.")
    else:
        print(f"Student {name} not found.")



add_student("Serhii", 28)
enroll_student_to_course("Serhii", "Math")
get_students_in_course("Math")
get_courses_for_student("Serhii")
update_student_name("Serhii", "Sergey")
delete_student("Serhii")
