from django.shortcuts import render
from django.http import HttpResponse
from .models import Log


# Create your views here.
def index(request):
    log_list = Log.objects.all().order_by('-created_time')
    return render(request, 'v1_admin/index.html', context={
        'title': '网络靶场日志管理平台',
        'welcome': '测试',
        'log_list': log_list,
    })


def log_check(request):
    return render(request, 'v1_admin/log_check.html')


def log_add(request):
    return render(request, 'v1_admin/log_add.html')


def tartget_check(request):
    return render(request, 'v1_admin/target_check.html')


def target_add(request):
    return render(request, 'v1_admin/target_add.html')


def task_manage(request):
    return render(request, 'v1_admin/task_manage.html')
