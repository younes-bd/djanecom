from io import BytesIO
from celery import task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

@task
def payment_completed(request, order_id):
    """ Task to send an e-mail notification when an order is successfully created. """
    user = request.user
    order = Order.objects.get(_id=order_id)

    # create invoice e-mail
    subject = f'My Shop - EE Invoice no. {order._id}'
    message = 'Please, find attached the invoice for your recent purchase.'
    email = EmailMessage(subject, message, 'youyouyounes77@gmail.com', [user.email])


    """# generate PDF
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)"""

    #generate PDF
    template_path = 'orders/order/pdf.html'
    #context = {'order': 'this is your template context'}
    context = {'order': order}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download:
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display
    response['Content-Disposition'] = f'filename="order_{order._id}.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    out = BytesIO()
    # create a pdf
    pisa_status = pisa.CreatePDF(html,  dest=response)
    # if error then show some funy view
    if pisa_status.err:
      return HttpResponse('We had some errors <pre>' + html + '</pre>')

    # attach PDF file
    email.attach(f'order_{order._id}.pdf', out.getvalue(), 'application/pdf')
    # send e-mail
    email.send()
