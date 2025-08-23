from django.shortcuts import render

# Create your views here.

def add_student(request):
    return render(request, 'students/add_student.html')






def student_list(request):
    return render(request, 'students/student_list.html')




def edit_student(request):
    return render(request, 'students/edit_student.html')



def view_student(request):
    return render(request, 'students/student_details.html')