from django.urls import path
from .views_front import (
    CookieCreateView,
    CookieDeleteView,
    CookieDetailView,
    CookieListView,
    CookieUpdateView,
)

urlpatterns = [
    path("", CookieListView.as_view(), name="cookie_list"),
    path("<int:pk>/", CookieDetailView.as_view(), name="cookie_detail"),
    path("create/", CookieCreateView.as_view(), name="cookie_create"),
    path("<int:pk>/update/", CookieUpdateView.as_view(), name="cookie_update"),
    path("<int:pk>/delete/", CookieDeleteView.as_view(), name="cookie_delete"),
]
