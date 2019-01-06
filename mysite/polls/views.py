from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.views import generic
from django.views.generic import View
from .models import *
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as django_login_view
from django.views.generic import FormView
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import decorators
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#import datetime
from django.db import connection
from datetime import datetime, timedelta
from django.views.generic import TemplateView, DetailView
import matplotlib.pyplot as plt
import threading
from tkinter import *
import math
import csv, io
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
import smtplib



# from here


class UserFormView(View):
    form_class = UserForm
    template_name = 'polls/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process from data
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            # return user objects if details are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('polls:index')

        return render(request, self.template_name, {'form': form})


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'polls/login.html'

    def form_valid(self, form):
        usuario = form.get_user()

        django_login_view(self.request, usuario)
        return redirect('polls:index')

        # return super(LoginView, self).form_valid(form)


# from .models import all  # Choice, Question, Product, Part, Unit
def logout(request):
    auth.logout(request)
    return render(request, 'polls/logout.html')


class Inventory(TemplateView):
    template_name = 'polls/inventory.html'
    context_object_name = 'all_generics'

    def get_context_data(self, *args, **kwargs):
        kaki = " "
        demands=getallPartsDemand()
        context = super(Inventory, self).get_context_data(*args, **kwargs)
        for par in Part.objects.all():
            for dem in demands:
                if(dem[0] == par):
                    today = (datetime.now()).replace(tzinfo=None)
                    lastOrder = getLatesTakenPorderWithPart(par)
                    #quantity = order 
                    if(lastOrder == None):
                        delta=0
                    else:  
                        delta = (today-lastOrder.porderDate.replace(tzinfo=None)).days
                        #delta=0
                    #nextdate = today + timedelta(days=5)
                    nextdate = today + timedelta(days=int((par.lt/30)*(math.sqrt(2*dem[1])))-int(delta))
                  
                     
                    kaki += "<td>" + par.pdes +"</td><td>" + str(par.stock) + "</td><td>" + str(math.sqrt(2*dem[1])) + "</td><td>" + str(nextdate) + "</td></tr>"  
        context['parts'] = kaki
        #context['parts'] = Part.objects.all()
        #context['date_last_order']=POrderItem.objects.filter()
        #context['parts_demand']=getallPartsDemand()
        
        
        return context


class AdminView(generic.ListView):
    template_name = 'polls/adminsite.html'
    context_object_name = 'all_orders'

    def get_queryset(self):
        return Order.objects.filter(
            Q(ifSupplied=False)
        ).order_by('-orderPick')


class IndexView(generic.ListView):
    template_name = 'polls/index.html'

    def get_queryset(self):
        request = self.request
        user_id = request.user.id
        order_list =Order.objects.filter(user=user_id).order_by('orderPick')
        order_list=order_list.reverse()[:5]
        return order_list


class OrderView(generic.ListView):
    context_object_name = 'all_generics'
    template_name = 'polls/generic_list.html'

    def get_queryset(self):
        return Order.objects.all()


"""DetailsView"""


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'polls/product_detail.html'


class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'polls/order_detail.html'


class PartDetailView(generic.DetailView):
    model = Part
    template_name = 'polls/part_detail.html'


class PipDetailView(generic.DetailView):
    model = Pip
    template_name = 'polls/pip_detail.html'


class SupplierDetailView(generic.DetailView):
    model = Supplier
    template_name = 'polls/supplier_detail.html'


class ComponentsDetailView(generic.DetailView):
    model = Components
    template_name = 'polls/components_detail.html'


class ExtrasDetailView(generic.DetailView):
    model = NewExtra
    template_name = 'polls/newextra_detail.html'


class SuppriceDetailView(generic.DetailView):
    model = SupPrice
    template_name = 'polls/supprice_detail.html'


class PorderDetailView(generic.DetailView):
    model = POrder
    template_name = 'polls/pord_detail.html'


class PorderitemDetailView(generic.DetailView):
    model = POrderItem
    template_name = 'polls/porderitem_detail.html'


"""IndexView"""


class ProductIndexView(generic.ListView):
    template_name = 'polls/product_index.html'
    context_object_name = 'all_products'

    def get_queryset(self):
        """Return the last five published questions."""
        return Product.objects.order_by('pdes')


class OrderIndexView(generic.ListView):
    template_name = 'polls/order_index.html'
    context_object_name = 'all_orders'
    paginate_by = 10
    queryset = Order.objects.all()

    def get_queryset(self):
        """Return the last five published questions."""
        return Order.objects.all()


