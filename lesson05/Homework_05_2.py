# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

'''Task_01'''
print('Would you like input your data (yes/no)')
c = input()
if c == 'yes':
  print('Name:');  Name = input()
  print('Surname:'); Surname = input()
  print('Age:'); Age = input()
  print('Role:') ; Role = input()
  print('City:'); City = input()
  new_person_1 = [(Name,Surname,Age,Role,City)]
else:
  new_person_1 = [('Serhii', 'Alokhin', 27, 'General QA','Kharkiv')]
print(new_person_1)
new_person_1.extend(people_records)

'''Task_02'''
people_records = new_person_1
switch_person = people_records[1]
people_records[1] = people_records [5]
people_records[5] = switch_person
print('=='*40)
for i in people_records:
    print(f" {i[0]} {i[1]}, Age: {i[2]}, Role: {i[3]}, City: {i[4]}")
print('=='*40)
'''Task_03'''

check_index = [6,10,13]

for i in check_index:
  if people_records[i][2] > 30:
    print(f'{people_records[i][0]} {people_records[i][1]} старше 30')
  else:
    print(f'{people_records[i][0]} {people_records[i][1]} молодше 30')



