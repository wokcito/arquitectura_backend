from django import forms
from airbnb.models import Property, User

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'address',
            'price',
            'priceBy',
            'max_guests',
            'description'
        ]

class SignUpUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