class PartIndexView(generic.ListView):
    template_name = 'polls/part_index.html'
    context_object_name = 'all_parts'

    def get_queryset(self):
        """Return the last five published questions."""
        return Part.objects.order_by('pdes')


class PipIndexView(generic.ListView):
    template_name = 'polls/pip_index.html'
    context_object_name = 'all_pips'

    def get_queryset(self):
        """Return the last five published questions."""
        return Pip.objects.order_by('part__pdes')


class SupplierIndexView(generic.ListView):
    template_name = 'polls/supplier_index.html'
    context_object_name = 'all_suppliers'

    def get_queryset(self):
        """Return the last five published questions."""
        return Supplier.objects.all()


class ComponentsIndexView(generic.ListView):
    template_name = 'polls/components_index.html'
    context_object_name = 'all_componentss'

    def get_queryset(self):
        """Return the last five published questions."""
        return Components.objects.all()


class ExtrasIndexView(generic.ListView):
    template_name = 'polls/newextra_index.html'
    context_object_name = 'all_newextras'

    def get_queryset(self):
        """Return the last five published questions."""
        return NewExtra.objects.all()


class SuppriceIndexView(generic.ListView):
    template_name = 'polls/supprice_index.html'
    context_object_name = 'all_supprices'

    def get_queryset(self):
        """Return the last five published questions."""
        return SupPrice.objects.all()


class PorderIndexView(generic.ListView):
    template_name = 'polls/pord_index.html'
    context_object_name = 'all_porders'

    def get_queryset(self):
        """Return the last five published questions."""
        return POrder.objects.all()


class PorderitemIndexView(generic.ListView):
    template_name = 'polls/porderitem_index.html'
    context_object_name = 'all_porderitems'

    def get_queryset(self):
        """Return the last five published questions."""
        return POrderItem.objects.all()


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class ProductView(generic.ListView):
    model = Product
    context_object_name = 'all_generics'
    template_name = 'polls/generic_list.html'

    def get_queryset(self):
        return Product.objects.all()


class ProductCreate(CreateView):
    model = Product
    fields = ['pdes', 'price', 'prep']


class ProductUpdate(UpdateView):
    model = Product
    fields = ['pdes', 'price', 'prep']


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('polls:product_index')


class PartCreate(CreateView):
    model = Part
    fields = ['pdes', 'unit', 'stock', 'lt', 'sshigh', 'sslow']


class PartUpdate(UpdateView):
    model = Part
    fields = ['pdes', 'unit', 'stock', 'lt', 'sshigh', 'sslow']


class PartDelete(DeleteView):
    model = Part
    success_url = reverse_lazy('polls:part_index')


class SupplierCreate(CreateView):
    model = Supplier
    fields = ['name', 'address', 'tel', 'mail']


class SupplierUpdate(UpdateView):
    model = Supplier
    fields = ['name', 'address', 'tel', 'mail']


class SupplierDelete(DeleteView):
    model = Supplier
    success_url = reverse_lazy('polls:supplier_index')


class ComponentsCreate(CreateView):
    model = Components
    fields = ['part', 'quant', 'product']


class ComponentsUpdate(UpdateView):
    model = Components
    fields = ['part', 'quant', 'product']


class ComponentsDelete(DeleteView):
    model = Components
    success_url = reverse_lazy('polls:components_index')


class PipCreate(CreateView):
    model = Pip
    fields = ['part', 'quant', 'product']


class PipUpdate(UpdateView):
    model = Pip
    fields = ['part', 'quant', 'product']


class PipDelete(DeleteView):
    model = Pip
    success_url = reverse_lazy('polls:pip_index')


class ExtrasCreate(CreateView):
    model = NewExtra
    fields = ['extra_part', 'extra_price', 'extra_product']


class ExtrasUpdate(UpdateView):
    model = NewExtra
    fields = ['extra_part', 'extra_price', 'extra_product']


class ExtrasDelete(DeleteView):
    model = NewExtra
    success_url = reverse_lazy('polls:newextra_index')


class SuppriceCreate(CreateView):
    model = SupPrice
    fields = ['supplier', 'part', 'price']


class SuppriceUpdate(UpdateView):
    model = SupPrice
    fields = ['supplier', 'part', 'price']


class SuppriceDelete(DeleteView):
    model = SupPrice
    success_url = reverse_lazy('polls:supprice_index')


class PorderCreate(CreateView):
    model = POrder
    fields = ['supplier', 'orderStatus', 'ifSupplied']


