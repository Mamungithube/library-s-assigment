from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .forms import ChangeuserData,RegistrationForm,CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile,Comment,Book,PaymentModel
from django.contrib.auth.decorators import login_required



class CustomLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('home')

class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('login')
    
class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        valid = super().form_valid(form)
        Profile.objects.create(user=self.object)
        return valid


class UpdateUserProfileView(LoginRequiredMixin,UpdateView):
    form_class = ChangeuserData
    template_name = 'profile.html'
    success_url = reverse_lazy('profile')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Bookall"] = PaymentModel.objects.all()
        return context
    

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        return response
    

class BookDetailView(DetailView):
    model = Book
    pk_url_kwarg = 'pk'
    template_name = 'details.html'
    context_object_name = 'Book'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        Book_object = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.Book = Book_object
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        Book_post = self.object
        context['comments'] = Comment.objects.all()
        context['form'] = CommentForm()
        return context
    


@login_required
def buy_now(request, Book_id):
    Book_data = Book.objects.get(pk=Book_id)
    if 0 < Book_data.Quantity:
        Book_data.Quantity -= 1
        Book_data.save()
        
        payment = PaymentModel.objects.create(
            Book_name=Book_data,
            user=request.user,
            net_quantity=1,
            total_price=Book_data.Borrow_price
        )

    return redirect('book_detail', pk=Book_id)