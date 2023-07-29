from django.urls import path
from . import views


app_name='streetcred'
urlpatterns = [
    path('edit/', views.profile_edit, name='edit'),
]
