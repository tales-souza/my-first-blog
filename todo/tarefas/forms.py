from django import forms

from .models import Categoria, Tarefa

class CategoriaForm(forms.ModelForm):
	class Meta:
		model = Categoria
		exclude = ('user',) #só mostre os inputs do criador da categoria




class TarefaForm(forms.ModelForm):
	class Meta:
		model = Tarefa
		exclude = ('user',) #só mostre os inputs do criador da categoria


	def __init__(self, user=None, *args, **kwargs):
		super(TarefaForm,self).__init__(*args, **kwargs)
		if user is not None:
			self.fields['categoria'].queryset = Categoria.objects.filter(user=user) #filtra as categorias só do usuario logado
	

	
		





