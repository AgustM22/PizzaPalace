from django import forms
from user.models import Users

class SignUpForm(forms.ModelForm):
    ConfirmPassword = forms.CharField(widget=forms.PasswordInput())
    CountryOptions = [
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
        ('NG', 'Nigeria')
        ]
    Country = forms.ChoiceField(choices=CountryOptions, widget=forms.Select)
    class Meta:
        model = Users
        fields = ['FullName','UserName','Password','StreetName','HouseNumber','City','Country','PostalCode']
        widgets = {
            'Password': forms.PasswordInput(),
        }


    #Need a password confirm validation