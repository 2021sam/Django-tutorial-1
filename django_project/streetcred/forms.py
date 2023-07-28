from django.forms import ModelForm
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'work_authorization', 'willing_to_relocate', 'address', 'birth_date', 'drivers_license', 'linkedin']

    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # address = models.TextField(max_length=500, blank=True)
    # birth_date = models.DateField(null=True, blank=True)
    # ip1 = models.TextField(max_length=46, blank=True)
    # ip2 = models.TextField(max_length=46, blank=True)
    # mac1 = models.TextField(max_length=50, blank=True)
    # mac2 = models.TextField(max_length=50, blank=True)
    # drivers_license = models.TextField(max_length=30, blank=True)
    # linkedin = models.TextField(max_length=50, blank=True)
    # portfolio = models.TextField(max_length=50, blank=True)
    # residential_street_address = models.TextField(max_length=50, blank=True)
    # residential_city_address = models.TextField(max_length=50, blank=True)
    # residential_state_address = models.TextField(max_length=50, blank=True)
    # residential_zip_address = models.TextField(max_length=50, blank=True)
    # work_street_address = models.TextField(max_length=50, blank=True)
    # work_city_address = models.TextField(max_length=50, blank=True)
    # work_state_address = models.TextField(max_length=50, blank=True)
    # work_zip_address = models.TextField(max_length=50, blank=True)
    # mobile_cell_number = models.TextField(max_length=14, blank=True)
    # willing_to_relocate = models.BooleanField(default=False)
    # # (456) 456-1234       Will need to format.
    # work_authorization = models.CharField(max_length=25, blank=True, choices=CHOICES_WORK_AUTHORIZATION)
