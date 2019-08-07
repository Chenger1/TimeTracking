from django.urls import path

from .views import *

urlpatterns = [
    path('task-list/', TaskListView.as_view(),
         name='task_list_url'),
    path('create/', TaskAddView.as_view(),
         name='task_add_url'),
    path('update-<slug:slug>/', TaskUpdateView.as_view(),
         name='task_update_url'),
    path('hidden-<slug:slug>/', DeleteAndRestore.hidden,
         name='task_hidden_url'),
    path('restore-<slug:slug>/', DeleteAndRestore.restore,
         name='task_restore_url'),
    path('category-create/', CategoryAddView.as_view(),
         name='category_add_url'),
    path('category-view-<slug:slug>/',CategoryView.as_view(),
         name='category_view_url'),
    path('delete/<slug:slug>', DeleteAndRestore.delete,
         name='delete_url'),
    path('history/', HistoryView.as_view(),
         name='history_url'),

]