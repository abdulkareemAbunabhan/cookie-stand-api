from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import CookieStand


class CookieListView(LoginRequiredMixin, ListView):
    template_name = "cookies/cookie_list.html"
    model = CookieStand
    context_object_name = "cookies"


class CookieDetailView(LoginRequiredMixin, DetailView):
    template_name = "cookies/cookie_detail.html"
    model = CookieStand


class CookieUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "cookies/cookie_update.html"
    model = CookieStand
    fields = "__all__"


class CookieCreateView(LoginRequiredMixin, CreateView):
    template_name = "cookies/cookie_create.html"
    model = CookieStand
    fields = ["name", "rating", "reviewer"] # "__all__" for all of them


class CookieDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "cookies/cookie_delete.html"
    model = CookieStand
    success_url = reverse_lazy("cookie_list")
