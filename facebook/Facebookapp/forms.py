from django import forms
from .models import Profile_final
from django.contrib.auth import (
authenticate,
get_user_model,
login,
logout
)
User=get_user_model()
class UserLoginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")

        if username and password:
            user=authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError("this user is does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("password is incorrect")
            if not user.is_active:
                raise forms.ValidationError("user is not active")
        return super(UserLoginForm,self).clean(*args,**kwargs)

class UserRegisterForm(forms.ModelForm):
    email=forms.EmailField(label='enter mail')
    email2=forms.EmailField(label='confirm mail')
    password=forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model=User
        fields=['username','email','email2','password']

    def clean(self,*args,**kwargs):
        email=self.cleaned_data.get("email")
        email2=self.cleaned_data.get("email2")
        if email != email2:
            raise forms.ValidationError("BOth mail id need to same")
        email_qs=User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("email is allready registered")
        return super(UserRegisterForm,self).clean(*args,**kwargs)

class UserProfileForm(forms.ModelForm):
    # AddImage=forms.ImageField(label="choose a image")

    class Meta:
        model=Profile_final
        fields=['profile_image','user']

