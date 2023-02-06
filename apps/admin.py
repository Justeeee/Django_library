from django.contrib import admin

from apps.models import Book, Subject, Writer, Publisher

# Register your models here.
admin.site.register(Book)
admin.site.register(Subject)
admin.site.register(Writer)
admin.site.register(Publisher)