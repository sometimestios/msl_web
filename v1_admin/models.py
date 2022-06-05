from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Service(models.Model):
    name = models.CharField('名称', max_length=50)

    class Meta:
        verbose_name = '服务'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Attack(models.Model):
    name = models.CharField('名称', max_length=50)

    class Meta:
        verbose_name = '攻击'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Target(models.Model):
    name = models.CharField('名称', max_length=50)
    ip = models.CharField('ip', max_length=50)
    os = models.CharField('os', max_length=50)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    desc = models.TextField('描述')

    class Meta:
        verbose_name = '靶标'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Log_type(models.Model):
    name = models.CharField('日志类型', max_length=50)

    class Meta:
        verbose_name = '日志类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Log(models.Model):
    target = models.ForeignKey(Target, verbose_name='靶标', on_delete=models.CASCADE)
    log_type = models.ForeignKey(Log_type, verbose_name='日志类型', on_delete=models.CASCADE)
    path1 = models.CharField('路径', max_length=50)
    path2 = models.CharField('路径', max_length=50)
    desc = models.TextField('描述')

    class Meta:
        verbose_name = '日志'
        verbose_name_plural = verbose_name
    def __str__(self):
        return f'{self.target}_{self.log_type}'