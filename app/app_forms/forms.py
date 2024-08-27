from django import forms

from app_forms.models import MyModel


class MyForms(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ["fullname", "mobile_number",]
        labels = {"fullname":"Name", "mobile_number":"Mobile number",}