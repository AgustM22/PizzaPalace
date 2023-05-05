from django import forms
from user.models import Users

class SignUpForm(forms.ModelForm):
    ConfirmPassword = forms.CharField(widget=forms.PasswordInput())
    CountryOptions = [
        ('Alabama',"Alabama"),
        ('Alabama2',"Alabama2")
        ]
    Country = forms.ChoiceField(choices=CountryOptions, widget=forms.Select)
    class Meta:
        model = Users
        fields = ['FullName','UserName','Password','StreetName','HouseNumber','City','Country','PostalCode']
        widget = {
            'Password': forms.PasswordInput(),
        }


    def clean(self): 
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data