from django import forms
from EcospaceEcom.models import Email


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email']