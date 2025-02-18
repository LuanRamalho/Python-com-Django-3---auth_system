from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def auth_home(request):
    return JsonResponse({"mensagem": "Bem-vindo ao sistema de autenticacao! Use /register/, /login/, ou /logout/."})

@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = User.objects.create_user(username=data['username'], password=data['password'])
        return JsonResponse({"mensagem": "Usuário criado com sucesso!", "id": user.id})
    return JsonResponse({"erro": "Metodo nao permitido. Use POST."}, status=405)

@csrf_exempt
@csrf_exempt
def user_login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            login(request, user)
            return JsonResponse({"mensagem": "Login realizado com sucesso!"})
        return JsonResponse({"erro": "Credenciais inválidas"}, status=400)
    else:
        return JsonResponse({"erro": "Método GET não permitido. Use POST para login."}, status=405)


@csrf_exempt
def user_logout(request):
    logout(request)
    return JsonResponse({"mensagem": "Logout realizado com sucesso!"})