class PorderUpdate(UpdateView):
    model = POrder
    fields = ['supplier', 'orderStatus', 'ifSupplied']


class PorderDelete(DeleteView):
    model = POrder
    success_url = reverse_lazy('polls:pord_index')


class PorderitemCreate(CreateView):
    model = POrderItem
    fields = ['porder', 'supprice', 'quant']


class PorderitemUpdate(UpdateView):
    model = POrderItem
    fields = ['porder', 'supprice', 'quant']


class PorderitemDelete(DeleteView):
    model = POrderItem
    success_url = reverse_lazy('polls:porderitem_index')


class OrderCreateAdmin(LoginRequiredMixin, CreateView):  # LoginRequiredMixin
    model = Order
    fields = ['user', 'orderPick', 'orderStatus', 'ifSupplied', 'product1',  'component1',
              'component2',  'component3',  'component4', 'component5',
              'extra1', 'extra2', 'extra3', 'extra4', 'extra5',  'product2', 'product3', 'remarks']
    """template_name = 'polls/generice_form.html'"""

    def form_valid(self, form):
        if ((form.instance.ifSupplied)==True):
            queryPr=Pip.objects.filter(product=form.instance.product1)
            for pip in queryPr:
                pip.part.stock=pip.part.stock-pip.quant
                pip.part.save()

        form.instance.user = self.request.user
        return super().form_valid(form)


class OrderUpdateAdmin(LoginRequiredMixin, UpdateView):  # LoginRequiredMixin
    model = Order
    fields = ['user', 'orderPick', 'orderStatus', 'ifSupplied', 'product1',  'component1',
              'component2',  'component3',  'component4', 'component5',
              'extra1', 'extra2', 'extra3', 'extra4', 'extra5',  'product2', 'product3', 'remarks']
    """template_name = 'polls/generice_form.html'"""
    def form_valid(self, form):
        if ((form.instance.ifSupplied)==True and Order.objects.filter(pk=form.instance.pk)):
            queryPr=Pip.objects.filter(product=form.instance.product1)

            for pip in queryPr:
                pip.part.stock=pip.part.stock-pip.quant
                pip.part.save()
        return super().form_valid(form)


class OrderDeleteAdmin(DeleteView):
    model = Order
    success_url = reverse_lazy('polls:order_index')


class OrderCreateCustomer(LoginRequiredMixin, CreateView):  # LoginRequiredMixin
    model = Order
    fields = [ 'orderPick', 'product1',  'component1',
              'component2',  'component3',  'component4', 'component5',
              'extra1', 'extra2', 'extra3', 'extra4', 'extra5', 'remarks']
    template_name = 'polls/order_costumer.html'
    def form_valid(self, form):
        print("kaki: ", form.instance.extra1)
        if(form.instance.product1.pdes in getAllProductsThatHasComponets()):
            if(form.instance.component1 == None ) or (form.instance.component2 == None): 
                form.add_error('component1', "component1 and component2 should not be empty if you want " +  form.instance.product1.pdes )
                return super().form_invalid(form)
        elif (form.instance.component1 != None ) or (form.instance.component2 != None) or (form.instance.component3 != None) or (form.instance.component4 != None) or (form.instance.component5 != None):
            form.add_error('component1', "components should be empty if no product with component was chosen")
            return super().form_invalid(form)
        
        elif(form.instance.extra1 != None):
            if(form.instance.extra1.extra_product.pdes!=form.instance.product1.pdes):
                form.add_error('extra1', "extras should be only used corresponding product" )
                return super().form_invalid(form)
        elif(form.instance.extra2 != None):
            if(form.instance.extra2.extra_product.pdes!=form.instance.product1.pdes):
                form.add_error('extra1', "extras should be only used corresponding product" )
                return super().form_invalid(form)
        elif(form.instance.extra3 != None):
            if(form.instance.extra3.extra_product.pdes!=form.instance.product1.pdes):
                form.add_error('extra1', "extras should be only used corresponding product" )
                return super().form_invalid(form)        
        elif(form.instance.extra4 != None):
            if(form.instance.extra4.extra_product.pdes!=form.instance.product1.pdes):
                form.add_error('extra1', "extras should be only used corresponding product" )
                return super().form_invalid(form) 
        elif(form.instance.extra5 != None):
            if(form.instance.extra5.extra_product.pdes!=form.instance.product1.pdes):
                form.add_error('extra1', "extras should be only used corresponding product" )
                return super().form_invalid(form) 
        if ((form.instance.ifSupplied)==True):
            queryPr=Pip.objects.filter(product=form.instance.product1)
            for pip in queryPr:
                pip.part.stock=pip.part.stock-pip.quant
                pip.part.save()
        form.instance.user=self.request.user
        return super().form_valid(form)
    

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def product_index(request):
    today = timezone.now().date()
    queryset_list = Product.objects.all()
    query = request.GET['q']
    if query:
        queryset_list = queryset_list.filter(
            Q(pdes__icontains=query) |
            Q(price__icontains=query) |
            Q(prep__icontains=query)
        ).distinct()
    else:
        queryset_list = Product.objects.all()
    paginator = Paginator(queryset_list, 10)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {"all_products": queryset, "title": "List", "page_request_var": page_request_var, "today": today, }

    return render(request, 'polls/product_index.html', context)


