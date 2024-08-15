class Student:
    def __init__(self, name, last_name, age, aver_points):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.aver_points = aver_points

    def change_aver_points(self, new_aver_points):
        self.aver_points = new_aver_points
        print(f'New average points is {self.aver_points}')

    def student_info(self):
        print(f'{self.name} {self.last_name}, {self.age}, Average points = {self.aver_points}')


student_1 = Student('Serhii', 'Alokhin', 27, 99)


student_1.student_info()
student_1.change_aver_points(100)
student_1.student_info()