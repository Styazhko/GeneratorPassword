import random

from django.shortcuts import render

# Create your views here.


def home(request):

    length_list = [8,
                   10,
                   12,
                   14,
                   ]

    checkbox_list = ['Верхний регистр',
                    'Цифры',
                    'Специальные символы',
                    ]

    return render(request, 'generator/home.html', {'length_list':length_list, 'checkbox_list':checkbox_list})


def password(request):

    random_password = ''

    symbol = list('qwertyuioplkjhgfdsazxcvbnm')

    if request.GET.get('Верхний регистр'):
        symbol.extend(list('QWERTYUIOPLKJHGFDSAZXCVBNM'))
    if request.GET.get('Специальные символы'):
        symbol.extend(list('!@#$%^&*()'))
    if request.GET.get('Цифры'):
        symbol.extend(list('1234567890'))

    length = int(request.GET.get('length', 8))

    for i in range(length):
        random_password += random.choice(symbol)

    return render(request, 'generator/password.html', {'password':random_password})
