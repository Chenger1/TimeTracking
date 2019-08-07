from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View

# Create your views here.


class MainView(View):

    @staticmethod
    def get(request):
        return redirect('task_list_url', permanent=True)
