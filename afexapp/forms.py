from django import forms
from afexapp.models import UserProfile, Tasks
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileForm(forms.ModelForm):
 
    class Meta():
        model = UserProfile
        fields = ('phonenumber',)

class TasksForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    class Meta():
        model = Tasks
        fields = ('task','description', 'date')        