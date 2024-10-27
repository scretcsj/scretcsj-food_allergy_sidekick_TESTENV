from django.contrib.auth.models import User
from django.db import models
from multiselectfield import MultiSelectField

class UserProfile(models.Model):
    ALLERGY_CHOICES = (
        ('peanuts', 'Peanuts'),
        ('treenuts', 'Tree Nuts'),
        ('dairy', 'Dairy'),
        ('egg', 'Egg'),
        ('soy', 'Soy'),
        ('wheat', 'Wheat'),
        ('fish', 'Fish'),
        ('crustaceans_shellfish', 'Crustaceans/Shellfish'),
        ('sesame', 'Sesame'),
        ('mustard', 'Mustard'),
        ('celery', 'Celery'),
        ('molluscs', 'Molluscs'),
        ('meat', 'Meat'),
        ('gluten', 'Gluten'),
        ('fruit', 'Fruit'),
        ('vegetables', 'Vegetables'),

    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    allergies = MultiSelectField(choices=ALLERGY_CHOICES, blank=True)
    image = models.ImageField(upload_to='profile_images/', default='profile_images/default_profile_pic.jpg')
    
    def __str__(self):
        return self.user.username
