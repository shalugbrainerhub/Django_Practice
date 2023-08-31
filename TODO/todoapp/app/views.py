from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Task
from .forms import AddTaskForm, UpdateTaskForm

# Create your views here.

def index(request):
    return HttpResponse("Welcome to home page of todoapp")


def viewTask(request):
    allTask=Task.objects.all()
    print(allTask)
    return render(request, 'app/viewTask.html', {'allTask':allTask})


def addTaskView(request):
    if request.method=='POST':
        form=AddTaskForm(request.POST)
        if form.is_valid():
            print("inside the form validation")
            title = form.cleaned_data['title']
            completed=form.cleaned_data['completed']
            print(title)
            new_task = Task(title=title, completed=completed)
            new_task.save()
            return redirect('allTask')
   
    else:
        form=AddTaskForm()


    return render(request, 'app/addTask.html', {'form':form})



# def updateTaskView(request, pk):
#     task=get_object_or_404(Task, id=pk)

#     if request.method=='POST':
#         form=UpdateTaskForm(request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#             return redirect('allTask')
        
#     else:
#         form=UpdateTaskForm(instance=task)

#     return render(request, 'app/updateTask.html', {'form':form, 'task':task})
        


def updateTaskView(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = UpdateTaskForm(request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.completed = form.cleaned_data['completed']
            task.save()
            return redirect('allTask')

    else:
        form = UpdateTaskForm(initial={'title': task.title, 'completed': task.completed})

    return render(request, 'app/updateTask.html', {'form': form, 'task': task})





def deleteTaskView(request, task_id):
    task=get_object_or_404(Task, id=task_id)
    if request.method=='POST':
        task.delete()
        return redirect('allTask')
    

    return render(request, 'app/deleteTask.html', {'task':task})