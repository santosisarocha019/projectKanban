from django.urls import path
from .views import UsuarioAPIView, TarefaAPIView

urlpatterns = [
    path('usuario/', UsuarioAPIView.as_view(), name='usuario'),
    path('usuario/<int:usuarioId>/', UsuarioAPIView.as_view(), name='usuario-detail'),
    path('tarefa/', TarefaAPIView.as_view(), name='tarefa'),
    path('tarefa/<int:tarefaId>/', TarefaAPIView.as_view(), name='tarefa-detail'),
]

