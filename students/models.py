from django.db import models
from django.utils.text import slugify
# Create your models here.



class Parent(models.Model):
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    father_mobile = models.CharField(max_length=20)
    father_email = models.EmailField(max_length=150)
    mother_name = models.CharField(max_length=100)
    mother_mobile = models.CharField(max_length=20)
    mother_email = models.EmailField(max_length=150)
    present_address = models.TextField(max_length=100)
    permanent_address = models.TextField(max_length=100)


    def __str__(self):
        return f"{self.father_name} & {self.mother_name}"
    

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    date_of_birth = models.DateField()
    student_class = models.CharField(max_length=100)
    joining_date = models.DateField()
    email = models.EmailField(max_length=150)
    mobile_number = models.CharField(max_length=20)
    fillier = models.CharField(max_length=100)
    student_image = models.ImageField(upload_to='student_images/', null=True, blank=True)
    parent = models.OneToOneField(Parent, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    
    def save (self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}-{self.last_name}-{self.student_id}")
            super(Student,self).save(*args, **kwargs)


    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"