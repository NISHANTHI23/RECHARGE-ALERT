# myapp/forms.py

from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'department', 'phone_number', 'recharge_plan_validity']
