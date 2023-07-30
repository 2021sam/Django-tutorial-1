from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

CHOICES_DGREE_TYPE = (
    ('select degree type', 'Select Degree Type'),
    ('none', 'None'),
    ('vocational', 'Vocational'),
    ('high school', 'High School'),
    ('bachelors degree', 'Bachelor\'s Degree'),
    ('masters degree', 'Master\'s Degree'),
    ('ged', 'GED')
)

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

    degree_type = models.CharField(max_length=20, blank=True, choices = CHOICES_DGREE_TYPE, default='select degree type')


    description = models.TextField(blank=True)
    skill1 = models.CharField(max_length=30, blank=True, help_text = 'Note: Skills are mutually exclusive in terms of adding time to subset skills.  Furthermore, only experience time with matching terms are added.')
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