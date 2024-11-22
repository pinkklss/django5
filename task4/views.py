from django.shortcuts import render


def main_page(requset):
    return render(requset, 'fourth_task/platform.html')


def store_games(requset):
    context = {'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']}
    return render(requset, 'fourth_task/games.html', context)


def cart_page(request):
    cart_items = {
        'Atomic Heart': {'price': 1000, 'quantity': 1},
        'Cyberpunk 2077': {'price': 2000, 'quantity': 1},
    }
    total = sum(item['price'] * item['quantity'] for item in cart_items.values())
    discount = 0.1 if total > 200 else 0
    final_total = total - (total * discount)
    discount_percent = discount * 100
    return render(request, 'fourth_task/cart.html', {
        'cart_items': cart_items,
        'total': total,
        'final_total': final_total,
        'discount_percent': discount_percent
    })
