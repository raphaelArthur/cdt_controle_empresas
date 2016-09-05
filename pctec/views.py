from django.shortcuts import get_object_or_404, render 
from django.http import HttpResponse

from django.template import loader

from .models import Empresa, Colaborador

def index(request):
    return render(request, 'pctec/index.html')

def pctec(request):
	lista_empresas = Empresa.objects.order_by('-nome')
	context = {
		'lista_empresas': lista_empresas,
	}
	return render(request, 'pctec/pctec.html', context)

def detail(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)
    lista_colaboradores = Colaborador.objects.filter(empresa=empresa_id).order_by('-nome')
    context = {
    	'lista_colaboradores': lista_colaboradores,
    	'empresa': empresa,
    }
    return render(request, 'pctec/detail.html', context)

def colaborador(request,empresa_id, colaborador_id):
    colaborador = get_object_or_404(Colaborador, pk=colaborador_id)
    context = {
        'colaborador': colaborador,
    }
    return render(request, 'pctec/colaborador.html', context)
    #return render(request, 'pctec/teste.html')

def cracha(request, colaborador_id):
    colaborador = get_object_or_404(Colaborador, pk=colaborador_id)
    context = {
        'colaborador': colaborador,
    }
    return render(request, 'multincubadora/cracha.html', context)
