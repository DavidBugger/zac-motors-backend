from django.shortcuts import render

def home(request):
    return render(request, 'frontend/home.html')


def about(request):
    return render(request, 'frontend/about.html')


def contact(request):
    return render(request, 'frontend/contact.html')

def buy(request):
    return render(request, 'frontend/buy.html')

def dealership(request):
    return render(request, 'frontend/dealerships.html')

def showroom(request):
    return render(request, 'frontend/showroom.html')





def brands(request):
    cars_slider = [
        {"name": "Mercedes Benz", "image": "cars/img/mercedes-47.jpg"},
        {"name": "Honda Accord", "image": "cars/img/accord.jpg"},
        {"name": "Toyota Camry", "image": "cars/img/camry.jpg"},
        {"name": "BMW", "image": "cars/img/main-car1.jpg"},
    ]

    cars = [
        {
            "name": "Mercedes Benz 4Matic C300",
            "mileage": "20,360 mi",
            "transmission": "Automatic",
            "fuel": "Petrol",
            "color": "Black",
            "year": 2023,
            "price": "49,950.00",
            "image": "cars/img/benz c300.jpg",
            "slug": "benz-c300",
        },
        {
            "name": "Honda Accord",
            "mileage": "20,360 mi",
            "transmission": "Automatic",
            "fuel": "Petrol",
            "color": "Grey",
            "year": 2024,
            "price": "49,950.00",
            "image": "cars/img/accord.jpg",
            "slug": "accord-2024",
        },
        {
            "name": "Toyota Camry SE",
            "mileage": "20,360 mi",
            "transmission": "Automatic",
            "fuel": "Petrol",
            "color": "Blue",
            "year": 2022,
            "price": "49,950.00",
            "image": "cars/img/camry.jpg",
            "slug": "camry-2022",
        },
    ]
    return render(request, "cars/brands.html", {"cars": cars, "cars_slider": cars_slider})
