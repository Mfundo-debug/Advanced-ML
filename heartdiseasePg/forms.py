from django import forms

class InputForm(forms.Form):
    cp_value = forms.DecimalField(min_value=0)
    thalach_value = forms.DecimalField(min_value=0)
    exang_value = forms.DecimalField(min_value=0)
    oldpeak_value = forms.DecimalField(min_value=0)
    slope_value = forms.DecimalField(min_value=0)
    thal_value = forms.DecimalField(min_value=0)
    age_value = forms.DecimalField(min_value=0)
    sex_value = forms.DecimalField(min_value=0)
    ca_value = forms.DecimalField(min_value=0)