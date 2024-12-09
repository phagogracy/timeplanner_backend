from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .apis import ProjectAPISet, TaskAPISet

router = SimpleRouter()
router.register("projects", ProjectAPISet)
router.register("tasks", TaskAPISet)

urlpatterns = [path("", include(router.urls))]
