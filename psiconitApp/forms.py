from django import forms
from .models import usuario

class usuarioForm(forms.ModelForm):
    class Meta:
        model = usuario
        #fields = ["numero", "importe", "fecha", "cliente", "observacion"]
        fields = ["username","email","first_name","last_name","fecha","password1","password2"]