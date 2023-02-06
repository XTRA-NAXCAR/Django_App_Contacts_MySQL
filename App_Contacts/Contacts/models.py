from django.db import models

# Create your models here.
class User (models.Model):
    id = models.AutoField(primary_key=True)
    Users = models.CharField(max_length=100, verbose_name='User')
    Passwords = models.CharField(max_length=100, verbose_name='Password')
    def __str__(self):
        return self.Users
    
class Contact (models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200, verbose_name='Name')
    Number = models.BigIntegerField()
    Email = models.CharField(max_length=500, verbose_name='Email')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
