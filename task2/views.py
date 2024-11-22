from django.views import View
from django.shortcuts import render
from django.http import HttpResponse


class ClassBasedView(View):
    def get(self, request):
        return render(request, 'second_task/class_view_template.html')


def func_based_view(request):
    return render(request, 'second_task/func_view_template.html')
