from django.db import models

# Create your models here.


class RegistredUser(models.Model):
    # a registred user
    username = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=150)
    email = models.EmailField()

    
class Contact(models.Model):
    # The person using the contact form isn't necessarily a registred user...
    name = models.CharField(max_length=150)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.name + " (" + self.email + "), " + self.text 