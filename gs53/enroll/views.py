from django.shortcuts import render

# Create your views here.
# def show_details(request, my_id):
#     #print(my_id)
#     student = {'id':my_id}
#     return render(request, 'enroll/show.html', student )

def home(request, check):
    return render(request, 'enroll/home.html', {'ch':check})

def show_details(request, my_id=1):
    if my_id == 1:
     student = {'id':my_id, 'name':'Rohan'}
    if my_id == 2:
     student = {'id':my_id, 'name':'Shreyash'}
    if my_id == 3:
     student = {'id':my_id, 'name':'Saikiran'}
    return render(request, 'enroll/show.html', student )
 
def show_sdetails(request, my_id, my_sid):
    if my_id == 1 and my_sid == 5:
     student = {'id':my_id, 'name':'Rohan', 'info':'Sub Details'}
    if my_id == 2 and my_sid == 6:
     student = {'id':my_id, 'name':'Shreyash', 'info':'Sub Details'}
    if my_id == 3 and my_sid == 7:
     student = {'id':my_id, 'name':'Saikiran', 'info':'Sub Details'}
    return render(request, 'enroll/show.html', student )