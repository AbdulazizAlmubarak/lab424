from django.shortcuts import render
from django.http import HttpResponse

# Tax rate stored as a variable (15%)
tax_rate = 0.15


def home(request):
    """Default path: shows a simple page describing the site."""
    return render(request, 'tax_app/home.html')


def calculate_tax(request, price):
    """Takes a number and calculates the total price after applying tax."""
    tax_amount = price * tax_rate
    total_price = price + tax_amount
    context = {
        'original_price': price,
        'tax_rate_percent': tax_rate * 100,
        'tax_amount': round(tax_amount, 2),
        'total_price': round(total_price, 2),
    }
    return render(request, 'tax_app/calculate.html', context)


def tax_rate_view(request):
    """Displays the current tax rate in a header element."""
    context = {
        'tax_rate_percent': tax_rate * 100,
    }
    return render(request, 'tax_app/taxrate.html', context)
