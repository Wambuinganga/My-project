from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"
class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=("full_names","email","password", "confirm_password")
class UpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"
        
    # def clean(self):
    #     cleaned_data = super(ShopForm, self).clean()
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get("confirm_password")

    #     if password != confirm_password:
    #         raise forms.ValidationError(
    #             "password and confirm_password does not match")
    # 