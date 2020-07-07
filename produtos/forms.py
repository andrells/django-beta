from django import forms
from .models import Produtos

class ProdutosForm(forms.ModelForm):

    class Meta:
        model = Produtos
        fields = ('nome_produto','qnt_produto','valor_produto', 'tipo_opcional')