def part_index(request):
        today = timezone.now().date()
        queryset_lists = Part.objects.all()
        query = request.GET['q']
        if query:
            queryset_lists = queryset_lists.filter(
                Q(pdes__icontains=query) |
                Q(stock__icontains=query)
            ).distinct()
        else:
            queryset_lists = Part.objects.all()
        paginator = Paginator(queryset_lists, 10)
        page_request_var = "page"
        page = request.GET.get(page_request_var)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        context = {"all_parts": queryset, "title": "List", "page_request_var": page_request_var, "today": today, }

        return render(request, 'polls/part_index.html', context)


def components_index(request):
    today = timezone.now().date()
    queryset_lists1 = Components.objects.all()
    query = request.GET['q']
    if query:
        queryset_lists1 = queryset_lists1.filter(
            Q(part__pdes__icontains=query) |
            Q(quant__icontains=query) |
            Q(product__pdes__icontains=query)
        ).distinct()
    else:
        queryset_lists1 = Components.objects.all()
    paginator = Paginator(queryset_lists1, 10)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {"all_componentss": queryset, "title": "List", "page_request_var": page_request_var, "today": today, }

    return render(request, 'polls/components_index.html', context)


def supplier_index(request):
        today = timezone.now().date()
        queryset_list = Supplier.objects.all()
        query = request.GET['q']
        if query:
            queryset_list = queryset_list.filter(
                Q(address__icontains=query) |
                Q(name__icontains=query) |
                Q(mail__icontains=query)
            ).distinct()
        else:
            queryset_list = Supplier.objects.all()
        paginator = Paginator(queryset_list, 10)
        page_request_var = "page"
        page = request.GET.get(page_request_var)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        context = {"all_suppliers": queryset, "title": "List", "page_request_var": page_request_var, "today": today, }

        return render(request, 'polls/supplier_index.html', context)


def extra_index(request):
    today = timezone.now().date()
    queryset_list2 = NewExtra.objects.all()
    query = request.GET['q']
    if query:
        queryset_list2 = queryset_list2.filter(
            Q(extra_price__icontains=query) |
            Q(extra_part__pdes__icontains=query) |
            Q(extra_product__pdes__icontains=query)
        ).distinct()
    else:
        queryset_list2 = NewExtra.objects.all()
    paginator = Paginator(queryset_list2, 10)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {"all_newextras": queryset, "title": "List", "page_request_var": page_request_var, "today": today, }

    return render(request, 'polls/newextra_index.html', context)


def order_index(request):
        today = timezone.now().date()
        queryset_list3 = Order.objects.all()
        query = request.GET['q']
        if query:
            queryset_list3 = queryset_list3.filter(
                Q(user__username__icontains=query) |
                Q(remarks__icontains=query) |
                Q(orderStatus__icontains=query)
            ).distinct()
        else:
            queryset_list3 = Order.objects.all()
        paginator = Paginator(queryset_list3, 5)
        page_request_var = "page"
        page = request.GET.get(page_request_var)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        context = {"all_orders": queryset, "title": "List", "page_request_var": page_request_var, "today": today, }

        return render(request, 'polls/order_search.html', context)


def pip_index(request):
    today = timezone.now().date()
    queryset_list4 = Pip.objects.all()
    query = request.GET['q']
    if query:
        queryset_list4 = queryset_list4.filter(
            Q(part__pdes__icontains=query) |
            Q(quant__icontains=query) |
            Q(product__pdes__icontains=query)
        ).distinct()
    else:
        queryset_list4 = Pip.objects.all()
    paginator = Paginator(queryset_list4, 10)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {"all_pips": queryset, "title": "List", "page_request_var": page_request_var, "today": today, }

    return render(request, 'polls/pip_index.html', context)


