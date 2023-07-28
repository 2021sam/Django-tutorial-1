from django.urls import path
from . import views

# urlpatterns = [
#     path('profile/edit/<int:id>/', views.profile_edit, name='profile-edit'),
# ]


urlpatterns = [
    path('profile/edit/', views.profile_edit, name='profile-edit'),
]
