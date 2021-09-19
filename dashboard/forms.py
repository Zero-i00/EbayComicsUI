from django import forms
from .models import SnipeModel


class SnipeForm(forms.ModelForm):

    class Meta:
        model = SnipeModel
        fields = [
            'gocollect_link',
            'price_percentage',
            'floor_price',
            'lowest_grade',
            'highest_grade',
            'negative_words',
        ]