from django import forms
from . models import Add_Rainfall

class RainfallForm(forms.Form):
    '''
    classs that creates the Rainfall addition form
    ''' 
    city = forms.CharField(label='City',max_length = 30)
    amount = forms.IntegerField(label = 'Amount of Rainfall(mm)') 

class RainfallForm2(forms.ModelForm):
    class Meta:
        model = Add_Rainfall
        fields = ('amount','city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = Add_Rainfall.objects.none()
    