# festival

Descreva aqui as alterações/correções que fez

Ora bem.

Foi alterada a linha: 2
Ficheiro: views.py

from .models import Palco, Dia, Concerto


Foi alterada a linha: 18 para a frente

def concerto_view(request, id):
    concerto = get_object_or_404(Concerto, id=id)
    context = {'concerto': concerto}
    return render(request, 'festival/concerto.html', context)

Lembro-me de fazer isto tambem no meu portfolio. 

A Ideia e conseguir OU apanhar o objecto OU devolver um erro (no meu portfolio fiz erro 404, vou usar a mesma logica aqui, se faz favor)
Assim, se nao houver ID, nao temos erro.

Ficheiro urls.view:

Linha 6:

Falta um caminho. O que esta nao esta necessariamente mal, mas esta incompleto.
Se nao tivermos isto, o path para ir buscar os dias nao esta registrado.
path('dias/', views.dias_view, name='dias'),

Tambem precisamos neste ficheiro (linha 5) de uma forma de aceder a view do palco.

ficheiro concerto.html

ficheiro views.py

nao temos uma funcao que ligue aos views, logo vamos criar uma nova funcao que permita aceder e ver todos os palcos.


concerto.html

navegacao, pois como esta, nao vai navegar entre outras urls.
Quero ir a palcos, nao o consigo fazer.
Quero ir a index, nao consigo.
concerto tem associado 2 atributos
Entao, temos que os ir buscar (concerto.dia, concerto.palco)







    

    L
