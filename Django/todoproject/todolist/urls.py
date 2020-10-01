from django.urls import path

from todolist import views

urlpatterns = [
    path('',views.home,name='home'),
#   path('task_detail/<int:task_id>',views.task_detail,name='task_detail'),
    path('addTask/',views.addTask,name='addTask'),
    path('completeTask/<int:task>',views.completeTask,name='completeTask'),
]
    