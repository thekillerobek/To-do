from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def todo_list(request):
    tasks = Todo.objects.all()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm()
    return render(request, 'index.html', {'form': form, 
                        'tasks': tasks})