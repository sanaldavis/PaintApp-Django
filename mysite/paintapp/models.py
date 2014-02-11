from django.db import models

# Create your models here.

#create database table fields use below command

class pic_store(models.Model):
	name=models.CharField(max_length=60)
	data=models.CharField(max_length=10000000)
