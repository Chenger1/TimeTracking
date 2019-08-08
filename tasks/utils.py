from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse


class TaskAddMixin:
    model = None
    form = None
    template = None

    def post(self, request):
        form = self.form(request.user, request.POST)
        if form.is_valid():
            time_trigger = form.cleaned_data['time_trigger']
            name = form.cleaned_data['name']
            times = [
                form.cleaned_data['scheduled_hours'],
                form.cleaned_data['scheduled_minutes'],
                form.cleaned_data['spent_hours'],
                form.cleaned_data['spent_minutes'],
            ]
            self.time_processing(times, time_trigger)
            description = form.cleaned_data['description']
            category = form.cleaned_data['category']
            new_action = self.model.objects.create(
                user=request.user,
                name=name,
                spent_hours=times[2],
                spent_minutes=times[3],
                scheduled_hours=times[0],
                scheduled_minutes=times[1],
                time_trigger=time_trigger,
                description=description,
            )
            new_action.category.set(category)
            return redirect(reverse('task_list_url'))
        return redirect(reverse('task_list_url'))

    @staticmethod
    def time_processing(times, time_trigger):
        for index, item in enumerate(times):
            if item == None:  # Заменяет пустую строку на 0
                times[index] = 0
        if time_trigger:
            if times[1] >= 60:
                while times[1] >= 60:
                    times[0] += 1
                    times[1] -= 60
                return times
        else:
            if times[3] >= 60:
                while times[3] >= 60:
                    times[2] += 1
                    times[3] -= 60
            if times[1] != 0:
                if times[1] >= 60:
                    while times[1] >= 60:
                        times[0] += 1
                        times[1] -= 60
                return times


class TaskUpdateMixin:
    model = None
    form = None

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        form = self.form(request.user, request.POST, request.FILES, instance=obj)
        if form.is_valid():
            time_trigger = form.cleaned_data['time_trigger']
            times = [
                form.cleaned_data['scheduled_hours'],
                form.cleaned_data['scheduled_minutes'],
                form.cleaned_data['spent_hours'],
                form.cleaned_data['spent_minutes'],
            ]
            TaskAddMixin.time_processing(times, time_trigger)
            print(times)
            new_obj = form.save()
            new_obj.spent_hours = times[2]
            new_obj.spent_minutes = times[3]
            new_obj.scheduled_hours = times[0]
            new_obj.scheduled_minutes = times[1]
            new_obj.save()
            return redirect(reverse('task_list_url'))
        print(form.errors)
        return redirect(reverse('task_list_url'))


class TaskHiddenMixin:
    model = None

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.is_available = False
        obj.save()
        return redirect(reverse('task_list_url'))


class TaskRestoreMixin:
    model = None

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.is_available = True
        obj.save()
        return redirect(reverse('task_list_url'))


class CategoryAddMixin:
    model = None
    form = None
    template = None

    def post(self, request):
        form = self.form(request.user, request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            self.model.objects.create(
                user=request.user,
                name=name
            )
            return redirect(reverse('task_list_url'))
        return render(request, self.template, context={'forms': form})


class TaskDeleteMixin:
    model = None
    url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.url))


class TaskHiddenMixin:
    model = None
    url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.is_available = False
        obj.save()
        return redirect(reverse(self.url))


class TaskRestoreMixin:
    model = None
    url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.is_available = True
        obj.save()
        return redirect(reverse(self.url))


class CategoryDeleteMixin:
    model = None
    url = None

    def get(self,request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.url))






