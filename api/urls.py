from django.urls import path
from . import views

urlpatterns = [
	path('', views.listOf, name="list-Of"),
    path('viewSomeBlog/', views.viewSomeBlog, name="view-Some-Blog"),
	path('inputBlog/', views.inputBlog, name="input-Blog"),
    path('outputBlog/<str:pk>/', views.outputBlog, name="output-Blog"),
]