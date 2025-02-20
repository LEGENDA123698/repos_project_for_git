import django_settings
from myapp.models import Subject, Teacher, Class, Schedule, Grade, Student

while True:
    choices = int(input('''оберіть дію: 1.Додавання предмету:
             2.Додавання вчителя:
             3.Додавання класу:
             4.Додавання учня: '''))
    if choices == 1:
        title = input("Назва: ")
        description = input("опис: ")
        name_teacher = input("ім'я вчителя: ")
        
        teacher = Teacher.objects.get(teacher_name = name_teacher)
        
        add_new_subject = Subject(name = title, description = description, teacher = teacher)
        add_new_subject.save()
    
    if choices == 2:
        name_teacher = input("ім'я вчителя: ")
        surname_teacher = input("Прізвище вчителя: ")
        subject_teacher = input("Предмет вчителя: ")
        
        add_new_teacher = Teacher(teacher_name = name_teacher, teacher_surname = surname_teacher, teacher_subject = subject_teacher)
        add_new_teacher.save()
        
    if choices == 3:
        class_name = input("назва классу: ")
        class_year = input("проміжок: ")
        
        add_new_class = Class(class_name = class_name, class_year = class_year)
        add_new_class.save()
    if choices == 4:
        student_name = input("ім'я: ")
        student_surname = input("Прізвище: ")
        student_class_name = input("назва классу: ")
        student_class_year = input("проміжок: ")
        
        classs = Class.objects.get(class_name = student_class_name, class_year = student_class_year)
        
        add_new_class = Student(student_name = student_name, student_surname = student_surname, student_class = classs)
        add_new_class.save()