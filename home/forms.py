from django import forms
from .models import Post


PRODUCT_QUANTITY_CHOICES = [(i,str(1))for i in range (1,21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices = PRODUCT_QUANTITY_CHOICES,
                                    coerce=int)

    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

class Post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ["user"]
