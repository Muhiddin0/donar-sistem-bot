from django import forms

class XabarYuborishForm(forms.Form):
    content = forms.FileField(required=False)
    captions = forms.CharField(help_text='Xabar mazmunini shu yerga yozing')
    buttons = forms.JSONField()