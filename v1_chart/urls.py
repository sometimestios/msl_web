from django.conf.urls import url
from . import views

urlpatterns = [
    url('bar/', views.ChartView.as_view(), name='v1_chart'),
    url('line/', views.ChartView.as_view(), name='v1_chart'),
    url('lineUpdate/', views.ChartUpdateView.as_view(), name='v1_chart'),
    # url('index/', views.IndexView.as_view(), name='v1_chart'),
]
