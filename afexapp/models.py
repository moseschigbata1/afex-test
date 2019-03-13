from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
APPROVED = 'A'
PENDING = 'P'
status = ((APPROVED, 'approved'),
           (PENDING, 'pending') 
)

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=30, blank=True)
    status = models.CharField(max_length=10, choices=status, default=PENDING)

    def __str__(self):
        return self.user.username

class Tasks(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    #goal_status = models.ForeignKey(GoalStatus, on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    date = models.DateField(default=datetime.date.today, null=True)



    def __str__(self):
        return self.task        

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)