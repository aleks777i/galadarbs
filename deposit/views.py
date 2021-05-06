from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy, reverse
from .models import Deposit
from .forms import DepositForm
from django.http import HttpResponseRedirect


def countInterest(deposit, term, rate):
    sum = deposit
    for i in range(0, term):
        sum = sum * (1+rate)
    return sum - deposit


class DepositListView(ListView):

    model = Deposit
    template_name = 'index.html'
    context_object_name = 'deposits'
    # paginate_by = 3

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['counter'] = Deposit.objects.all().count()
    #     return context


class DepositDetailView(DetailView):

    model = Deposit
    template_name = 'deposit.html'
    context_object_name = 'deposit'




class DepositAddView(CreateView):
    model = Deposit
    fields = ['deposit', 'term', 'rate', ]
    template_name = 'add_deposit.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.interest = countInterest(self.object.deposit, self.object.term, self.object.rate)
        print(self.object.interest)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
#
#
# class DepositDeleteView(DeleteView):
#     model = Deposit
#     template_name = 'user_confirm_delete.html'
#     success_url = reverse_lazy('home')
#
#
# class DepositUpdateView(UpdateView):
#     model = Deposit
#     fields = ['username', 'email']
#     template_name = 'update_user.html'


