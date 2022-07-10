from django.urls import path, include
from task.views import TaskViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = []
urlpatterns += router.urls
