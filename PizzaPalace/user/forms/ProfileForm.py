from django.forms import ModelForm, widgets
from user.models import UserProfile,CreditCard

class ProfileForm(ModelForm):
    class Meta:
        COUNTRIES = (
        ('US', 'United States'),
        ('CA', 'Canada'),
        ('MX', 'Mexico'),
        ('GB', 'United Kingdom'),
        ('DE', 'Germany'),
        ('FR', 'France'),
        ('IT', 'Italy'),
        ('JP', 'Japan'),
        ('CN', 'China'),
        ('IN', 'India'),
        ('BR', 'Brazil'),
        ('AU', 'Australia'),
        ('NZ', 'New Zealand'),
        ('ZA', 'South Africa'),
        ('NG', 'Nigeria'),
        )
        model = UserProfile
        exclude = ['id','user']
        widgets = {
            'FullName':widgets.TextInput(),
            'ProfilePic':widgets.TextInput(),
            'StreetName':widgets.TextInput(),
            'HouseNumber':widgets.TextInput(),
            'City':widgets.TextInput(),
            'Country':widgets.Select(choices=COUNTRIES),
            'PostalCode':widgets.TextInput(),
            'PhoneNumber':widgets.TextInput()
        }

class CreditCardForm(ModelForm):
    class Meta:
        model = CreditCard
        exclude = ['id','user']
        widgets = {
            'NameCardholder':widgets.TextInput(),
            'CardNumber':widgets.TextInput(),
            'ExpirationDate':widgets.DateInput(),
            'CVC':widgets.TextInput(),
        }