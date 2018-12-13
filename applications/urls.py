from django.urls import path
from . import views
from . import fileops

app_name = "applications"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.get_login, name="get_login"),
    path("post_login", views.post_login, name="post_login"),
    path("logout", views.logoutUser, name="logout"),
    path("register", views.get_register, name="get_register"),
    path("post_register", views.post_register, name="post_register"),
    path("add_app", views.add_app, name="add_app"),
    path("save_app", views.save_app, name="save_app"),
    path("show_app/<int:app_id>", views.show_app, name="show_app"),
    path("edit_app/<int:app_id>", views.edit_app, name="edit_app"),
    path("update_app/<int:app_id>", views.update_app, name="update_app"),
    path("delete_app/<int:app_id>", views.delete_app, name="delete_app"),

    path("search/", fileops.get_search, name="fops_get_search"),
    path("post_search/", fileops.post_search, name="fops_post_search"),
]