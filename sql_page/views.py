from django.shortcuts import render
from sql_page.sql_queries import SQL_1, SQL_2, SQL_3, SQL_4, SQL_5, SQL_6, SQL_7, SQL_8


def index(request):
    if request.method == 'POST':
        if 'SQL_1' in request.POST:
            input = request.POST.get('SQL_1')
            value = SQL_1(input)
        elif 'SQL_2' in request.POST:
            input = request.POST.get('SQL_2')
            value = SQL_2(input)
        elif 'SQL_3' in request.POST:
            input = request.POST.get('SQL_3')
            value = SQL_3(input)
        elif 'SQL_4' in request.POST:
            input = request.POST.get('SQL_4')
            value = SQL_4(input)
        elif 'SQL_5' in request.POST:
            input = request.POST.get('SQL_5')
            value = SQL_5(input)
        elif 'SQL_6' in request.POST:
            input = request.POST.get('SQL_6')
            value = SQL_6(input)
        elif 'SQL_7' in request.POST:
            input = request.POST.get('SQL_7')
            value = SQL_7(input)
        elif 'SQL_8' in request.POST:
            input = request.POST.get('SQL_8')
            value = SQL_8(input)
        else:
            value = None
        return render(request, 'index.html', {'value': value})
    return render(request, 'index.html')
