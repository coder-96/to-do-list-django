from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, \
    ListView, DetailView, UpdateView, DeleteView
from .models import Todo, User
from .forms import TodosForm, MyUserCreationForm, UserForm, PasswordUpdateForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# def home(request):
#     return render(request, "firstapp/about.html")

class SignUpView(CreateView):
    template_name = "firstapp/signup.html"
    form_class = MyUserCreationForm

    def get_success_url(self):
        return reverse_lazy("todo_list")

    def form_valid(self, form):
        # if self.request.user.is_authenticated:
        form.instance.username = self.request.POST.get("email")
        form.save()
        # return super().form_valid(form)
        return super(SignUpView, self).form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = "firstapp/user_update.html"

    def get_success_url(self):
        return reverse_lazy('todo_list')

    def form_valid(self, form):
        # if self.request.user.is_authenticated:
        form.instance.username = self.request.POST.get("email")
        form.instance.avatar = self.request.POST.get("avatar")
        form.save()
        # return super().form_valid(form)
        return super(UserUpdateView, self).form_valid(form)


class PasswordUpdateView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordUpdateForm
    template_name = "firstapp/password_update.html"

    def get_success_url(self):
        # pk = self.kwargs['pk']
        # return reverse_lazy('user_update', kwargs={'pk': pk})
        return reverse_lazy('todo_list')


class SignInView(LoginView):
    template_name = "firstapp/signin.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todo_list')


class SignOutView(LoginRequiredMixin, LogoutView):

    def get_success_url(self):
        return reverse_lazy('login')


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "firstapp/user_delete.html"
    success_url = reverse_lazy('login')


class AboutPageView(TemplateView):
    template_name = "firstapp/about.html"


class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    # queryset = Todo.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = context["todo_list"].filter(user=self.request.user)
        context["count"] = Todo.objects.filter(done=False, user=self.request.user).count()

        search_input = self.request.GET.get("search-area") or ""
        if search_input:
            context["todo_list"] = context["todo_list"].filter(name__startswith=search_input)
        context["search_input"] = search_input
        return context

class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Todo


class TodoCreateView(LoginRequiredMixin, CreateView):
    form_class = TodosForm
    template_name = "firstapp/todo_form.html"

    def get_success_url(self):
        return reverse_lazy('todo_list')
        # return reverse('about')

    # Optional: Overwrite form data (before save)
    def form_valid(self, form):
        # if self.request.user.is_authenticated:
        form.instance.user = self.request.user
        form.instance.done = False
        form.save()

        # return super().form_valid(form)
        return super(TodoCreateView, self).form_valid(form)


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = "firstapp/todo_delete.html"
    success_url = reverse_lazy('todo_list')


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    form_class = TodosForm
    template_name = "firstapp/todo_update.html"

    def get_success_url(self):
        return reverse_lazy('todo_list')
