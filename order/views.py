from django.shortcuts import HttpResponse
from models import TrialOrder
from models import PrintOrder
from models import OrderStatus
from eprint.views import show_success
import datetime
from django import forms
from eprint import validate
from eprint.views import authenticated_view
from django.utils.html import escape
from django.template import RequestContext
from dashboard.views import get_profile_of_user


class PrintOrderForm(forms.Form):
    file = forms.FileField()
    color = forms.CharField()
    method = forms.CharField()


class TrialOrderForm(forms.Form):
    name = forms.CharField()
    phone = forms.CharField()
    building = forms.CharField()
    file = forms.FileField()


def validate_print_order_form(form):
    color = form.cleaned_data['color']
    method = form.cleaned_data['method']
    up_file = form.cleaned_data['file']
    if validate.print_order_validate['filetype'](up_file.name) \
            and validate.print_order_validate['color'](str(color)) \
            and validate.print_order_validate['method'](str(method)):
        return True
    return False


@authenticated_view
def print_order(request):
    if request.method == "POST":
        user_profile = get_profile_of_user(request.user)
        if not user_profile or not user_profile.can_use():
            return show_success('Finish your profile', '/dashboard', RequestContext(request))
        order_form = PrintOrderForm(request.POST, request.FILES)
        if order_form.is_valid() and validate_print_order_form(order_form):
            user = request.user
            new_print_order = PrintOrder()

            new_print_order.user = user
            new_print_order.up_file = order_form.cleaned_data['file']
            new_print_order.time = datetime.datetime.now()
            new_print_order.status = OrderStatus.STATUS_UPLOADED

            new_print_order.color = order_form.cleaned_data['color']
            new_print_order.method = order_form.cleaned_data['method']

            new_print_order.save()
            return show_success('upload ok', 'dashboard', RequestContext(request))
    return show_success('upload fail', 'dashboard', RequestContext(request))


def validate_trail_order_form(trial_form):
    name = trial_form.cleaned_data['name']
    phone = trial_form.cleaned_data['phone']
    building = trial_form.cleaned_data['building']
    file = trial_form.cleaned_data['file']
    if validate.trial_order_validate['name'](name) and validate.trial_order_validate['phone'](phone) \
            and validate.trial_order_validate['building'](building) \
            and validate.trial_order_validate['filetype'](file.name):
        return True
    return False


def trial_order(request):
    if request.method == "POST":
        trial_form = TrialOrderForm(request.POST, request.FILES)

        if trial_form.is_valid() and validate_trail_order_form(trial_form):

            phone = trial_form.cleaned_data['phone']

            if TrialOrder.is_this_phone_used(phone):
                return show_success('upload fail', '/', RequestContext(request))

            new_trial_order = TrialOrder()
            new_trial_order.name = trial_form.cleaned_data['name']
            new_trial_order.phone = trial_form.cleaned_data['phone']
            new_trial_order.building = trial_form.cleaned_data['building']
            new_trial_order.up_file = trial_form.cleaned_data['file']
            new_trial_order.status = OrderStatus.STATUS_UPLOADED

            new_trial_order.save()
            return show_success('Upload ok', 'register')

    return show_success('upload fail', '/', RequestContext(request))
