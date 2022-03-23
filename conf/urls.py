from django.urls import path, include

urlpatterns = [
    path('exapp/', include('exapp.urls')),
]
