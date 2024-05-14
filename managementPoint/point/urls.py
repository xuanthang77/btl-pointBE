from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import SubjectViewSet, GradeViewSet, ForumPostViewSet, ForumCommentViewSet,UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'subjects', SubjectViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'forum-posts', ForumPostViewSet)
router.register(r'forum-comments', ForumCommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),  # Thay đổi tên không gian URL của admin
    path('o/', include('oauth2_provider.urls', namespace='oauth2')),  # Thay đổi tên không gian URL của oauth2_provider
]
