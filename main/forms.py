from django import forms
from .models import FactionMember, Faction
from django.core.exceptions import ValidationError

class MemberForm(forms.ModelForm):

    class Meta:
        model = FactionMember
        fields = ['name', 'role', 'bio', 'faction']
        widgets = {
            'bio': forms.Textarea(attrs={'rows':5, 'cols':40, 'placeholder':'Описание участника'}),
            'role': forms.Select(attrs={'class':'role-select'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise ValidationError('Имя обязательно')
        if len(name) < 3:
            raise ValidationError('Имя слишком короткое (минимум 3 символа)')
        if len(name) > 100:
            raise ValidationError('Имя слишком длинное (максимум 100 символов)')
        return name

    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if not bio:
            raise ValidationError('Описание обязательно')
        if len(bio) < 10:
            raise ValidationError('Описание слишком короткое (минимум 10 символов)')
        if len(bio) > 1000:
            raise ValidationError('Описание слишком длинное (максимум 1000 символов)')
        return bio

    def clean_faction(self):
        faction = self.cleaned_data.get('faction')
        if not faction:
            raise ValidationError('Нужно выбрать фракцию')
        return faction