from django import forms

from .models import Order

class OrderForm(forms.ModelForm):
    
    # doing override and taking product
    def __init__(self, *args, **kwargs):
        product = kwargs.pop("product") or None
        super().__init__(*args, **kwargs)
        self.product = product

    class Meta:
        model = Order
        fields = [
            'shipping_address',
            'billing_address',
        ]

    def clean(self, *args, **kwargs):
        self.cleaned_data = super().clean(*args, **kwargs)
        shipping_addr = self.cleaned_data.get("shipping_address")

        # import pdb; pdb.set_trace()
        if self.product != None:
            if not self.product.has_inventory():
                raise forms.ValidationError("This product is out of inventory")
        return self.cleaned_data



    