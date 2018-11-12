from django.contrib import admin

# Register your models here.
from .models import Question, Product, Part, PartsInProduct, Supplier

admin.site.register(Question)
admin.site.register(Product)
admin.site.register(Part)
admin.site.register(PartsInProduct)
admin.site.register(Supplier)

