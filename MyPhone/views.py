from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from MyPhone.forms import PhoneCreateForm
from MyPhone.models import Phone


def main(request):
    phones = Phone.objects.all()
    context = {
        'phones': phones
    }
    return render(request, 'main.html', context)


class PhoneCreateView(generic.CreateView):
    template_name = 'create.html'
    form_class = PhoneCreateForm
    model = Phone

    def get_success_url(self):
        return reverse('main')


class UpdatePhoneView(generic.UpdateView):
    template_name = 'update.html'
    form_class = PhoneCreateForm
    model = Phone
    context_object_name = 'phone'

    def get_success_url(self):
        return reverse('main')
