from django.db import models

# Create your models here.
class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    HotelCode = models.CharField(max_length=10)
    State = models.CharField(max_length=11)
    Cost = models.IntegerField(default=1000)
    Rating = models.FloatField(default=5)

    def __str__(self):
        return self.HotelCode + " from " + self.State
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)