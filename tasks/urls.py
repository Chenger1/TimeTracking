from django.urls import path

from .views import *

urlpatterns = [
    path('task-list/', TaskListView.as_view(),
         name='task_list_url'),
    path('create/', TaskAddView.as_view(),
         name='task_add_url'),
    path('update-<slug:slug>/', TaskUpdateView.as_view(),
         name='task_update_url'),
    path('hidden-<slug:slug>/', TaskHidden.as_view(),
         name='task_hidden_url'),
    path('restore-<slug:slug>/', TaskRestore.as_view(),
         name='task_restore_url'),
    path('tasl-delete/<slug:slug>/', TaskDelete.as_view(),
         name='task_delete_url'),
    path('category-create/', CategoryAddView.as_view(),
         name='category_add_url'),
    path('category-view-<slug:slug>/',CategoryView.as_view(),
         name='category_view_url'),
    path('category-delete/<slug:slug>/', CategoryDelete.as_view(),
         name='category_delete_url'),
    path('history/', HistoryView.as_view(),
         name='history_url'),

]