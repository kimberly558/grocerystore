from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def blogdetails(request):
    return render(request, 'blog-details.html')


def checkout(request):
    return render(request, 'checkout.html')


def contact(request):
    return render(request, 'contact.html')


def main(request):
    return render(request, 'main.html')


def shopdetails(request):
    return render(request, 'shop-details.html')


def shopgrid(request):
    return render(request, 'shop-grid.html')


def cart(request):
    return render(request, 'shoping-cart.html')


def blog(request):
    return render(request, 'blog.html')
