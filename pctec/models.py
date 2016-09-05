from __future__ import unicode_literals

from django.db import models
from datetime import date

class Empresa(models.Model):
	nome = models.CharField(max_length=200)
	razao_social = models.CharField(max_length=200, default="")
	cnpj = models.CharField(max_length=14, default="")
	email = models.EmailField()
	sala = models.CharField(max_length=50)
	tel1 = models.CharField(("Telefone 1"), max_length=14)
	tel2 = models.CharField(("Telefone 2"), max_length=14, blank = True)
	tel3 = models.CharField(("Telefone 3"), max_length=14, blank = True)
	
	entrada_pctec= models.DateField(('Data de Entrada PCTec'), default=date.today)
	data_abertura = models.DateField(('Data de Abertura'), default=date.today)
	site = models.URLField(blank = True, null = True, default="")
	#Colaboradores = models.ForeignKey(Colaborador, on_delete=models.CASCADE,blank = True, null = True)
	descricao = models.TextField(blank = True)
	observacao = models.TextField(blank = True)
	logo = models.ImageField(upload_to='empresa/', blank = True, null = True)
	def __str__(self):
		return self.nome

	def image_tag(self):
		return u'<img src="%s" />' % logo
	image_tag.short_description = 'Logo'
	image_tag.allow_tags = True


class Colaborador(models.Model):
	nome = models.CharField(max_length=50)
	sobrenome = models.CharField(max_length=50, default = "")
	tel1 = models.CharField(("Telefone 1"), max_length=14)
	tel2 = models.CharField(("Telefone 2"), max_length=14, blank = True)
	tel3 = models.CharField(("Telefone 3"), max_length=14, blank = True)
	email = models.EmailField()
	cpf = models.CharField(max_length=11)
	rg = models.CharField(max_length=10, blank = True)
	endereco = models.CharField(max_length=200, blank = True)
	cep = models.CharField(max_length=10, blank = True)
	cidade = models.CharField(max_length=50,default="",blank = True)
	estado = models.CharField(max_length=50,default="", blank = True)
	pais = models.CharField(max_length=50,default="", blank = True)
	data_nascimento = models.DateField(("Data de Nascimento"), default=date.today)
	data_entrada = models.DateField(("Data de Entrada"), default=date.today)
	empresa = models.ForeignKey(Empresa, blank = True, null = True)
	foto = models.ImageField(upload_to='colaboradores/', blank = True, null = True, default="/pctec/static/pctec/no_foto.png")
	contato = models.BooleanField(("Definir como Contato"), default=False)
	cracha = models.BooleanField(("Possui Cracha?"), default=False)
	instituicao = models.CharField(("Telefone"), max_length=50, default="PCTec")
	def __str__(self):
		return self.nome