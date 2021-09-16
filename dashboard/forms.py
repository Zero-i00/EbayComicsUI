from django import forms
from .models import SnipeModel


class SnipeForm(forms.ModelForm):

    class Meta:
        model = SnipeModel
        fields = [
            'ebay_item_number',
            'gocollect_link',
            'max_percent_of_price',
            'min_percent_of_price',
            'lowest_grade',
            'highest_grade',
            'negative_words'
        ]