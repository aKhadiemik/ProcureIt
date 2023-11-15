from django.shortcuts import render, redirect,get_object_or_404
from ProcureIt_0_0_1.models import *
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import *
import os, time, copy
from datetime import datetime, timezone

asctime = time.asctime()
parts = asctime.split()
year = parts[4]

# Read Data, Todo: Addition of fields to help in searching for specific fields
def get_vendordetails(request, id):
    vendor = Vendors.objects.filter(vendorid=id)
    title = 'Vendor Details'
    pagetitle = 'Suppliers Directory'
    template_data = get_template('getvendors.html')
    html = template_data.render({'title': title,
                                'pagetitle': pagetitle, 'year' : year,
                                'vendor': vendor})
    return HttpResponse(html)

def get_vendors(request):
    vendors = Vendors.objects.all()
    title = 'Vendors'
    title1 = 'Suppliers'
    titleleft = 'Suppliers Directory'
    template_data = get_template('getvendors.html')
    html = template_data.render({'title': title, 'title1': title1,
                                'titleleft': titleleft, 'year' : year,
                                'vendors': vendors})
    return HttpResponse(html)

def get_purchaseorders(request):
    purchaseorders = PurchaseOrders.objects.all()
    title = 'Purchase Orders'
    pagetitle = 'Purchase Orders'
    template_data = get_template('getpurchaseorders.html')
    html = template_data.render({'title': title,
                                'pagetitle': pagetitle, 'year' : year,
                                'purchaseorders': purchaseorders})
    return HttpResponse(html)

def get_purchaseorderdetails(request, id):
    po_details = PurchaseOrderItems.objects.filter(purchase_order_id__orderid=id)
    title = 'PO Details'
    pagetitle = 'PO Details'

    #view_url = reverse('get_podetails/<int:id>', args=[id])

    template_data = get_template('getpurchaseorderdetails.html')
    html = template_data.render({'title': title,
                                'pagetitle': pagetitle, 'year' : year,
                                'po_details': po_details})
    return HttpResponse(html)

def get_grns(request):
    grns = GoodsReceivedNotes.objects.all()
    title = 'Goods Received Notes'
    pagetitle = 'Goods Received Notes'
    template_data = get_template('getgrns.html')
    html = template_data.render({'title': title,
                                'pagetitle': pagetitle, 'year' : year,
                                'grns': grns})
    return HttpResponse(html)

def get_grndetails(request, id):
    grn_details = GRNItems.objects.filter(grn_id__grnid=id)
    title = 'GRN Details'
    pagetitle = 'GRN Details'
    template_data = get_template('getgrndetails.html')
    html = template_data.render({'title': title,
                                'pagetitle': pagetitle, 'year' : year,
                                'grn_details': grn_details})
    return HttpResponse(html)

# ViewRequestContext
class ViewRequestContext(RequestContext):
    def __init__(self, request, dict=None, processors=None, META=None):
        super().__init__(request, dict, processors)
        self.META = META

# Create and Update Views
def update_vendordetails(request, id):
    vendor = Vendors.objects.get(vendorid=id).update()
    title = 'Vendor Details'
    pagetitle = 'Suppliers Directory'
    template_data = get_template('getvendors.html')
    html = template_data.render({'title': title,
                                'pagetitle': pagetitle, 'year' : year,
                                'vendor': vendor})
    return HttpResponse(html)

def add_vendor(request):
    vendor = Vendors.objects.create(vendor_name="", contact_email="", contact_name="", contact_phone="")
    title = 'Vendors'
    title1 = 'Suppliers'
    titleleft = 'Suppliers Directory'
    template_data = get_template('getvendors.html')
    html = template_data.render({'title': title, 'title1': title1,
                               
                                'titleleft': titleleft, 'year' : year,
                                'vendors': vendors})
    return HttpResponse(html)

@csrf_protect
def create_purchaseorder(request):

    vendorid_id=request.POST.get('vendorid_id')
    totalamount=request.POST.get('totalamount')
    status=request.POST.get('status')
    orderdate=request.POST.get('orderdate')
    
    purchaseorder = None

    if vendorid_id is not None and totalamount is not None and status is not None:
        last_purchase_order = PurchaseOrders.objects.latest('orderid')
        last_purchase_order_no = last_purchase_order.ordernumber
        ordernumber = last_purchase_order_no + 1
        orderdate = datetime.strptime(orderdate, '%Y-%m-%d')
        #orderdate = datetime.utcnow()

        purchaseorder = PurchaseOrders.objects.create(
            ordernumber=ordernumber,
            orderdate=orderdate,
            vendorid_id=vendorid_id,
            totalamount=totalamount,
            status=status,
        )

        #return render(request, 'purchaseorder_created.html', {'purchaseorder': purchaseorder})
        return redirect('get_purchaseorders')

    title = 'Purchase Orders'
    pagetitle = 'Purchase Orders'
    template = 'createpurchaseorder.html'
    context = ViewRequestContext(request, {'title': title, 'year': year, 'purchaseorder': purchaseorder}, META=request.META)
    return render(context, template)

