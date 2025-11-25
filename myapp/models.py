from django.db import models

class UserRegistration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=100) # In real apps, hash this!
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email