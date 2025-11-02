from django.urls import path

from .views import AboutPageView, HomePageView, WorkspacePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("workspace/", WorkspacePageView.as_view(), name="workspace"),
]
