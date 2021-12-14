# from django.shortcuts import render
# from django.http import HttpResponse

# def sayHello(req):
#     return render(req, 'hello.html', {'name': 'Susy'})
from django.db.models.fields import DateField
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.shortcuts import render

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.views import View
from django.shortcuts import redirect
from django.db import models, transaction

from .models import Task
from .forms import PositionForm, AddForm


class CustomLoginView(LoginView):
    template_name = 'myapp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class RegisterPage(FormView):
    template_name = 'myapp/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(rejected=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'myapp/task.html'


class AddBookView(FormView):
    template_name = 'myapp/add.html'
    form_class = AddForm
    success_url = reverse_lazy('tasks')

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = AddForm
    # fields = ['title', 'jobdescription',  'joblink', 'interview', 'rejected']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['updated'] = False
        return context

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = AddForm
    success_url = reverse_lazy('tasks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['updated'] = True
        return context

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)

class TaskReorder(View):
    def post(self, request):
        form = PositionForm(request.POST)

        if form.is_valid():
            positionList = form.cleaned_data["position"].split(',')

            with transaction.atomic():
                self.request.user.set_task_order(positionList)

        return redirect(reverse_lazy('tasks'))

# def get_form(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/thanks/')
#     else:
#         form = TaskForm()
#     return render(request, 'task_form.html', {'form': form})

# from .calendarAPI import test_calendar

# def demo(request):
#     results = test_calendar()
#     context = {"results": results}
#     return render(request, 'myapp/demo.html', context)

from .forms import CalendarForm
  
# Create your views here.
def demo(request):
    context = {}
    context['mydate'] = CalendarForm()
    return render( request, "myapp/task_form.html", context)