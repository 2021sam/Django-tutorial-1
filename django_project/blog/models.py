from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


class Post(models.Model):
    title = models.CharField(max_length=120)
    company = models.CharField(max_length=50, blank=True)
    company_manager = models.CharField(max_length=50, blank=True)
    manager_email = models.CharField(max_length=30, blank=True)

    recruiter = models.CharField(max_length=50, blank=True)
    recruiter_email = models.CharField(max_length=50, blank=True)
    recruiter_phone = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    date_start = models.DateField(default=datetime.date.today)
    date_end = models.DateField(default=datetime.date.today)
    # duration = models.IntegerField(default=0)
    duration = models.DurationField(default=datetime.timedelta(seconds=0))
    hourly_pay_rate = models.FloatField(default=0)
    payment_form = models.CharField(max_length=50, blank=True)

    description = models.TextField(blank=True)
    skill1 = models.CharField(max_length=30, blank=True)
    skill1_years = models.SmallIntegerField(default=0)
    skill1_months = models.SmallIntegerField(default=0)
    skill2 = models.CharField(max_length=30, blank=True)
    skill2_years = models.SmallIntegerField(default=0)
    skill2_months = models.SmallIntegerField(default=0)
    skill3 = models.CharField(max_length=30, blank=True)
    skill3_years = models.SmallIntegerField(default=0)
    skill3_months = models.SmallIntegerField(default=0)


    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title