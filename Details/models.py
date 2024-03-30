from django.db import models
from Review.models import Review
# Create your models here.
class Detail(models.Model):
    hotel_name = models.CharField(max_length=30)
    address = models.CharField(max_length = 50)
    review = models.OneToOneField(Review, on_delete = models.CASCADE)
    photo = models.ImageField(upload_to='Details/images/')
    
    def __str__(self):
        return f"{self.hotel_name}"
    