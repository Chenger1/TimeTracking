from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.urls import reverse

from .models import Task
from .models import Category
from .forms import TaskForm
from .forms import CategoryForm
from .utils import TaskAddMixin
from .utils import CategoryAddMixin
from .utils import TaskUpdateMixin
from .utils import TaskDeleteMixin
from .utils import TaskHiddenMixin
from .utils import TaskRestoreMixin
from .utils import CategoryDeleteMixin
# Create your views here.


class TaskListView(View):

    def get(self, request):
       try:
            model = Task.objects.filter(user=request.user).order_by('-id')
            action_model = [item for item in model if item.is_available]
            category_model = Category.objects.filter(user=request.user)
            category_form = CategoryForm(request.user)
            task_form = TaskForm(request.user)
            context = { 'actions': action_model,
                            'categories': category_model,
                            'category_form': category_form,
                            'task_form': task_form}
            return render(request, 'main/actions.html', context)
       except:
            return render(request, 'main/first_look.html', context={'trigger': True})


class CategoryView(View):

    def get(self, request, slug):
        model = Category.objects.filter(slug__iexact=slug)
        return render(request, 'main/category_view.html', context={'model': model})


class HistoryView(View):

    def get(self, request):
        action_model = Task.objects.filter(user=request.user).order_by('-id')
        return render(request, 'main/history.html', context={'actions': action_model})


class TaskAddView(TaskAddMixin, View):
    model = Task
    form = TaskForm
    template = 'tasks/templates/'


class CategoryAddView(CategoryAddMixin, View):
    model = Category
    form = CategoryForm
    template = 'tasks/templates/'


class TaskUpdateView(TaskUpdateMixin, View):
    model = Task
    form = TaskForm


class TaskDelete(TaskDeleteMixin, View):
    model = Task
    url = 'history_url'


class TaskHidden(TaskHiddenMixin, View):
    model = Task
    url = 'task_list_url'


class TaskRestore(TaskRestoreMixin, View):
    model = Task
    url = 'task_list_url'


class CategoryDelete(CategoryDeleteMixin, View):
    model = Category
    url = 'task_list_url'
