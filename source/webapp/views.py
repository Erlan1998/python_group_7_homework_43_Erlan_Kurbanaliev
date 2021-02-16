from django.shortcuts import render


# Create your views here.

def calculate_view(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        print(request.POST)
        first = int(request.POST.get('First_number'))
        second = int(request.POST.get('Second_number'))
        choice = request.POST.get('choice')
        if choice == 'Add':
            message = f'{first} + {second} = {first+second}'
        elif choice == 'Subtract':
            message = f'{first} - {second} = {first - second}'
        elif choice == 'Multiply':
            message = f'{first} * {second} = {first * second}'
        elif choice == 'Divide':
            if second != 0:
                message = f'{first} : {second} = {first / second}'
            else:
                message = 'На ноль делить нельзя!!!'

        return render(request, 'home.html', {'message': message})
