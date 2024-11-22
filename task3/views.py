from django.shortcuts import render, redirect


def home(request):
    return render(request, 'third_task/home.html')


def store(request):
    items = {
        "item1": "Игровая консоль",
        "item2": "Игровая мышь",
        "item3": "Игровая клавиатура",
    }
    return render(request, 'third_task/store.html', {'items': items})


def cart(request):
    return render(request, 'third_task/cart.html')
