from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from cogs import views


router = DefaultRouter()
router.register(r'cogs', views.CogViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'notes', views.NoteViewSet)
router.register(r'personalnotes', views.PersonalNoteViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'api-auth', include('rest_framework.urls')),
]
