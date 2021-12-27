from django import forms

class CalcPlusForm(forms.Form):
#    val1 = forms.FloatField(label='点1x',widget=forms.Textarea(attrs={'cols':'3','rows':'1.5'}))
    val1 = forms.FloatField(label='x1',widget=forms.TextInput(attrs={'size': '2'}))
    val2 = forms.FloatField(label='y1',widget=forms.TextInput(attrs={'size': '2'}))
    val3 = forms.FloatField(label='x2',widget=forms.TextInput(attrs={'size': '2'}))
    val4 = forms.FloatField(label='y2',widget=forms.TextInput(attrs={'size': '2'}))
   