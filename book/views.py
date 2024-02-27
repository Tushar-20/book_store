from django.shortcuts import render
from book.forms import BookStroreForm

# Create your views here.
def home(request):
      return render(request, "store_book.html")

def store_book(request):
      book=BookStroreForm
      return render(request, 'store_book.html',{'form' :book})