from django.shortcuts import render

# Create your views here.
from django.http import request
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, DeleteView
from django.views.generic import DetailView

from .forms import task, task_form
from . models import task

class TaskListview(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'data_add'

class TaskDetailView(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'data'

class TaskUpdateView(UpdateView):
    model=task
    template_name = 'update.html'
    context_object_name = 'data'
    fields=('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('demo:cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model=task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')
def add(request):
    data_add = task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        task_data=task(name=name,priority=priority,date=date)
        task_data.save()
        return  redirect('/')
    return render(request,'home.html',{'data_add':data_add})
def delete(request,taskid):
    if request.method == 'POST':
        data = task.objects.get(id=taskid)
        data.delete()
        return redirect('/')
    return render(request, 'delete.html')
def update(request,taskid):
    data=task.objects.get(id=taskid)
    form_up=task_form(request.POST or None,request.FILES,instance=data)
    if form_up.is_valid():
        form_up.save()
        return redirect('/')

    return render(request,'edit.html',{'form':form_up,'data': data})

