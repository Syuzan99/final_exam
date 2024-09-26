from django.db import models


from django.db import models
from django.contrib.auth.models import User

class Specialist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='specialists/')
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)

    def __str__(self):
        return self.user.username

class Appointment(models.Model):
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()

    def __str__(self):
        return f'Appointment with {self.specialist.user.username} on {self.date_time}'