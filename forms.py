from django.contrib.auth.forms import UserCreationForm
import django.contrib.auth
User=django.contrib.auth.get_user_model()
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']