from django.contrib import admin
from .models import Service,Attack,Target,Log_type,Log
# Register your models here.
admin.site.register(Service)
admin.site.register(Attack)
admin.site.register(Target)
admin.site.register(Log_type)
admin.site.register(Log)
