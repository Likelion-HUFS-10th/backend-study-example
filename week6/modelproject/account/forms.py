from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    class Meta: 
        model = CustomUser
        fields = ['nickname','university', 'location']