def pord_index(request):
        today = timezone.now().date()
        queryset_list4 = POrder.objects.all()
        query = request.GET['q']
        if query:
            queryset_list4 = queryset_list4.filter(
                Q(supplier__name__icontains=query) |
                Q(orderStatus__icontains=query)
            ).distinct()
        else:
            queryset_list4 = POrder.objects.all()
        paginator = Paginator(queryset_list4, 10)
        page_request_var = "page"
        page = request.GET.get(page_request_var)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        context = {"all_porders": queryset, "title": "List", "page_request_var": page_request_var, "today": today, }

        return render(request, 'polls/pord_index.html', context)


def porderitem_index(request):
    today = timezone.now().date()
    queryset_list2 = POrderItem.objects.all()
    query = request.GET['q']
    if query:
        queryset_list2 = queryset_list2.filter(
            Q(porder__supplier__name__icontains=query) |
            Q(supprice__part__pdes__icontains=query) |
            Q(quant__icontains=query)
        ).distinct()
    else:
        queryset_list2 = POrderItem.objects.all()
    paginator = Paginator(queryset_list2, 10)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {"all_porderitems": queryset, "title": "List", "page_request_var": page_request_var, "today": today, }

    return render(request, 'polls/porderitem_index.html', context)


def supprice_index(request):
        today = timezone.now().date()
        queryset_list2 = SupPrice.objects.all()
        query = request.GET['q']
        if query:
            queryset_list2 = queryset_list2.filter(
                Q(supplier__name__icontains=query) |
                Q(part__pdes__icontains=query) |
                Q(price__icontains=query)
            ).distinct()
        else:
            queryset_list2 = SupPrice.objects.all()
        paginator = Paginator(queryset_list2, 10)
        page_request_var = "page"
        page = request.GET.get(page_request_var)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        context = {"all_supprices": queryset, "title": "List", "page_request_var": page_request_var, "today": today, }

        return render(request, 'polls/supprice_index.html', context)


class QueueUpdateAdmin(LoginRequiredMixin, UpdateView):  # LoginRequiredMixin
    model = Order
    fields = ['ifSupplied']
    """template_name = 'polls/generice_form.html'"""


def queue_index(request):
    today = timezone.now().date()
    queryset_list3 = Order.objects.filter(
            Q(ifSupplied=False)
        )
    query = request.GET['q']
    if query:
        queryset_list3 = queryset_list3.filter(
            Q(user__username__contains=query) |
            Q(remarks__contains=query) |
            Q(orderStatus__contains=query)
        ).distinct()
    else:
        queryset_list3 = Order.objects.filter(
            Q(ifSupplied=False)
        )
    paginator = Paginator(queryset_list3, 10)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {"all_orders": queryset, "title": "List", "page_request_var": page_request_var, "today": today, }

    return render(request, 'polls/adminsite.html', context)


def BusyTime(request):
    context = {}
    for i in range(8, 18):
        times = Order.objects.filter(orderPick__hour=i, orderPick__gte=datetime.now() - timedelta(days=90)).count()
        hour = 'hour' + str(i)
        context.update({hour: times})
    fig = plt.figure()
    fig.suptitle('Data of orders for each hour in the last quarterly', fontsize=16)
    plt.bar(list(context.keys()), (list(context.values())))  # A bar chart
    plt.xlabel('Hour', fontsize=14)
    plt.ylabel('Orders', fontsize=14)
    plt.show()
    return render(request, 'polls/busytime.html', context)

