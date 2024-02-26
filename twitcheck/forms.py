from django import forms

#Attributes for the form used in check_twitch.html

class TwitchForm(forms.Form):
    username = forms.CharField(max_length=25,
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter Twitch Username'})
        )