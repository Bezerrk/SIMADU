from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html')

def map_view(request):
    return render(request, 'map.html')

def ocurrences_view(request):
    return render(request, 'ocurrences.html')

def alerts_view(request):
    return render(request, 'alerts.html')

def reports_view(request):
    return render(request, 'reports.html')