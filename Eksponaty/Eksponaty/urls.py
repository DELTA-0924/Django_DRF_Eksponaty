from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from main_app.views import ListViewEks,ListViewComment

urlpatterns = [
    path('list_exhibit',ListViewEks.as_view(),name="list_exhibit"),
    path('list_comment',ListViewComment.as_view(),name="list_comment"),
    path('admin/', admin.site.urls)
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
