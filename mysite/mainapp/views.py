from django.shortcuts import render
from datetime import datetime

BORN_YEAR = 1983
BORN_MONTH = 6
BORN_DAY = 5

def index(request):
    now_date = datetime.now()
    format_date = now_date.strftime('%a %b %d %H:%M:%S UTC %Y')
    age =  now_date.year - BORN_YEAR - ((now_date.month, now_date.day) < (BORN_MONTH, BORN_DAY))
    context = {
        'page_title': 'Akmanov Ruslan',
        'formated_now_date': format_date,
        'age': age,
        'current_year': now_date.year,
    }

    return render(request, 'mainapp/index.html', context)
