from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from book.forms import BookStroreForm
from book.models import BookStoreModel
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
# Create your views here.
# def home(request):
#       return render(request, "store_book.html")

class MyTemplateView(TemplateView):
      template_name = 'home.html'
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context ={'name' : 'Tushar','age':23}
            context.update(kwargs)
            return context
      
# def store_book(request):
#       if request.method == 'POST':
#             book = BookStroreForm(request.POST)
#             if book.is_valid():
#                   book.save()
#                   print(book.cleaned_data)
#                   return redirect("show_books")     
#       else:
#             book=BookStroreForm()
#       return render(request, 'store_book.html', {'form' :book})

# class BookFormView(FormView):
#       template_name = 'store_book.html'
#       form_class = BookStroreForm
#       # success_url = reverse_lazy('show_books')
#       def form_valid(self,form):
#             print(form.cleaned_data)
#             form.save()
#             return redirect("show_books") 

class BookFormView(CreateView):
      model = BookStoreModel
      template_name = 'store_book.html'
      form_class = BookStroreForm
      success_url = reverse_lazy('show_books')

# def show_books(request):
#       book = BookStoreModel.objects.all()
#       print(book)
#       return render(request,'show_book.html', {'data' : book})

class BookListView(ListView):
      model = BookStoreModel
      template_name ='show_book.html'
      context_object_name = 'data'
      # def get_queryset(self):
      #       return BookStoreModel.objects.filter(id='4')
      # ordering=['-id']
      
class BookDetailView(DetailView):
      model = BookStoreModel
      template_name ='book_details.html'
      context_object_name = 'item'
      pk_url_kwarg ='id'

def edit_book(request,id):
      book=BookStoreModel.objects.get(pk =id)
      form=BookStroreForm(instance=book)
      if request.method == 'POST':
            form = BookStroreForm(request.POST,instance=book)
            if form.is_valid():
                   form.save()
                   return redirect("show_books")     
      return render(request, 'store_book.html', {'form' :form})
class BookUpdateView(UpdateView):
      model = BookStoreModel
      template_name = 'store_book.html'
      form_class = BookStroreForm
      success_url = reverse_lazy('show_books')
      
class BookDeleteView(DeleteView):
      model = BookStoreModel
      template_name= 'delete_confirmation.html'
      success_url = reverse_lazy('show_books')
      
# def delete_book(request,id):
#       book = BookStoreModel.objects.get(pk =id).delete()
#       return redirect("show_books")
      
