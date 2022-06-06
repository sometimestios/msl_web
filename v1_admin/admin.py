from django.contrib import admin
from .models import Service, Attack, Target, Log_type, Log, Task


# Register your models here.

class TargetAdmin(admin.ModelAdmin):
    list_display = ['name', 'ip', 'os', 'service', 'desc']
    fields = ['name', 'ip', 'os', 'service', 'desc']


class LogAdmin(admin.ModelAdmin):
    list_display = ['target', 'log_type', 'path1', 'path2', 'desc']
    fields = ['target', 'log_type', 'path1', 'path2', 'desc']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['target', 'status']
    fields = ['target', 'logs', 'status']


admin.site.register(Service)
admin.site.register(Attack)
admin.site.register(Log_type)
admin.site.register(Target,TargetAdmin)
admin.site.register(Log,LogAdmin)
admin.site.register(Task,TaskAdmin)
