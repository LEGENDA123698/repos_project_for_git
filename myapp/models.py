from django.db import models

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50)
    teacher_surname = models.CharField(max_length=50, null=True)
    teacher_subject = models.CharField(max_length=50, null=True)


class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="subjects")



class Class(models.Model):
    class_name = models.CharField(max_length=100)
    class_year = models.CharField(max_length=9, null=True)




class Student(models.Model):
    student_name = models.CharField(max_length=50)
    student_surname = models.CharField(max_length=50, null=True)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="students")
    
    
class Schedule(models.Model):
    schedule_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="schedules")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="schedules")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="schedules")
    day = models.CharField(max_length=100, null=True)
    time = models.DateTimeField(null=True)



class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="grades")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="grades")
    grade = models.IntegerField()
    time = models.DateTimeField(null=True)
