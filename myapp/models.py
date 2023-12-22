from django.db import models

# Create your models here.

class student(models.Model): #class name later becomes the table name in the database.appname_class-name
    
     name = models.CharField(max_length=20)
     age = models.IntegerField()
     address = models.CharField(max_length=30)
     email = models.EmailField(max_length=20)




     # student.objects.create(name="john")
     # #INSERT INTO student (NAME,EMAIL) VALUES ("fnd",)

     # student.objects.all()
     # #select * from student