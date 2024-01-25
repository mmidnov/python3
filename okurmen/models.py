# okurmen/models.py
from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    # subject = models.CharField(max_length=50,choices=[('Посмотреть Группы', 'Check Groups')])
    programming_type = models.CharField(max_length=50, choices=[
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('UX/UI', 'UX/UI'),
    ])

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=255)
    trainer = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    mentor = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=17)
    payment = models.IntegerField()
    payment_date = models.DateField(null=True, blank=True)
    manager = models.ForeignKey('Manager', on_delete=models.SET_NULL, null=True, blank=True)
    payment_receipt = models.ImageField(upload_to='payment_receipts/', null=True, blank=True)

class Manager(models.Model):
    name = models.CharField(max_length=255)
    responsibilities = models.TextField()
    directed_students_count = models.IntegerField()
    manager_number = models.CharField(max_length=17)    
    def __str__(self):
        return self.name
    
    
    
    
    

