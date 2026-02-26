from django.forms import ModelForm, BooleanField
from catalog.models import Product
from django.core.exceptions import ValidationError


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ('views_counter', 'owner')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        unaccepted_names = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        for forbidden_word in unaccepted_names:
            if forbidden_word in name:
                self.add_error('name', f'слово "{forbidden_word}" нельзя использовать в названии')
            elif forbidden_word in description:
                self.add_error('description', f'слово "{forbidden_word}" нельзя использовать в описании')
            else:
                return None

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'published')