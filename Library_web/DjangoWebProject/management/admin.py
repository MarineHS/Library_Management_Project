from django.contrib import admin
from .models import BorrowBook
from Catalog.models import Book
from django.contrib import messages
from django.core.exceptions import ValidationError

# Register your models here.
@admin.register(BorrowBook)
class BorrowBookAdmin(admin.ModelAdmin):
    actions = None

    # Define an action to mark books as returned
    def mark_as_returned(self, request, queryset):
        for borrow in queryset:
            borrow.isbn.available = True
            borrow.isbn.save()
            borrow.delete()
        self.message_user(request, "Selected book(s) marked as returned.")

    mark_as_returned.short_description = "Mark selected as Returned"


    def save_model(self, request, obj, form, change):
        if not change:  # New book borrowed
            if not obj.isbn.available:
                self.message_user(request, "This book is not available.", level=messages.ERROR)
                return  # Do not save
            else:
                obj.isbn.available = False
                obj.isbn.save()
                super().save_model(request, obj, form, change)
                # Book succesfully borrowed
                self.message_user(request, f"The book \"{obj.isbn}\" was borrowed by {obj.user}.", level=messages.SUCCESS)
        else:
            super().save_model(request, obj, form, change)
    
    # Remove automatic pop up
    def response_add(self, request, obj, post_url_continue=None):
        return self.response_post_save_add(request, obj)

    list_display = ('isbn', 'user', 'borrow_date', 'return_date')
    autocomplete_fields = ('isbn', 'user')
    actions = [mark_as_returned]  
