from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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


class OrderUser(generic.ListView):
    #model = Order
    context_object_name = 'all_generics'
    template_name = 'polls/order.html'

    def get_queryset(self):
        return Order.objects.all()

    def get_context_data(self, **kwargs):
        context=super(OrderUser,self).get_context_data(**kwargs)
        context['extras_form']=Extras.objects.all()
        context['product_form']=Product.objects.all()
        return context


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


""" Lior M """

class ProductIndexView(generic.ListView):
    template_name = 'polls/product_index.html'
    context_object_name = 'all_products'

    def get_queryset(self):
        """Return the last five published questions."""
        return Product.objects.all()


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'polls/product_detail.html'


class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'polls/order_detail.html'


class OrderIndexView(generic.ListView):
    template_name = 'polls/order_index.html'
    context_object_name = 'all_orders'

    def get_queryset(self):
        """Return the last five published questions."""
        return Order.objects.all()


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class ProductView(generic.ListView):
    model = Product
    context_object_name = 'all_generics'
    template_name = 'polls/generic_list.html'

    def get_queryset(self):
        return Product.objects.all()


class ProductOneView(generic.DetailView):
    model = Product
    template_name = 'polls/product_one.html'
    slug_url_kwarg = 'slug'


class ExtraView(generic.ListView):
    # model = Product
    context_object_name = 'all_generics'
    template_name = 'polls/generic_list.html'

    def get_queryset(self):
        return Extras.objects.all()


class ExtraOneView(generic.DetailView):
    model = Extras
    template_name = 'polls/extra_one.html'
    slug_url_kwarg = 'slug'


class PartOneView(generic.DetailView):
    model = Part
    template_name = 'polls/part_one.html'
    slug_url_kwarg = 'slug'


class PartView(generic.ListView):
    context_object_name = 'all_generics'
    template_name = 'polls/generic_list.html'

    def get_queryset(self):
        return Part.objects.all()


class SupplierOneView(generic.DetailView):
    model = Supplier
    template_name = 'polls/part_one.html'
    slug_url_kwarg = 'slug'


class SupplierView(generic.ListView):
    context_object_name = 'all_generics'
    template_name = 'polls/generic_list.html'

    def get_queryset(self):
        return Supplier.objects.all()


class OrderView(generic.ListView):
    context_object_name = 'all_generics'
    template_name = 'polls/generic_list.html'

    def get_queryset(self):
        return Order.objects.all()


"""Lior M"""


class ProductCreate(CreateView):
    model = Product
    fields = ['pdes', 'price', 'prep', 'slug']


class PartCreate(CreateView):
    model = Part
    fields = ['pdes', 'unit', 'stock', 'lt', 'sshigh', 'sslow']


class SupplierCreate(CreateView):
    model = Supplier
    fields = ['name', 'address', 'tel', 'mail']


class PartsInProductCreate(CreateView):
    model = PartsInProduct
    fields = ['part', 'quant', 'product']


from django.contrib.auth.mixins import LoginRequiredMixin


class OrderCreate(LoginRequiredMixin, CreateView):  # LoginRequiredMixin
    model = Order
    fields = ['user', 'orderPick', 'orderStatus', 'ifSupplied', 'product1',  'component1',
              'component2',  'component3',  'component4', 'component5',
              'extra1', 'extra2', 'extra3', 'extra4', 'extra5',  'product2', 'product3', 'remarks']
    """template_name = 'polls/generice_form.html'"""

    def form_valid(self, form):
        form.instance.user = self.request.user
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

    # asdfaslk!! hiush ##
    # try8