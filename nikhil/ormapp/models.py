from django.db import models
from django.contrib import admin
class Student(models.Model):
	Name=models.CharField(max_length=10)
	Refno=models.IntegerField(primary_key="Refno")
	Percentage=models.FloatField()
	DoB=models.DateField()
	Email=models.EmailField()
class StudentAdmin(admin.ModelAdmin):
	list_display=('Name','Refno','Percentage','DoB','Email')