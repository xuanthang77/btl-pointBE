from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="API description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="1951052190thang@ou.edu.vn"),
        license=openapi.License(name="Vu Trong Thang"),
    ),
    public=True,
)
urlpatterns = [
    path('point/', include('point.urls')),
    path('admin/', admin.site.urls),  # Thay đổi tên không gian URL của admin
    path('o/', include('oauth2_provider.urls', namespace='oauth2')),  # Thay đổi tên không gian URL của oauth2_provider
]
