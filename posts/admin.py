from django.contrib import admin
from .models import blog,Author,Entry
admin.site.register(blog)
admin.site.register(Author)
admin.site.register(Entry)
