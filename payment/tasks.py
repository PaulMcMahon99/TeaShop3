from io import BytesIO
from celery import task
# import weasyprint - this will not work due to incompatibility
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order

# This function is never called and is part of the ongoing OS compatibility issue
# with PDF billing. 

# The decorated function to send an e-mail notification when an order is successfully created. 

# The task decorator ensures this is called as an asynchronous task
@task
def payment_completed(order_id):
    
    order = Order.objects.get(id=order_id)

    # create invoice e-mail
    subject = f'My Shop - EE Invoice no. {order.id}'
    message = 'Please, find attached the invoice for your recent purchase.'
    email = EmailMessage(subject,
                         message,
                         'admin@myshop.com',
                         [order.email])
    # generate PDF
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    # weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets) - non-functional

    # attach PDF file
    email.attach(f'order_{order.id}.pdf',
                 out.getvalue(),
                 'application/pdf')
    # send e-mail
    email.send()