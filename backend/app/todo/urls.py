from rest_framework.routers import DefaultRouter

from app.todo import views

router= DefaultRouter()
router.register('note',views.TodoModelViewSet)

urlpatterns=router.urls


