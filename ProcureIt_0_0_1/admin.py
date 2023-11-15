from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Vendors)
admin.site.register(PurchaseOrders)
admin.site.register(GoodsReceivedNotes)
admin.site.register(PurchaseOrderItems)
admin.site.register(GRNItems)