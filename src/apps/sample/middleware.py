# Todo mundo em superuser na minha aplicação em tempo-real
# Posso criar um middleware sendo uma classe ou um método, whatever.


class ChangeNormalUserToAdminMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    # Meu método (call) que fica entre a request e a response
    def __call__(self, request):

        # Antes que meu request seja entregue
        print("Rodou antes")
        response = self.get_response(request)

        # Depois
        return response
