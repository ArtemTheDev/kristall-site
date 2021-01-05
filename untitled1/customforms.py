from allauth.account.forms import SignupForm
from django import forms

class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        #name
        first_name = forms.CharField(max_length=12, label='first_name')
        self.fields['first_name'] = forms.CharField(required=True)

        #surname
        last_name = forms.CharField(max_length=12, label='last_name')
        self.fields['last_name'] = forms.CharField(required=True)

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user