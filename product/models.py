from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import RegexValidator


# User = get_user_model()

class Brand(models.TextChoices):
    another = 'Another'
    toyota = 'Toyota'
    mercedes = 'Mercedes'
    bmw = 'BMW'
    audi = 'Audi'

class Color(models.TextChoices):
    another = 'Another'
    RED = 'R', 'Red'
    BLUE = 'B', 'Blue'
    GREEN = 'G', 'Green'
    YELLOW = 'Y', 'Yellow'
    BLACK = 'BK', 'Black'
    WHITE = 'WH', 'White'
    SILVER = 'SV', 'Silver'
    GRAY = 'GR', 'Gray'

def get_default_image():
    return '/home/user/StoreImages/images.png'


class StatusChoices(models.TextChoices):
    processing = "processing"
    published = "published"


class Car(models.Model):
    brand = models.CharField(max_length=100, choices=Brand.choices, default='Another')
    color = models.CharField(max_length=40, choices=Color.choices, default='Another')
    release = models.IntegerField(
        validators=[
            MaxValueValidator(2023, 'Date cannot be above 2023'), 
            MinValueValidator(1900, 'Date cannot be below 1900')
        ]
    )
    image = models.ImageField(upload_to='cars')
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default='processing')

    def __str__(self) -> str:
        return self.brand + ' ' + str(self.release) + ' year'
    
    