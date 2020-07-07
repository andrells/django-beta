from django.urls import path
from . import views


urlpatterns = [
    path('', views.listaProdutos, name='produtos'),
    path('add/', views.addProdutos, name='addproduto'),
    path('edit/<int:id>', views.editProdutos, name="edit-produto"),
    path('delete/<int:id>', views.deleteProdutos, name="delete-produto"),
    path('produto/<int:id>', views.produtosViews, name="produto-view"),

]