@csrf_protect
def add_poitem(request, id):
    purch_ord = PurchaseOrders.objects.get(orderid=id)
    ordernumber = purch_ord.ordernumber
    orderid = purch_ord.orderid

    po_item_id=request.POST.get('po_item_id')
    item_name=request.POST.get('item_name')
    quantity=request.POST.get('quantity')
    unit_price=request.POST.get('unit_price')

    if quantity is not None:
        quantity = float(quantity)
    else:
        quantity = 0

    if unit_price is not None:
        unit_price = float(unit_price)
    else:
        unit_price = 0

    total_price = float(quantity) * float(unit_price)

    po_details = None

    if po_details is not None:
        last_po_item = PurchaseOrderItems.objects.latest('po_item_id')
        last_po_item_id = last_po_item.po_item_id
        po_item_id = last_po_item_id + 1

        po_details = PurchaseOrderItems.objects.create(
            po_item_id=po_item_id,
            item_name=item_name,
            quantity=quantity,
            unit_price=unit_price,
            total_price=total_price,
        )
        return redirect('get_podetails')

    title = 'PO Details'
    pagetitle = 'PO Details'
    template = 'createpoitem.html'
    context = ViewRequestContext(request, {'title': title, 'year': year, 'po_details': po_details, 'purch_ord': purch_ord, 'orderid': orderid}, META=request.META)
    return render(context, template)

@csrf_protect
def create_grn(request):

    deliverynotenumber=request.POST.get('deliverynotenumber')
    supplierinvoicenumber=request.POST.get('supplierinvoicenumber')
    receivedby=request.POST.get('receivedby')
    orderedqty=request.POST.get('orderedqty')
    receivedqty=request.POST.get('receivedqty')
    status=request.POST.get('status')
    poid_id=request.POST.get('poid_id')
    grndate=request.POST.get('grndate')
    
    grn = None

    if poid_id is not None and status is not None:
        last_grn = GoodsReceivedNotes.objects.latest('grnid')
        last_grn_no = last_grn.grnnumber
        grnnumber = last_grn_no + 1
        grndate = datetime.strptime(grndate, '%Y-%m-%d')
        #grndate = datetime.utcnow()

        grn = GoodsReceivedNotes.objects.create(
            grnnumber=grnnumber,
            deliverynotenumber=deliverynotenumber,
            supplierinvoicenumber=supplierinvoicenumber,
            receivedby=receivedby,
            orderedqty=orderedqty,
            receivedqty=receivedqty,
            status=status,
            poid_id=poid_id,
            grndate=grndate,
        )
        
        return redirect('get_grns')

    title = 'Goods Received Notes'
    pagetitle = 'Goods Received Notes'
    template = 'creategrn.html'
    context = ViewRequestContext(request, {'title': title, 'year': year, 'grn': grn}, META=request.META)
    return render(context, template)

def add_grndetails(request, id):
    grn_details = GRNItems.objects.filter(grnid__grnid=id)
    title = 'GRN Details'
    pagetitle = 'GRN Details'
    template_data = get_template('getgrndetails.html')
    html = template_data.render({'title': title,
                                'pagetitle': pagetitle, 'year' : year,
                                'grn_details': grn_details})
    return HttpResponse(html)

