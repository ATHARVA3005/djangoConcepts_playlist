from django.shortcuts import render

# Create your views here.
def fees_django(request):
    return render(request, 'fees/feesone.html', {'title': 'Python', 'cname': 'Python', 'charge':3000})