from django.shortcuts import render,redirect
from book.forms import BookStroreForm
from book.models import BookStoreModel
# Create your views here.
def home(request):
      return render(request, "store_book.html")

def store_book(request):
      if request.method == 'POST':
            book = BookStroreForm(request.POST)
            if book.is_valid():
                  book.save()
                  print(book.cleaned_data)
                  return redirect("show_books")     
      else:
            book=BookStroreForm()
      return render(request, 'store_book.html', {'form' :book})
def show_books(request):
      book = BookStoreModel.objects.all()
      print(book)
      return render(request,'show_book.html', {'data' : book})

def edit_book(request,id):
      book=BookStoreModel.objects.get(pk =id)
      form=BookStroreForm(instance=book)
      if request.method == 'POST':
            form = BookStroreForm(request.POST,instance=book)
            if form.is_valid():
                   form.save()
                   redirect("show_books")     
      return render(request, 'store_book.html', {'form' :form})