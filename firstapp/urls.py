from django.urls import path
from . import views

# app_name = "firstapp"

urlpatterns = [
    # path("", views.home, name="home"),
    path("about", views.AboutPageView.as_view(), name="about"),

    path("", views.TodoListView.as_view(), name="todo_list"),
    path("<int:pk>", views.TodoDetailView.as_view(), name="todo_detail"),
    path("create/", views.TodoCreateView.as_view(), name="create_todo"),
    path("update/<int:pk>", views.TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", views.TodoDeleteView.as_view(), name="todo_delete"),

    path("register/", views.SignUpView.as_view(), name="register"),
    path("login/", views.SignInView.as_view(), name="login"),
    path("logout/", views.SignOutView.as_view(), name="logout"),
    path("user-update/<int:pk>", views.UserUpdateView.as_view(), name="user_update"),
    path("password-update/<int:pk>", views.PasswordUpdateView.as_view(), name="password_update"),
    path("user-delete/<int:pk>", views.UserDeleteView.as_view(), name="user_delete"),
]
