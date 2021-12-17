from django import forms
from IPLWebApp.models import Banglore, chennai, mumbai, delhi, kolkata, punjab, rajasthan, hyderabad, addTeam, \
    addNewPlayers


#FORMS


class BangaloreForm(forms.ModelForm):
    class Meta:
        model = Banglore
        fields = '__all__'


class ChennaiForm(forms.ModelForm):
    class Meta:
        model = chennai
        fields = '__all__'


class MumbaiForm(forms.ModelForm):
    class Meta:
        model = mumbai
        fields = '__all__'


class DelhiForm(forms.ModelForm):
    class Meta:
        model = delhi
        fields = '__all__'


class  KolkataForm(forms.ModelForm):
    class Meta:
        model = kolkata
        fields = '__all__'


class PunjabForm(forms.ModelForm):
    class Meta:
        model = punjab
        fields = '__all__'


class RajasthanForm(forms.ModelForm):
    class Meta:
        model = rajasthan
        fields = '__all__'


class HyderabadForm(forms.ModelForm):
    class Meta:
        model = hyderabad
        fields = '__all__'


class AddNewTeam(forms.ModelForm):
    class Meta:
        model = addTeam
        fields = '__all__'


class AddNewPlayers(forms.ModelForm):
    class Meta:
        model = addNewPlayers
        fields = '__all__'



