from django.shortcuts import render, redirect
from .forms import TaskForm, TaskUpdateForm
from django.views import View
from django.contrib.auth.decorators import login_required
from django.db.models import Case, CharField, Value, When
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import Tasks


class ListTasksView(LoginRequiredMixin, View):
    login_url = 'Register:login'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        tasks = Tasks.objects.filter(user=request.user).annotate(
            custom_order=Case(
                When(priority='High', then=Value(1)),
                When(priority='Medium', then=Value(2)),
                When(priority='Low', then=Value(3)),
                default=Value(4),
                output_field=CharField()
            )
        ).order_by('custom_order')
        context = {
            'tasks': tasks
        }
        return render(request, 'Tasks/tasklist.html', context)


class TaskCreateView(View, LoginRequiredMixin):
    login_url = 'Register:login'
    redirect_field_name = 'redirect_to'
    def get(self, request):
        form = TaskForm()
        context = {
            'form': form
        }
        return render(request, 'Tasks/taskcreate.html', context)

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('Home')
        context = {
            'form': form
        }
        return render(request, 'Tasks/taskcreate.html', context)


class TaskUpdateView(View, LoginRequiredMixin):
    login_url = 'Register:login'
    redirect_field_name = 'redirect_to'
    def get(self, request, id):
        task = Tasks.objects.get(id=id)
        form = TaskForm(instance=task)
        context = {
            'form': form
        }
        return render(request, 'Tasks/taskcreate.html', context)

    def post(self, request, id):
        task = Tasks.objects.get(id=id)
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('Home')
        context = {
            'form': form
        }
        return render(request, 'Tasks/taskcreate.html', context)


@login_required(login_url='Register:login', redirect_field_name='redirect_to')
def task_delete(request, id):
    task = Tasks.objects.get(id=id)
    task.delete()
    return redirect('Home')

@login_required(login_url='Register:login', redirect_field_name='redirect_to')
def complete_task(request, id):
    task = Tasks.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect('Home')
