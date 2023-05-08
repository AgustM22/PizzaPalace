from django.forms import ModelForm, widgets
from user.models import UserProfile

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['id','user']
        widgets = {
            'FullName':widgets.TextInput(attrs={'class': 'form-control'}),
            'ProfilePic':widgets.TextInput(attrs={'class': 'form-control'}),
            'StreetName':widgets.TextInput(attrs={'class': 'form-control'}),
            'HouseNumber':widgets.TextInput(attrs={'class': 'form-control'}),
            'City':widgets.TextInput(attrs={'class': 'form-control'}),
            'Country':widgets.Select(attrs={'class': 'form-control'}),
            'PostalCode':widgets.TextInput(attrs={'class': 'form-control'}),
            'PhoneNumber':widgets.TextInput(attrs={'class': 'form-control'})
        }