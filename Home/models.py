from django.db import models

# Create your models here.
class Contact (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):   # This method returns the string representation of the model instance.(basically the name of the contact object)
        return self.name