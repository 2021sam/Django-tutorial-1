from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'company', 'company_manager', 'recruiter', 'recruiter_email', 'city', 'state', 'degree_type', 'date_start', 'date_end', 'duration', 'description', 'skill1', 'skill1_years', 'skill1_months', 'skill2', 'skill2_years', 'skill2_months', 'skill3', 'skill3_years', 'skill3_months', 'hourly_pay_rate']
