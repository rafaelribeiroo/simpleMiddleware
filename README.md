# Simples middleware

Uma demonstração de como funcionam os middlewares em django

## Conceitos

Middleware fica entre a request e a response, todas as vezes que trabalhamos com qualquer requisição, há uma resposta. Um middleware pode interceptar essa request para retornar uma response totalmente modificada, seja pela ação anterior ou accessibilidade, a ideia é fantástica pois podemos fazer interceptações em tempo-real.

## Configurações.py

Ao trabalhar com o framework django nos deparamos com um arquivo de configurações nomeado: "settings.py", que contém uma tupla chamada MIDDLEWARE, abaixo veremos como ela funciona.

```
MIDDLEWARE = [

	# Ele vai várias validações como por exemplo o tipo de request, ver se você está atrás de um proxy, ele pode ajudar você a escapar informações
    'django.middleware.security.SecurityMiddleware',

    # Depois ele passa por um middleware de sessão, carrega sessão, carrega os usuários, fazer gerenciamento da sessão
    'django.contrib.sessions.middleware.SessionMiddleware',

    # No django, ao trabalhar com forms devemos por o csrf_token, esse middleware validará se aquele CSRF é o mesmo no momento que a pessoa está fazendo o POST
    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

> Como eles são chamados?

Como eles são chamados?

Primeiro, o de segurança é chamado, ele pode ter 2 ações sobre a requisição, ou interromper por ali mesmo e não chamar os abaixos ou retornar uma informação completamente alterada (timezone está setado em pt-BR mas se a pessoa acessar de Londres, passar a ter as informações apresentadas em língua nativa), e ir chamando os itens abaixo consecutivamente, "sessão etc"