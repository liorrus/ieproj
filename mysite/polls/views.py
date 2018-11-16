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


from django.http import HttpResponse

#from here
class UserFormView(View):
    form_class=UserForm
    template_name='polls/registration_form.html'
    #display blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request, self.template_name, {'form':form})


    #process from data
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            #cleaned (normalized) data
            username= form.cleaned_data['username']
            password= form.cleaned_data['password']
            user.set_password(password)
            user.save()
            # return user objects if details are correct
            user=authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return  redirect('polls:index')
        return render(request, self.template_name, {'form':form})

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'polls/login.html'

    def form_valid(self, form):
        usuario = form.get_user()

        django_login_view(self.request, usuario)
        return redirect('polls:index')

        #return super(LoginView, self).form_valid(form)

#from .models import all  # Choice, Question, Product, Part, Unit
def logout(request):
    auth.logout(request)
    return render(request,'polls/logout.html')

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class ProductView(generic.ListView):
    #model = Product
    context_object_name = 'all_generics'
    template_name ='polls/generic_list.html'
    def get_queryset(self):
        return Product.objects.all()

class ProductOneView(generic.DetailView):
    model = Product
    template_name = 'polls/product_one.html'
    slug_url_kwarg = 'slug'

class PartOneView(generic.DetailView):
    model = Part
    template_name = 'polls/part_one.html'
    slug_url_kwarg = 'slug'

class PartView(generic.ListView):
    context_object_name = 'all_generics'
    template_name ='polls/generic_list.html'
    def get_queryset(self):
        return Part.objects.all()

class SupplierOneView(generic.DetailView):
    model = Supplier
    template_name = 'polls/part_one.html'
    slug_url_kwarg = 'slug'

class SupplierView(generic.ListView):
    context_object_name = 'all_generics'
    template_name ='polls/generic_list.html'
    def get_queryset(self):
        return Supplier.objects.all()














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

    #asdfaslk!! hiush ##
    #try8