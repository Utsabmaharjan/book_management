from django.shortcuts import render, redirect
from book.models import Book
from book.form import CreateForm
from django.views.generic import ListView

# Create your views here.
def Create_form(request):
       form = CreateForm
       if request.method=='POST':
               form= CreateForm(request.POST, request.FILES)
               if form.is_valid():
                       form.save()
                       return redirect('/')
               else:
                       print(form.errors)
       context = {
        "form": form
        } 
       return render(request, 'create.html', context)   
   
   
   
class List(ListView):
      model = Book
      template_name = 'book/index.html'
      context_object_name = 'data'
