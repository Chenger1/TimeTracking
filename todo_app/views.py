from django.shortcuts import redirect


def redirect_view(request):
	return redirect('task_list_url', permanent=True)