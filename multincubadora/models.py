from __future__ import unicode_literals

from django.db import models
from datetime import date
# Create your models here.

class Incubada(models.Model):
	nome = models.CharField(max_length=200)
	cnpj = models.CharField(max_length=14, default="",blank = True)
	socio = models.CharField(max_length=200, default="")
	email = models.EmailField(blank = True)
	sala = models.CharField(max_length=50)
	tel1 = models.CharField(("Telefone"), max_length=14, blank = True)
	responsavel_financeiro = models.CharField(max_length=200, blank = True, default="")

	site = models.URLField(null = True,blank = True)
	linkedin =  models.URLField(null = True,blank = True)
	facebook = models.URLField(null = True,blank = True)
	blog = models.URLField(null = True,blank = True)
	twitter = models.URLField(null = True,blank = True)
	
	descricao = models.TextField(blank = True)
	observacao = models.TextField(blank = True)
	logo = models.ImageField(upload_to='incubada/', blank = True, null = True, default="multincubadora/unb.png")
	def __str__(self):
		return self.nome

	def image_tag(self):
		return u'<img src="%s" />' % logo
	image_tag.short_description = 'Logo'
	image_tag.allow_tags = True

class Graduada(models.Model):
	nome = models.CharField(max_length=200)
	cnpj = models.CharField(max_length=14, default="")
	data_saida = models.CharField(max_length=4, blank = True, null = True)
	status = models.CharField(max_length=8, blank = True, null = True)
	socio = models.TextField(blank = True, null = True)
	email = models.TextField(blank = True, null = True)
	descricao = models.TextField(blank = True)
	enviar_type = models.CharField(max_length=50, blank = True, null = True)
	def __str__(self):
		return self.nome

class Empresa_Junior(models.Model):
	nome = models.CharField(max_length=200)
	curso = models.CharField(max_length=100)
	email_responsavel = models.TextField(blank = True, null = True)
	tel1 = models.CharField(("Telefone"), max_length=14, blank = True)
	descricao = models.TextField(blank = True)
	logo = models.ImageField(upload_to='prjr/', blank = True, null = True)
	def __str__(self):
		return self.nome

	def image_tag(self):
		return u'<img src="%s" />' % logo
	image_tag.short_description = 'Logo'
	image_tag.allow_tags = True

class Automovel(models.Model):
	placa = models.CharField(max_length = 9,blank = True)
	modelo = models.CharField(max_length = 20)
	cor = models.CharField(max_length = 10,blank = True)
	def __str__(self):
		return self.modelo
	

class Consultores(models.Model):
	nome = models.CharField(max_length=50)
	empresa = models.TextField()
	redes_sociais = models.TextField(blank = True, null = True)
	eixo = models.TextField()
	email = models.EmailField(default="",blank = True)
	tel1 = models.CharField(("Telefone"), max_length=14,blank = True)
	def __str__(self):
		return self.nome

class Colaborador(models.Model):
	nome = models.CharField(max_length=50)
	cpf = models.CharField(max_length=14)
	rg = models.CharField(max_length=10, blank = True)
	expeditor = models.CharField(max_length=10, blank = True)
	tel1 = models.CharField(("Telefone"), max_length=14,blank = True)
	email = models.EmailField()
	endereco = models.CharField(max_length = 200, blank = True)
	foto = models.ImageField(upload_to='colaboradores_multi/', blank = True, null = True, default="/colaboradores_multi/no_foto.png")
	instituicao = models.CharField(("Telefone"), max_length=50, default="Multincubadora")
	class Meta:
		abstract = True
		ordering = ['nome']

class Colaborador_multi(Colaborador):
	empresa = models.ForeignKey(Incubada, blank = True, null = True)
	status_cracha = models.CharField(max_length = 8)
	automovel = models.ForeignKey(Automovel, blank = True, null = True)
	def __str__(self):
		return self.nome

class Colaborador_Empresa_Junior(Colaborador):
	empresa = models.ForeignKey(Empresa_Junior, blank = True, null = True)
	presidente = models.BooleanField(default=False)
	def __str__(self):
		return self.nome







