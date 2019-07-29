from django import forms
from . models import AllFeilds_1

class AllFeilds_Form(forms.ModelForm):

    class Meta:
        model = AllFeilds_1
        fields = '__all__'
        # gender = forms.ChoiceField(widget=forms.RadioSelect(choices=gender),label="") 
    
class AllFeildForm(forms.Form):
    name = forms.CharField(max_length=20)
    address = forms.CharField(max_length=20)
    email = forms.EmailField(label='email')
    city = forms.ChoiceField(choices=[('pune','Pune'),('mumbai','Mumbai'),('nashik','Nashik'),('banglore','Banglore')])
    feedback = forms.CharField(widget=forms.Textarea)
    url = forms.URLField()

gender= [
    ('male', 'Male'),
    ('female', 'Female'),
    ]
class UserForm(forms.Form):
    name= forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    email= forms.EmailField()
    gender= forms.CharField(widget=forms.RadioSelect(choices=gender))
    
    