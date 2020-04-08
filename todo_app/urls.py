from django.urls import path
from .views import NewTaskView,UpdateTaskView,DeleteTaskView

urlpatterns = [
    # path('',HomePageView.as_view(),name='home'),
    path('',NewTaskView.as_view(),name='new_task'),
    path('edit/<int:pk>',UpdateTaskView.as_view(),name= 'update'),
    path('delete/<int:pk>',DeleteTaskView.as_view(),name='delete'),
]

