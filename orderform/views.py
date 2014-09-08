# ~*~ coding: utf-8 ~*~
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.shortcuts import render

from models import *


from django.core.mail import send_mail, EmailMessage
from datetime import date
from datetime import datetime

from django.core.mail import EmailMultiAlternatives
from django.utils.translation import ugettext_lazy as _


def order(request):
    message=""
    br = "</br>"
    #name = request.POST.get('name','utf-8')
    #contact = request.POST.get('contact','utf-8')
    #email = request.POST.get('email','')
    email = "123"
    #sourcelang = request.POST.get('sourcelang','')
    #resultlang = request.POST.get('resultlang','')
    #comments = request.POST.get('comments','utf-8')
    d = date.today()
    #html = email+br+"<b>Name:</b>"+name+br+"Kontakt:"+contact+br+"sourcelang+">"+resultlang"+br+"Comments:"+comments+br
    # datetime.combine(d, datetime.min.time())name = request.POST.get('name', '')

    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            #form.save()
            name = form.cleaned_data['name']
            contact = form.cleaned_data['contact']
            comments = form.cleaned_data['comments']
            #attach = request.FILES['file']
            html="<b>Имя:</b>"+name+"</br>"+"<b>Контакты:</b>"+contact+"</br>"+comments
            subject, from_email, to = 'Barkalov Anton', 'volant247@gmail.com', 'barkalov_anton@mail.ru'
            msg = EmailMultiAlternatives(subject, html, from_email, [to])
            #try:
                #msg.attach(attach.name, attach.read(), attach.content_type)
            #except:
                #return "Attachment error"
            msg.attach_alternative(html, "text/html")
            #msg.content_subtype = "html"
            msg.send()

            message = _("Спасибо, ваш запрос доставлен.")
            form = EmailForm()
    else:
        form = EmailForm()
    return render(request, 'order.html', {
        'form': form,
        'message': message,
    })


