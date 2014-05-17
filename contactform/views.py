# ~*~ coding: utf-8 ~*~
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils.translation import ugettext

from models import ContactForm

def gindex(request):
    #latest_post_list = Post.objects.order_by('-name')[:8]
    #output = ', '.join([p.name for p in latest_post_list])
    #return HttpResponse(output)
    #oss = os.path.dirname(os.path.dirname(__file__))
    template = loader.get_template('contacts.html')
    context = Context(request, {
        'latest_post_list': latest_post_list,
        'oss': oss,
    })
    return HttpResponse(template.render(context))

def index(request): # наша вьюшка
    all_is_right = ''

    if request.method == 'POST': # пару проверок формы
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() # сохраняем нашу форму в базу
            all_is_right = u"Ваше сообщение успешно отправлено."
            form = ContactForm() # очищаем форму
    else:
        form = ContactForm()
    return render(request, 'contacts.html', {
        'form': form,
        'all_is_right': all_is_right,
        })
