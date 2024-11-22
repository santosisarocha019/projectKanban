from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Usuario, Tarefa
from .serializers import UsuarioSerializer, TarefaSerializer

class UsuarioAPIView(APIView):
    def post(self, request):
        usuarioJson = request.data
        usuarioSerialized = UsuarioSerializer(data=usuarioJson)
        usuarioSerialized.is_valid(raise_exception=True)
        usuarioSerialized.save()
        return Response(status=201, data=usuarioSerialized.data)

    def get(self, request, usuarioId=None):
        if usuarioId is None:
            usuarioFound = Usuario.objects.all()
            usuarioSerialized = UsuarioSerializer(usuarioFound, many=True)
            return Response(usuarioSerialized.data)
        else:
    
            try:
                usuarioFound = Usuario.objects.get(id=usuarioId)
                usuarioSerialized = UsuarioSerializer(usuarioFound)
                return Response(usuarioSerialized.data)
            except Usuario.DoesNotExist:
                return Response(status=404, data={"error": "Usuário não encontrado"})

class TarefaAPIView(APIView):
    def post(self, request):
        tarefaJson = request.data
        tarefaSerialized = TarefaSerializer(data=tarefaJson)
        tarefaSerialized.is_valid(raise_exception=True)
        tarefaSerialized.save()
        return Response(status=201, data=tarefaSerialized.data)

    def get(self, request, tarefaId=None):
        status = request.query_params.get('status', None)  
        
        if tarefaId is None:
            if status:
                
                tarefaFound = Tarefa.objects.filter(status=status)
            else:
                
                tarefaFound = Tarefa.objects.all()
                
            tarefaSerialized = TarefaSerializer(tarefaFound, many=True)
            return Response(tarefaSerialized.data)
        else:
            try:
                
                tarefaFound = Tarefa.objects.get(id=tarefaId)
                tarefaSerialized = TarefaSerializer(tarefaFound)
                return Response(tarefaSerialized.data)
            except Tarefa.DoesNotExist:
                return Response(status=404, data={"error": "Tarefa não encontrada"})
    
    
    
    def put(self, request, tarefaId=None):
        try:
            
            tarefaFound = Tarefa.objects.get(id=tarefaId)
        except Tarefa.DoesNotExist:
            return Response(status=404, data={"error": "Tarefa não encontrada!"})

        tarefaJson = request.data

        tarefaSerialized = TarefaSerializer(tarefaFound, data=tarefaJson, partial=True)  # `partial=True` para atualizações parciais
        tarefaSerialized.is_valid(raise_exception=True)
        tarefaSerialized.save()

        return Response(status=200, data=tarefaSerialized.data)

    def delete(self, request, tarefaId=''):
        tarefaFound = None
        try:
            tarefaFound = Tarefa.objects.get(id=tarefaId)
        except Tarefa.DoesNotExist:
            return Response(status=404, data="Tarefa not found")
        tarefaFound.delete()
        return Response(status=200, data="tarefa successfully deletd")


    