@permission_required('admin.can_add_CSV')
def orders_upload(request):
    template = "orders_upload.html"
    prompt ={
        'order': 'order of the CSV should be user id, orderdate, orderpick, order status, remarks, ifsupplied, '
                 'product1	product2	product3	extra1	extra2	extra3	extra4	extra5,'
                 '	componen1	component2	component3	component4	component5'
   }
    if request.method == "GET":
        return render(request, 'polls/orders_upload.html', prompt)

    csv_file = request.FILES['orders']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'not a csv file')
        return render(request, 'polls/orders_upload.html', prompt)


    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    try:
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            _, created = Order.objects.update_or_create(
                user = User.objects.get(id=column[0]),
                orderDate= datetime.strptime(column[1], '%d/%m/%Y %H:%M'),
                orderPick = datetime.strptime(column[2], '%d/%m/%Y %H:%M'),
                orderStatus=column[3],
                remarks = column[4],
                ifSupplied = TRUE,
                product1 = Product.objects.get(pk=column[6]),
                product2 = Product.objects.get(pk=column[7]),
                product3 = Product.objects.get(pk=column[8]),
                extra1 = NewExtra.objects.get(Q(extra_part=column[9]),Q(extra_product=column[6])),
                extra2 = NewExtra.objects.get(Q(extra_part=column[10]),Q(extra_product=column[6])),
                extra3 = NewExtra.objects.get(Q(extra_part=column[11]),Q(extra_product=column[6])),
                extra4 = NewExtra.objects.get(Q(extra_part=column[12]),Q(extra_product=column[6])),
                extra5 = NewExtra.objects.get(Q(extra_part=column[13]),Q(extra_product=column[6])),
                component1 = Components.objects.get(part=column[14]),
                component2 = Components.objects.get(part=column[15]),
                component3 = Components.objects.get(part=column[16]),
                component4 = Components.objects.get(part=column[17]),
                component5 = Components.objects.get(part=column[18])
            )
    except ObjectDoesNotExist:
        context ={}
        return HttpResponse('Your CSV has illegal IDs.')

    return render(request, 'polls/orders_upload.html')


def getallPartsDemand():  
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    count = 0
    lis = [] 
    for par in Part.objects.all():
        for i in range(0,1):
            year = currentYear
            month=currentMonth-i-1
            if month<=0:
                year=currentYear-1
                month=12-month
            total = getNumberOfPartsUsedOnMonth(year,month,par)
            temp=[par,total]
            lis.append(temp)
    return lis


def getNumberOfPartsUsedOnMonth(year,month,par):
    total=0
    list=getListOfProuductWithPart(par)
    if(list==None):
        return total 
    for prod in list:
        total=total+(getNumberOfProductOrdersInMonth(year,month,prod)*getQuant(prod,par))
    return total

def getQuant(prod,par):
    return Pip.objects.filter(part=par,product=prod)[0].quant


def getNumberOfProductOrdersInMonth(year,month,prod):
    orderp1=Order.objects.filter(product1=prod,ifSupplied=True,orderPick__month=month,orderPick__year=year)
    orderp2=Order.objects.filter(product2=prod,ifSupplied=True,orderPick__month=month,orderPick__year=year)
    orderp3=Order.objects.filter(product3=prod,ifSupplied=True,orderPick__month=month,orderPick__year=year)
    return orderp1.count()+orderp2.count()+orderp3.count()


def getListOfProuductWithPart(par):
    
    count = 0
    qs=None
    pips=Pip.objects.filter(part=par)
    if(pips.count() > 0):
        qs=Product.objects.filter(pk=pips[0].product.pk)
    else:
        return qs
    for pip in pips:
        if(count == 0):
            count+=1
            continue
        qs=qs.union(Product.objects.filter(pk=pip.product.pk))

    return qs


def getAllPOrdersWithPart(par):
    pois = POrderItem.objects.filter(supprice__part = par)
    count = 0
    qs=None
    if(pois.count() > 0):
        qs=POrder.objects.filter(pk=pois[0].porder.pk)
    else:
        return qs
    for poi in pois:
        if(count == 0):
            count+=1
            continue
        qs=qs.union(POrder.objects.filter(pk=poi.porder.pk))
    return qs


def getLatesTakenPorderWithPart(par):
    qs = getAllPOrdersWithPart(par)
    if(qs == None):
        return None
    qs = qs.filter(ifSupplied=True).order_by('-porderDate')
    if(qs.count() == 0):
        return None
    return qs[0]

def getAllProductsThatHasComponets():
    list1=[]
    comps=Components.objects.all()
    for comp in comps:
        list1.append(comp.product.pdes)
    return list1

def getAllProductsThatHasComponets():
    list1=[]
    comps=Components.objects.all()
    for comp in comps:
        list1.append(comp.product.pdes)
    return list1

"""
    target_email = form.instance.user.email
    send_email(target_email)

def get_email():
    return form.instance.user.email
"""
def send_email():
    FROM = 'shushtushliraz@gmail.com'
    TO ='koren76@gmail.com'
    SUBJECT = 'Your order is ready to pickup!'
    TEXT = 'Thank you for buying at Shush Tush!'

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)


    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('shushtushliraz@gmail.com', 'maataroze123')
    server.sendmail(FROM, TO, message)
    server.close()
    print('successfully sent the mail')
    #this function works here, but needs to be fixed to be called from the queue update
    #TO field needs to be changed to the user's email probably like this:   form.instance.user.email