from allauth.account.forms import SignupForm
from django import forms
class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        organization = forms.CharField(max_length=12, label='Phone')
        self.fields['organization'] = forms.CharField(required=True)
    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.organization = self.cleaned_data['organization']
        print(user.organization)
        user.save()
        return user