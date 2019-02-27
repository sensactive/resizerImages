from django import forms
from .models import Picture


class PictureUploadForm(forms.ModelForm):

    class Meta:
        model = Picture
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control text-center'
            field.help_text = ''

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['img'] and cleaned_data['urlImg']:
            raise forms.ValidationError("Должно быть заполнено только одно из полей")


class PictureUpdateForm(forms.Form):

    width = forms.IntegerField()
    height = forms.IntegerField()
    size = forms.FloatField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control text-center'
            field.help_text = ''

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['width'] < 1 or cleaned_data['height'] < 1 or cleaned_data['size'] < 1:
            raise forms.ValidationError('Значения в полях должны быть больше 0')