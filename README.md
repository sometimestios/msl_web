正则表达式替换

(href|src)="(bower_components)(.*?)"

$1="{% static 'v1_admin/$2$3'%}"
