from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .models import Log, Target, Task
from .forms import TargetForm


# Create your views here.
def index(request):
    return task_manage(request)


def tartget_check(request):
    target_list = Target.objects.all().order_by('-created_time')
    return render(request, 'v1_admin/target_check.html', context={
        'target_list': target_list
    })


def target_add(request):
    return render(request, 'v1_admin/target_add.html')


@require_POST
def target_form(request):
    form = TargetForm(request.POST)
    if form.is_valid():
        target = form.save(commit=False)
        target.save()
        messages.add_message(request, messages.SUCCESS, '靶标添加成功！', extra_tags='success')
        return tartget_check(request)
    else:
        messages.add_message(request, messages.ERROR, '靶标添加失败！请修改错误后重新提交', extra_tags='danger')
        return render(request, 'v1_admin/target_add.html')


def log_check(request):
    log_list = Log.objects.all().order_by('-created_time')
    return render(request, 'v1_admin/log_check.html', context={
        'log_list': log_list
    })


def log_add(request):
    return render(request, 'v1_admin/log_add.html')


def task_manage(request):
    target_num = Target.objects.all().count()
    log_num = Log.objects.all().count()
    task_list = Task.objects.all().order_by('-created_time')
    return render(request, 'v1_admin/task_manage.html', context={
        'target_num': target_num,
        'log_num': log_num,
        'task_list': task_list,
    })
