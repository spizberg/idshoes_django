from django import forms

class TestingForm(forms.Form):
    iou = forms.DecimalField(label="iou", min_value=0, max_value=1, widget=(forms.TextInput(attrs={'class':'form-control','placeholder':'Non Max Suppression IoU'})), required=False)
    conf = forms.DecimalField(label="conf", min_value=0, max_value=1, widget=(forms.TextInput(attrs={'class':'form-control','placeholder':'Niveau de confiance'})), required=False)
    image = forms.FileField()