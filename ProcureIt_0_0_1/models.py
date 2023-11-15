from django.db import models
from django.db.models.fields import Field
from django.db.models import Model

class Vendors(models.Model):
    class Meta:
        db_table = "vendors"
    vendorid = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=128, help_text="")
    contact_name = models.CharField(max_length=128)
    contact_email = models.EmailField(max_length=128, null=True, blank=True)
    contact_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.vendor_name

class PurchaseOrders(models.Model):
    class Meta:
        db_table = "purchaseorders"
    orderid = models.AutoField(primary_key=True)
    ordernumber = models.IntegerField(unique=True)
    orderdate = models.DateTimeField(auto_now_add=True)
    vendorid = models.ForeignKey(Vendors, on_delete=models.CASCADE, default=0)
    totalamount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=256)

    def __str__(self):
        return f"Purchase Order {self.ordernumber}"

"""     
    class PurchaseOrderStatus(models.TextChoices):
        DRAFT = "DRAFT", "Draft"
        PENDING = "PENDING", "Pending"
        APPROVED = "APPROVED", "Approved"
        COMPLETED = "COMPLETED", "Completed"
    role = models.CharField (verbose_name= "The role this contributor had in the book.",
                                choices=PurchaseOrderStatus.choices, max_length=20) """


class PurchaseOrderItems(models.Model):
    class Meta:
        db_table = "po_items"
    purchase_order = models.ForeignKey('PurchaseOrders', on_delete=models.CASCADE)
    po_item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=128)
    quantity = models.IntegerField(null=False)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"PO Item {self.po_item_id}"

class GoodsReceivedNotes(models.Model):
    class Meta:
        db_table = "gr_notes"
    grnid = models.AutoField(primary_key=True)
    poid = models.ForeignKey('PurchaseOrders', on_delete=models.CASCADE)
    grnnumber = models.IntegerField(unique=True)
    grndate = models.DateTimeField(auto_now_add=True)
    deliverynotenumber = models.CharField(max_length=25)
    supplierinvoicenumber = models.CharField(max_length=25)
    receivedby = models.CharField(max_length=256)
    orderedqty = models.IntegerField(default=0)
    receivedqty = models.IntegerField(default=0)
    status = models.CharField(max_length=25)

    def __str__(self):
        return f"GRN {self.grnnumber}"

from django.db import models

class GRNItems(models.Model):
    class Meta:
        db_table = "grnitems"
    grn = models.ForeignKey('GoodsReceivedNotes', on_delete=models.CASCADE)
    grnitemid = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=128)
    orderedqty = models.IntegerField(null=False)
    receivedqty = models.IntegerField(null=False, default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"GRN Item {self.grnitemid}"
