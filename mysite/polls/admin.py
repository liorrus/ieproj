from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Question)
admin.site.register(Product)
admin.site.register(Part)
admin.site.register(Pip)
admin.site.register(Supplier)
admin.site.register(SupPrice)
admin.site.register(Order)
admin.site.register(Unit)
admin.site.register(POrder)
admin.site.register(POrderItem)

admin.site.register(NewExtra)
admin.site.register(Components)
