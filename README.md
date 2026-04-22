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


    

    L
