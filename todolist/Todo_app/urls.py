from django.urls import path
from .views import Todo_list,Todo_item,Update,Create,Delete,home
urlpatterns = [
    path("Todos/",Todo_list.as_view(),name="Todos"),
    path("Todo/<int:pk>/",Todo_item.as_view(),name="Todo"),
    path("update/<int:pk>/",Update.as_view(),name="update"),
    path("create/",Create.as_view(),name="create"),
    path("delete/<int:pk>/",Delete.as_view(),name="delete"),
    path("",home,name="home"),





]
