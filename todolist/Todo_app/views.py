from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .form import Todo_form
from authentication.models import User
from django.urls import reverse_lazy
from .models import Todo
# Create your views here.

class Todo_list(LoginRequiredMixin,ListView):
    model=Todo
    context_object_name="todos"
    template_name='Todo_app/Todo_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todos"] = context["todos"].filter(author=self.request.user) 
        return context
        

class Todo_item(LoginRequiredMixin,DetailView):
    model=Todo
    context_object_name="todo"
    template_name='Todo_app/Todo_detail.html'

# class Update_item(LoginRequiredMixin,DetailView):
#     model=Todo
    

  
class Update(LoginRequiredMixin,UpdateView):
    # specify the model you want to use
    model = Todo
    # specify the fields
    fields = [
        "title",
        "description",
    ]
    # template_name='Todo_app/Todo_detail.html'
    success_url=reverse_lazy("Todos")

class Create(LoginRequiredMixin,CreateView):
    model=Todo
    template_name="Todo_app/create.html"
    fields=("title","description")
    success_url=reverse_lazy("Todos")
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super(Create,self).form_valid(form)

class Delete(DeleteView):
    model=Todo
    success_url=reverse_lazy("Todos")
def home(request):
    return render(request,"Todo_app/home.html")