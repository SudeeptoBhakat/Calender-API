from django.http import JsonResponse
import calendar

def get_calendar(request, year):
    try:
        year = int(year)
    except ValueError:
        return JsonResponse({'error': 'Invalid year'}, status=400)

    if year < 1:
        return JsonResponse({'error': 'Invalid year'}, status=400)

    calendar_data = {}
    for month in range(1, 13):
        month_name = calendar.month_name[month]
        month_days = list(range(1, calendar.monthrange(year, month)[1] + 1))
        calendar_data[month_name] = month_days

    response_data = {str(year): calendar_data}

    return JsonResponse(response_data)
