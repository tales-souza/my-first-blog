from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required # biblioteca para forçar o usuario estar logado para entrar na página


from .forms import CategoriaForm, TarefaForm
from django.http import HttpResponse
from .models import Categoria, Tarefa
from django.contrib import messages #framework de mensagem





# Create your views here.
@login_required
def nova_categoria(request):
	if request.method == 'POST':
		form = CategoriaForm(request.POST)
		if form.is_valid():
			f = form.save(commit=False)
			f.user = request.user
			f.save()
			return redirect('tarefas:lista_categorias')
		else:
			print(form.errors)
	else:
		form = CategoriaForm()
	return render(request, 'tarefas/nova_categoria.html',{'form':form})

@login_required
def lista_categorias(request):
	categorias = Categoria.objects.filter(user=request.user) # mostra as categorias só do usuário
	return render(request, 'tarefas/lista_categorias.html', {'categorias': categorias})




@login_required
def delete_categoria(request, id_categoria):
    categoria = Categoria.objects.get(id=id_categoria)
    if categoria.user == request.user:
        categoria.delete()
    else:
        messages.error(request, 'Você não tem permissão para fazer isso =).')
        return render(request, 'tarefas/lista_categorias.html')
    return redirect('tarefas:lista_categorias')

@login_required
def editar_categoria(request, id_categoria): # editar categoria
	categoria = get_object_or_404(Categoria, id=id_categoria, user=request.user)
	if request.method == 'POST':
		form = CategoriaForm(request.POST, instance=categoria)
		if form.is_valid():
			form.save()
			return redirect('tarefas:lista_categorias')
	else:
		form = TarefaForm(instance=categoria)
	return render(request, 'tarefas/nova_categoria.html', {'form': form})



@login_required
def nova_tarefa(request):
	if request.method == 'POST':
		form = TarefaForm(user = request.user, data= request.POST)
		if form.is_valid():
			f = form.save(commit=False)
			f.user = request.user
			f.save()
			return redirect('tarefas:lista_tarefas')
		else:
			print(form.errors)
	else:
		form = TarefaForm(user = request.user)
	return render(request, 'tarefas/nova_tarefa.html',{'form':form})
@login_required
def delete_tarefa(request,id_tarefa):
	tarefa = Tarefa.objects.get(id=id_tarefa)
	if tarefa.user == request.user:
		tarefa.delete()
	else:
		messages.error(request,'Você não tem permissão para isso =)')
		return render(request,'tarefas/lista_tarefas.html')
	return redirect('tarefas:lista_tarefas')

@login_required
def editar_tarefa(request, id_tarefa): # editar tarefa
	tarefa = get_object_or_404(Tarefa, id=id_tarefa, user=request.user)
	if request.method == 'POST':
		form = TarefaForm(user = request.user, data =request.POST, instance=tarefa)
		if form.is_valid():
			form.save()
			return redirect('tarefas:lista_tarefas')
	else:
		form = TarefaForm(user= request.user, instance=tarefa)
	return render(request, 'tarefas/nova_tarefa.html', {'form': form})


@login_required
def search(request):
	q = request.GET.get('search')
	if q is not None:
		result = Tarefa.objects.search(q,request.user)
	return render(request, 'tarefas/pagina_resultado.html', {'result':result})


@login_required
def detalhes_tarefa(request, id_tarefa):
	tarefa = get_object_or_404(Tarefa,id=id_tarefa, user=request.user)
	return render(request,'tarefas/detalhes_tarefa.html',{'tarefa':tarefa})


@login_required
def lista_tarefas(request):
	tarefas = Tarefa.objects.filter(user=request.user, status='') # mostra as categorias só do usuário
	return render(request, 'tarefas/lista_tarefas.html', {'tarefas': tarefas})