# Todo: Addition of cases where different fields are updated
@csrf_protect
def update_grn(request, id):
    grn = GoodsReceivedNotes.objects.get(pk=id)
    curr_grn = copy.deepcopy(grn)
    
    if request.method == 'POST':
        if 'deliverynotenumber' in request.POST:
            new_deliverynotenumber = grn.deliverynotenumber = request.POST.get('deliverynotenumber')
            if new_deliverynotenumber:
                grn.deliverynotenumber = new_deliverynotenumber
            else:
                grn.deliverynotenumber = curr_grn.deliverynotenumber
        
        if 'supplierinvoicenumber' in request.POST:
            new_invoicenumber = grn.supplierinvoicenumber = request.POST['supplierinvoicenumber']
            if new_invoicenumber:
                grn.supplierinvoicenumber = new_invoicenumber
            else:
                grn.supplierinvoicenumber = curr_grn.supplierinvoicenumber

        if 'grndate' in request.POST:
            raw_date = request.POST.get('grndate')
            if raw_date:
                grn.grndate = datetime.strptime(raw_date, '%Y-%m-%d')
        else:
            raw_date = curr_grn.grndate
            grn.grndate = datetime.strptime(raw_date, '%Y-%m-%d %H:%M:%S')

        grn.save()

        #return redirect('get_grns')

    title = 'GRN Details'
    pagetitle = 'GRN Details'
    template = 'updategrn.html'
    context = ViewRequestContext(request, {'title': title, 'year': year, 'grn': grn}, META=request.META)
    return render(context, template)

@csrf_protect
def update_grndetails(request, id):
    grn_details = GRNItems.objects.filter(grnitemid=id)

    if request.method == 'POST':
        #print(pprint.pprint(request.POST))
        
        if 'orderedqty' in request.POST:
            grn_details.orderedqty = request.POST['orderedqty']
        if 'receivedqty' in request.POST:
            grn_details.receivedqty = request.POST['receivedqty']
        if 'unit_price' in request.POST:
            grn_details.unit_price = request.POST['unit_price']
        
        grn_details.save()

        # from django.db import transactions
        # transaction.commit()

        return redirect('update_grndetails', grnitemid=id)

    title = 'GRN Details'
    pagetitle = 'GRN Details'
    template = 'updategrndetails.html'
    context = ViewRequestContext(request, {'title': title, 'year': year, 'grn_details': grn_details}, META=request.META)
    return render(context, template)

def update_purchaseorder(request, id):
    grns = GoodsReceivedNotes.objects.get(poid_id=id).update()
    title = 'Goods Received Notes'
    pagetitle = 'Goods Received Notes'
    template_data = get_template('getgrns.html')
    html = template_data.render({'title': title,
                                'pagetitle': pagetitle, 'year' : year,
                                'grns': grns})
    return HttpResponse(html)

def update_purchaseorderdetails(request, id):
    po_details = PurchaseOrderItems.objects.get(po_item_id=id)

    po_item_id=request.POST.get('po_item_id')
    item_name=request.POST.get('item_name')
    quantity=request.POST.get('quantity')
    unit_price=request.POST.get('unit_price')
    total_price = quantity * unit_price

    po_details = None

    if purchase_order_id is not None:
        last_po_item = PurchaseOrderItems.objects.latest('po_item_id')
        last_po_item_id = last_po_item.po_item_id
        po_item_id = last_po_item_id + 1

        po_details = PurchaseOrderItems.objects.create(
            po_item_id=po_item_id,
            item_name=item_name,
            quantity=quantity,
            unit_price=unit_price,
            total_price=total_price,
        )
        return redirect('get_purchaseorderdetails')

    title = 'Update PO Details'
    pagetitle = 'Update PO Details'
    template = 'updatepurchaseorderdetails.html'
    context = ViewRequestContext(request, {'title': title, 'year': year, 'po_details': po_details}, META=request.META)
    return render(context, template)


    template_data = get_template('getgrndetails.html')
    html = template_data.render({'title': title,
                                'pagetitle': pagetitle, 'year' : year,
                                'grn_details': grn_details})
    return HttpResponse(html)

# Delete views
def delete_grnitem(request, id):
    grnitem = GRNItems.objects.get(grnitemid=id)
    grnitem.delete()
    title = 'Goods Received Notes'
    pagetitle = 'Goods Received Notes'
    template_data = get_template('deletegrndetails.html')
    html = template_data.render({'title': title,
                                'pagetitle': pagetitle, 'year' : year,
                                'grnitem': grnitem})
    return HttpResponse(html)

def delete_purchaseorderitem(request, id):
    po_item = get_object_or_404(PurchaseOrderItems, pk=id)
    po_item.delete()
    #po_item = PurchaseOrderItems.objects.get(pk=id).delete()
    title = 'Purchase Order Details'
    pagetitle = 'PO Details'
    template_data = get_template('deletepoitem.html')
    html = template_data.render({'title': title, 'pagetitle': pagetitle,
                                'year' : year,
                                'po_item': po_item})
    return HttpResponse(html)