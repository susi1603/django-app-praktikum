from django.db import models
from django.contrib.auth.models import User
from mysite.mysite.settings import DATABASES

# model for database
# includes the user which when registered from the register.html should not have credentials to write on the database
# the title of the job, its job description, a job link, 
# an interview field to mark whether the applicant has been invited to an interview or no
# a calendar to book an interview and add to Google Calendar, which is to be implemented
# whether the applicant has or has not been rejected from the position. 
# created is the field to keep track of when the user was created.


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name='Job title')
    jobdescription = models.TextField(null=True, blank=True, verbose_name='Position Description')
    joblink =  models.CharField(max_length=200, verbose_name='Job Link')
    interview = models.BooleanField(default=False, verbose_name='Interview')
    rejected = models.BooleanField(default=False, verbose_name='Rejected')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'

