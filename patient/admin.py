from django.contrib import admin
from .models import Tweet, Patient, Document, TestResult, Label, Category
# Register your models here.

admin.site.register(Tweet)
admin.site.register(Patient)
admin.site.register(Document)
admin.site.register(TestResult)
admin.site.register(Label)
admin.site.register(Category)