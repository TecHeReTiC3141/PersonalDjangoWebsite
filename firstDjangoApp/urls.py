"""firstDjangoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.views.generic import TemplateView

all_projects = [
    [
        {'title': 'Platformetic', 'image': '/images/platformetic.png',
         'descr': 'Simple platformer with elements of bullet hell',
         'refs': [{'ref': 'https://github.com/TecHeReTiC3141/PygamePlatformer',
                   'img': '/images/github.png'}]},
        {'title': 'Dungetic', 'image': '/images/dungetic.png',
         'descr': 'Rogue-like game with elements of RPG',
         'refs': [{'ref': 'https://github.com/TecHeReTiC3141/Dungetic',
                   'img': '/images/github.png'}]},
    ],

    [
        {'title': 'Style Transfering bot', 'image': '/images/style_bot.png',
         'descr': 'Tg bot which can transfer style of one image to another one',
         'refs': [{'ref': 'https://github.com/TecHeReTiC3141/NeuroTransferStylerBot',
                   'img': '/images/github.png'}]},
        {'title': 'Platformetic', 'image': '/images/platformetic.png',
         'descr': 'Simple platformer with elements of bullet hell',
         'refs': [{'ref': 'https://github.com/TecHeReTiC3141/PygamePlatformer',
                   'img': '/images/github.png'}]},
    ],

]


urlpatterns = [
    path("", TemplateView.as_view(template_name='main_page.html',
                                  extra_context={'projects': all_projects}
                                  ))
]
