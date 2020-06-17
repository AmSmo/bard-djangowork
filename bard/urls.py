from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import madlibs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', madlibs.views.home,  name="home"),
    path('marlib/', madlibs.views.marlib, name="marlib"),
    path(r'sonnet/<int:id>', madlibs.views.sonnet, name="sonnet"),
    path('play/', madlibs.views.play, name="play"),
    path('play/answer/', madlibs.views.answer, name="answer"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
