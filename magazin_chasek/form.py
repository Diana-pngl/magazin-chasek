from magazin_chasek import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
class FormDR(UserCreationForm):
    class Meta():
        model = models.Polzovatel
        fields = ['username','email','password1','password2']

class FormDI(UserChangeForm):
    class Meta():
        model = models.Polzovatel
        fields = ['username','email','nomer','adres']