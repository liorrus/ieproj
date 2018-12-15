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


class AdminView(generic.ListView):
    context_object_name = 'all_generics'
    template_name = 'polls/adminsite.html'

    def get_queryset(self):
        return Order.objects.all()


class IndexView(generic.ListView):
    template_name = 'polls/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.all()


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
        return Product.objects.all()


class OrderIndexView(generic.ListView):
    template_name = 'polls/order_index.html'
    context_object_name = 'all_orders'

    def get_queryset(self):
        """Return the last five published questions."""
        return Order.objects.order_by('-orderDate')


class PartIndexView(generic.ListView):
    template_name = 'polls/part_index.html'
    context_object_name = 'all_parts'

    def get_queryset(self):
        """Return the last five published questions."""
        return Part.objects.all()


class PipIndexView(generic.ListView):
    template_name = 'polls/pip_index.html'
    context_object_name = 'all_pips'

    def get_queryset(self):
        """Return the last five published questions."""
        return Pip.objects.all()


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
    fields = ['porder', 'part', 'quant']


class PorderitemUpdate(UpdateView):
    model = POrderItem
    fields = ['porder', 'part', 'quant']


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
        form.instance.user = self.request.user
        return super().form_valid(form)


class OrderUpdateAdmin(LoginRequiredMixin, UpdateView):  # LoginRequiredMixin
    model = Order
    fields = ['user', 'orderPick', 'orderStatus', 'ifSupplied', 'product1',  'component1',
              'component2',  'component3',  'component4', 'component5',
              'extra1', 'extra2', 'extra3', 'extra4', 'extra5',  'product2', 'product3', 'remarks']
    """template_name = 'polls/generice_form.html'"""


class OrderDeleteAdmin(DeleteView):
    model = Order
    success_url = reverse_lazy('polls:order_index')


class OrderCreateCustomer(LoginRequiredMixin, CreateView):  # LoginRequiredMixin
    model = Order
    fields = [ 'orderPick', 'product1',  'component1',
              'component2',  'component3',  'component4', 'component5',
              'extra1', 'extra2', 'extra3', 'extra4', 'extra5',  'product2', 'product3', 'remarks']
    template_name = 'polls/order_costumer.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(OrderCreateCustomer, self).form_valid(form)


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
            Q(part__icontains=query) |
            Q(quant__icontains=query) |
            Q(product__icontains=query)
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

    # asdfaslk!! hiush ##
    # try8