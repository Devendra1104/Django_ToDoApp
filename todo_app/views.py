from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Todo
from django.urls import reverse_lazy

# class HomePageView(ListView):
#     template_name = 'home.html'
#     model = Todo
#     context_object_name = 'tasks'
#     success_url = reverse_lazy('new_task')

class NewTaskView(CreateView,ListView):
    model = Todo
    template_name = 'home.html'
    fields = ['title']
    success_url = reverse_lazy('new_task')
    context_object_name ='tasks'

class UpdateTaskView(UpdateView):
    model = Todo
    template_name = 'edit.html'
    fields = ['title','complete']
    success_url = reverse_lazy('new_task')

class DeleteTaskView(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('new_task')
