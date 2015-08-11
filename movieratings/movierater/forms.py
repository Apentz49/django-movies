from django.forms import ModelForm
from movierater.models import Rating


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ('movie','rating',)
