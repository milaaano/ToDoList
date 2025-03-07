from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from django.shortcuts import get_object_or_404, redirect
from django.utils.timezone import now, localtime


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    ordering = ['priority']

    def get_queryset(self):
        tasks = Task.objects.filter(completed=False)
        for task in tasks:
            if task.due_date and task.due_date.strftime("%H:%M:%S") == "00:00:00":
                task.due_date = task.due_date.date()
        return tasks


class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'priority']
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'priority']
    template_name = 'task_form.html'
    # success_url = reverse_lazy('task_list')
    def get_success_url(self):
        task = self.object
        if task.completed:
            return reverse_lazy('task_complete')
        return reverse_lazy('task_list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    # success_url = reverse_lazy('task_list')

    def get_success_url(self):
        task = self.object
        if task.completed:
            return reverse_lazy('task_complete')
        return reverse_lazy('task_list')


class TaskCompleteView(ListView):
    model = Task
    template_name = "task_completed.html"
    context_object_name = 'completed'

    # def get_queryset(self):
    #     return Task.objects.filter(completed=True)
    def get_queryset(self):
        tasks = Task.objects.filter(completed=True)
        for task in tasks:
            if task.due_date and task.due_date.strftime("%H:%M:%S") == "00:00:00":
                task.due_date = task.due_date.date()
        return tasks


# class MarkCompleteView(View):
#     def get(self, request, pk):
#         task = get_object_or_404(Task, pk=pk)
#         task.completed = True
#         task.completed_date = now()
#         task.save()
#         return redirect('task_complete')

class ToggleCompleteView(ListView):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)

        if task.completed:
            task.completed = False
            task.completed_date = None
        else:
            task.completed = True
            task.completed_date = now()

        task.save()

        if task.completed:
            return redirect('task_complete')
        else:
            return redirect('task_list')