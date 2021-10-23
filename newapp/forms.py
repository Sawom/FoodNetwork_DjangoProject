from django import forms
from newapp import models

#customer form
class customerForm(forms.ModelForm):
    class Meta:
        model = models.customer
        fields = "__all__"

#order form
class orderForm(forms.ModelForm):
    class Meta:
        model = models.order
        fields = "__all__"
