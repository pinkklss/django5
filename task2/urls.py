from django.urls import path
from .views import ClassBasedView, func_based_view

urlpatterns = [
    path('class/', ClassBasedView.as_view(), name='class_based_view'),
    path('func/', func_based_view, name='func_based_view'),]
