# Todo mundo em superuser na minha aplicação em tempo-real
# Posso criar um middleware sendo uma classe ou um método, whatever.
from django.contrib.auth.models import User


class ChangeNormalUserToAdminMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    # Meu método (call) que fica entre a request e a response
    def __call__(self, request):

        # Antes que meu request seja entregue
        rafael = User.objects.get(username='Rafael')
        print(request.user)
        request.user = rafael
        print(request.user)

        print('Rodou antes')
        response = self.get_response(request)

        # Depois
        return response

# No caso utilizei apenas 2 hooks que o Django já me fornece, sendo eles: call e init. Métodos de middleware basicamente.
