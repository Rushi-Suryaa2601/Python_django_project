from django.urls import path
from . import views
from vege.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.recepes, name="recepes"),
    path("delete_recepe/<id>/", views.delete_recepe, name="delete_recepe"),
    path("update_recepe/<id>/", views.update_recepe, name="update_recepe"),
    path("login/", views.login_page, name="login_page"),
    path("logout/", views.logout_page, name="logout_page"),
    path("register/", views.register_page, name="register_page"),
    path("student/", views.get_student, name="get_student"),
    path("see_marks/<student_id>", views.see_marks, name="see_marks"),
    path("send-email/", views.send_email, name="send_email"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
