from django import forms

class RainfallForm(forms.Form):
    '''
    classs that creates the Rainfall addition form
    ''' 
    city = forms.CharField(label='City',max_length = 30)
    amount = forms.ImageField(label = 'Amount of Rainfall(mm)') 
    