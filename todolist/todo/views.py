from django.shortcuts import render, redirect

from .models import Todo


# Create your views here.

def index(request):
    todos = Todo.objects.all()

    if request.method == 'POST':
        new_todo = Todo(title=request.POST['title'])
        new_todo.save()
        return redirect('/')

    return render(request, 'index.html', {'todos': todos})


def delete(request, pk):
    if request.method == 'GET':
        deletable_todo = Todo.objects.get(id=pk)
        deletable_todo.delete()
        return redirect('/')
