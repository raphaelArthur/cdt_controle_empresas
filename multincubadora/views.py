from django.shortcuts import get_object_or_404, render 

from django.template import loader

# import cStringIO as StringIO
# from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

from .models import Incubada, Graduada, Empresa_Junior, Automovel, Colaborador_multi, Consultores, Colaborador_Empresa_Junior
#from cgi import escape


# def render_to_pdf(template_src, context_dict):
#     template = get_template(template_src)
#     context = Context(context_dict)
#     html  = template.render(context)
#     result = StringIO.StringIO()

#     pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

# def myview(request):
#     #Retrieve data or whatever you need
#     return render_to_pdf(
#             'cracha.html',
#             {
#                 'pagesize':'A4',
#                 'mylist': results,
#             }
#         )


def multi_princ(request):
    return render(request, 'multincubadora/multi_princ.html')

def incubadas(request):
	lista_empresas_incubadas = Incubada.objects.order_by('-nome')
	context = {
		'lista_empresas_incubadas': lista_empresas_incubadas,
	}
	return render(request, 'multincubadora/incubadas.html',context)

def projr(request):
	lista_empresas_junior = Empresa_Junior.objects.order_by('-nome')
	context = {
		'lista_empresas_junior': lista_empresas_junior,
	}
	return render(request, 'multincubadora/projr.html', context)

def projr_detalhe(request, jr_id):
	empresa = get_object_or_404(Empresa_Junior, pk=jr_id)
	lista_colaboradores = Colaborador_Empresa_Junior.objects.filter(empresa=jr_id).order_by('-nome')
	context = {
		'lista_colaboradores': lista_colaboradores,
		'empresa': empresa,
	}
	return render(request, 'multincubadora/projr_detalhe.html', context)

def atendimento(request):
	return render(request, 'multincubadora/atendimento.html')

def consultores(request):
	lista_consultores = Consultores.objects.order_by('-nome')
	context = {
		'lista_consultores': lista_consultores,
	}
	return render(request, 'multincubadora/consultores.html',context)

def profs_labs(request):
	return render(request, 'multincubadora/profs_labs.html')

def empresas_detalhe(request, incubada_id):
	incubada = get_object_or_404(Incubada, pk=incubada_id)
	lista_colaboradores = Colaborador_multi.objects.filter(empresa=incubada_id).order_by('-nome')
	context = {
		'lista_colaboradores': lista_colaboradores,
		'incubada': incubada,
		'range_redes':(5),
	}
	return render(request, 'multincubadora/incubadas_detalhe.html', context)

def graduadas(request):
	lista_empresas_graduadas = Graduada.objects.order_by('-nome')
	context = {
		'lista_empresas_graduadas': lista_empresas_graduadas,
	}
	return render(request, 'multincubadora/graduadas.html', context)

def colaborador(request,incubada_id, colaborador_id):
	colaborador = get_object_or_404(Colaborador_multi, pk=colaborador_id)
	context = {
		'colaborador': colaborador,
	}
	return render(request, 'multincubadora/colaborador.html',context)

def cracha(request, colaborador_id):
    colaborador = get_object_or_404(Colaborador_multi, pk=colaborador_id)
    context = {
        'colaborador': colaborador,
    }
    return render(request, 'multincubadora/cracha.html', context)