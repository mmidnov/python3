# okurmen/views.py
from audioop import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .models import Teacher, Group, Student,Manager
from django.http import FileResponse, HttpResponse
from django.utils.translation import activate, gettext_lazy as _
from .utils import generate_receipt

def home(request):
    return render(request, 'home.html')

def managers(request):
    managers_data = Manager.objects.all()
    return render(request, 'managers.html', {'managers_data':managers_data})

def teachers(request):
    teachers_data = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers_data': teachers_data})

def groups(request):
    groups_data = Group.objects.all()
    return render(request, 'groups.html', {'groups_data': groups_data})

def students(request):
    students_data = Student.objects.all()
    return render(request, 'students.html', {'students_data': students_data})

def student_details(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST' and 'download_receipt' in request.POST:
        # Generate receipt PDF
        pdf_buffer = generate_receipt(student)

        # Create a response with PDF content
        response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={student.name}_receipt.pdf'
        return response

    return render(request, 'student_details.html', {'student': student})

def managers_details(request, manager_id):
    manager = get_object_or_404(Manager, pk=manager_id)
    return render(request, 'manager_details.html', {'manager': manager})



# def translate(request):
#     translation = None
#     if request.method == 'POST':
#         original_text = request.POST.get('original_text', '')
#         # Perform translation (you can use any translation service or library)
#         # For simplicity, we'll just reverse the text.
#         translation = original_text[::-1]

#     return render(request, 'home.html', {'translation': translation})

def set_language(request):
    # Get the language from the query parameter or default to 'en'
    language = request.GET.get('language', 'en')
    
    # Activate the selected language
    activate(language)

    # Get the referring page from the 'HTTP_REFERER' header
    referring_page = request.META.get('HTTP_REFERER', None)

    # If referring page is available, redirect to it; otherwise, redirect to a specific page
    if referring_page:
        return redirect(referring_page)
    else:
        # If referring page is not available, redirect to a specific URL
        # For example, you can redirect to the home page
        return redirect(reverse('home'))
    
class DownloadReceiptView(View):
    def post(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        # Assuming the receipt file field is named 'payment_receipt'
        receipt_file = student.payment_receipt
        if receipt_file:
            response = FileResponse(receipt_file)
            response['Content-Disposition'] = f'attachment; filename="{receipt_file.name}"'
            return response
        else:
            # Handle the case when there is no receipt file
            # Redirect, show an error message, or handle it as you wish
            pass
