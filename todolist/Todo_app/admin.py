from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *
# Register your models here.
class Todo_model(ModelAdmin):
    model=Todo
    list_display=("title","author","created")
admin.site.register(Todo,Todo_model)