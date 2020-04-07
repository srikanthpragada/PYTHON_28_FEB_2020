from django import forms


class AddEmployeeForm(forms.Form):
    # Fields
    fullname = forms.CharField(max_length=30, required=True, label="Fullname")
    job = forms.CharField(max_length=5, label="Job", required=True)
    salary = forms.IntegerField(required=True, label="Salary")
