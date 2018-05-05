from django.shortcuts import render
from django.http import HttpResponse

from todo.tarefas.models import Tarefa
from django.contrib.auth.decorators import login_required # biblioteca para forçar o usuario estar logado para entrar na página


# Create your views here.

@login_required
def home(request):
	tarefas = Tarefa.objects.filter(user=request.user, status='') #SELECT * FROM tarefa where user= ""; ORM - Object Relationship Manager
	return render(request, 'core/index.html',{'tarefas': tarefas})
