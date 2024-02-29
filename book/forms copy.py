from django import forms
from book.models import BookStoreModel
class BookStroreForm(forms.ModelForm):
      class Meta:
            model = BookStoreModel
            fields =['id','book_name','author','category']