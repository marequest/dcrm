# Create Add Record Form
from django import forms
from .models import Record


class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label='First Name', widget=forms.TextInput({"placeholder":"First Name", "class":"form-control"}))
    last_name = forms.CharField(required=True, label='Last Name', widget=forms.TextInput({"placeholder":"First Name", "class":"form-control"}))
    email = forms.EmailField(required=True, label='Email', widget=forms.TextInput({"placeholder":"First Name", "class":"form-control"}))
    phone = forms.CharField(required=True, label='Phone', widget=forms.TextInput({"placeholder":"First Name", "class":"form-control"}))
    country = forms.CharField(required=True, label='Country', widget=forms.TextInput({"placeholder":"First Name", "class":"form-control"}))
    city = forms.CharField(required=True, label='City', widget=forms.TextInput({"placeholder":"First Name", "class":"form-control"}))
    address = forms.CharField(required=True, label='Address', widget=forms.TextInput({"placeholder":"First Name", "class":"form-control"}))

    class Meta:
        model = Record
        exclude = ['user']
        fields = ['first_name', 'last_name', 'email', 'phone', 'country', 'city', 'address']