from django import forms
from django.core.validators import ValidationError
from .models import Message



class ContactUsForm(forms.Form):
    BIRTH_YEAR_CHOISES = ['1980', '1981', '1982']
    FAVORITE_COLORS_CHOISES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]
    name = forms.CharField(max_length=20, label='your name')
    text = forms.CharField(max_length=500, label='your message')
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOISES, attrs={'class': 'form-control'}))
    colors = forms.MultipleChoiceField(widget=forms.RadioSelect(), choices=FAVORITE_COLORS_CHOISES)

    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        # if 'a' in name:
        #     self.add_error('name', 'The letter a is not allowed in name')
        if name == text:
            raise ValidationError('The name and the text are the same', code='name_text_same')
        
    # def clean_name(self):
    #     name = self.cleaned_data.get('name')    
    #     if 'a' in name:
    #         raise ValidationError('The letter a is not allowed in name', code='a_in_name')


# class MessageForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     text = forms.CharField(widget=forms.Textarea())
#     email = forms.EmailField()
#     age = forms.IntegerField()

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        # fields = '__all__'
        fields = ('title', 'text')