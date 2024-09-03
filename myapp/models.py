from django.db import models

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50)


class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="subjects")



class Class(models.Model):
    class_name = models.CharField(max_length=100)




class Student(models.Model):
    student_name = models.CharField(max_length=50)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="students")