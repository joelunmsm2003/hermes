from django.shortcuts import *
from django.template import RequestContext
from django.contrib.auth import *
from django.contrib.auth.models import Group, User
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.core.urlresolvers import reverse
from django.db.models import Max,Count
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cotizar.models import *
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import View

from jwt_auth.compat import json
from jwt_auth.mixins import JSONWebTokenAuthMixin

from django.db import transaction
from django.contrib.auth.hashers import *
from django.core.mail import send_mail
from django.db import connection
from django.utils.six.moves import range
from django.http import StreamingHttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt
from jwt_auth.compat import json
from jwt_auth.mixins import JSONWebTokenAuthMixin

from django.db.models import Count, Min, Sum, Avg
import collections
from datetime import *
from decimal import *
import xlrd
import json 
import csv
import simplejson
import xlwt
import requests
import os
import pdfkit
import datetime
import pdfcrowd

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.models import Group, User
from jwt_auth.compat import json
from jwt_auth.mixins import JSONWebTokenAuthMixin

import simplejson
from django.views.decorators.csrf import csrf_exempt
import xlrd



from django.views.decorators.csrf import csrf_exempt



from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter, landscape

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch


from django.http import HttpResponse


class Perfil(JSONWebTokenAuthMixin, View):

	def get(self, request):

		id =request.user.id

		print 'ID',id

		return HttpResponse(id, content_type="application/json")


def hello(c):
	from reportlab.lib.units import inch

	#First Example

	c.setFont("Helvetica", 6) #choose your font type and font size
  
def pdfout(request):
 
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

	p = canvas.Canvas(response)

	p.setFillColorRGB(0,0,0)


	logo = "/var/www/cotizacion/frontend/img/logo-hermes.png"

	p.drawImage(logo, 20, 800,width=80,height=22,mask='auto');

	hello(p)
	j=50

	r = requests.get('http://cotizador.hermes.pe:800/html/cotiza.json')
	c = requests.get('http://cotizador.hermes.pe:800/html/coberturas.json')
	d = requests.get('http://cotizador.hermes.pe:800/html/deducibles.json')
	s = requests.get('http://cotizador.hermes.pe:800/html/servicios.json')
	g = requests.get('http://cotizador.hermes.pe:800/html/gps.json')
	cl = requests.get('http://cotizador.hermes.pe:800/html/cliente.json')
	f = requests.get('http://cotizador.hermes.pe:800/html/financiamiento.json')

	a = json.loads(r.text)
	c= json.loads(c.text)
	d= json.loads(d.text)
	s= json.loads(s.text)
	g= json.loads(g.text)
	cl= json.loads(cl.text)
	cl= cl[0]
	fi= json.loads(f.text)


	#'id_cliente','fullname','email','celular','chose_marca__name_marca','chose_modelo__name_model','chose_tipo__clase','chose_timon__name_tipo','chose_modalid__name_modalidad','chose_uso__uso','chose_anio__anio_antig','chose_ubicl','chose_ubicp','chose_informat','value');
	
	print 'hahhaha',cl
	# Draw things on the PDc. Here's where the PDF generation happens.
	# See the ReportLab documentation for the full list of functionality.

	columna = 780
	es=0

	p.drawString(20, columna, "Datos Cliente")
	p.drawString(70+j, columna,str(cl['id_cliente'] ))
	p.drawString(120+j*2, columna,'Nombre: '+str(cl['fullname'] ))
	p.drawString(170+j*3, columna,'Email: '+str(cl['email'] ))


	et=2
	p.setFillColorRGB(0,0,0)
	p.rect(20,columna-13*et,7.5*inch,.15*inch, fill=1)
	p.setFillColorRGB(13,10,101)
	p.drawString(22, columna-13*et+3,'Marca: ' )
	p.drawString(70+j, columna-13*et+3,'Modelo: ')
	p.drawString(120+j*2, columna-13*et+3,'Clase: ')
	p.drawString(170+j*3, columna-13*et+3,'Anio: ')
	p.drawString(220+j*4, columna-13*et+3,'Precio: ')


	et=3
	p.setFillColorRGB(0,0,0)

	p.drawString(20, columna-12*et,str(cl['chose_marca__name_marca']))
	p.drawString(70+j, columna-12*et,str(cl['chose_modelo__name_model'] ))
	p.drawString(120+j*2, columna-12*et,str(cl['chose_tipo__clase'] ))
	p.drawString(170+j*3, columna-12*et,str(cl['chose_anio__anio_antig'] ))
	p.drawString(220+j*4, columna-12*et,str(cl['value'] ))

	

	#et=4
	
	#p.drawString(70+j, columna-13*et+3,'MAPFRE ')
	#p.drawString(120+j*2, columna-13*et+3,'LA POSITIVA ')
	#p.drawString(170+j*3, columna-13*et+3,'RIMAC: ')
	#p.drawString(220+j*4, columna-13*et+3,'PACIFICO: ')
	#p.drawString(250+j*5, columna-13*et+3,'Marca: ' )

	et = 4
	#p.drawString(20, columna-15*et, "GPS")

	p.drawString(70+j, columna-13*et,'GPS: '+g['gpsmapfre'] )
	p.drawString(120+j*2, columna-13*et,'GPS: '+g['gpspositiva'] )
	p.drawString(170+j*3, columna-13*et,'GPS: '+g['gpsrimac'] )
	p.drawString(220+j*4, columna-13*et,'GPS: '+g['gpspacifico'])
	p.drawString(250+j*5, columna-13*et,'GPS: '+g['gpshdi'] )


	et=5
	p.setFillColorRGB(0,0,0)
	p.rect(20,columna-15*et,7.5*inch,.15*inch, fill=1)
	p.setFillColorRGB(13,10,101)
	p.drawString(250, columna-15*et+3, "Financiamiento")

	fi[0]['financiamiento'] = fi[0]['financiamiento'].encode('ascii','ignore').encode('ascii','replace')
	fi[0]['mapfre'] = fi[0]['mapfre'].encode('ascii','ignore').encode('ascii','replace')
	fi[0]['positiva']= fi[0]['positiva'].encode('ascii','ignore').encode('ascii','replace')
	fi[0]['rimac']= fi[0]['rimac'].encode('ascii','ignore').encode('ascii','replace')
	fi[0]['hdi']= fi[0]['hdi'].encode('ascii','ignore').encode('ascii','replace')

	fi[1]['financiamiento'] = fi[1]['financiamiento'].encode('ascii','ignore').encode('ascii','replace')
	fi[1]['mapfre'] = fi[1]['mapfre'].encode('ascii','ignore').encode('ascii','replace')
	fi[1]['positiva']= fi[1]['positiva'].encode('ascii','ignore').encode('ascii','replace')
	fi[1]['rimac']= fi[1]['rimac'].encode('ascii','ignore').encode('ascii','replace')
	fi[1]['hdi']= fi[1]['hdi'].encode('ascii','ignore').encode('ascii','replace')

	fi[2]['financiamiento'] = fi[2]['financiamiento'].encode('ascii','ignore').encode('ascii','replace')
	fi[2]['mapfre'] = fi[2]['mapfre'].encode('ascii','ignore').encode('ascii','replace')
	fi[2]['positiva']= fi[2]['positiva'].encode('ascii','ignore').encode('ascii','replace')
	fi[2]['rimac']= fi[2]['rimac'].encode('ascii','ignore').encode('ascii','replace')
	fi[2]['hdi']= fi[2]['hdi'].encode('ascii','ignore').encode('ascii','replace')


	et =6
	p.drawString(20, columna-15*et, str(fi[0]['financiamiento']))
	p.drawString(70+j, columna-15*et, str(fi[0]['mapfre']))
	p.drawString(120+j*2, columna-15*et, str(fi[0]['positiva']))
	p.drawString(170+j*3, columna-15*et, str(fi[0]['rimac']))
	p.drawString(220+j*4, columna-15*et, str(fi[0]['pacifico']))
	p.drawString(250+j*5, columna-15*et, str(fi[0]['hdi']))

	et=7
	p.drawString(20, columna-15*et, str(fi[1]['financiamiento']))
	p.drawString(70+j, columna-15*et, str(fi[1]['mapfre']))
	p.drawString(120+j*2, columna-15*et, str(fi[1]['positiva']))
	p.drawString(170+j*3, columna-15*et, str(fi[1]['rimac']))
	p.drawString(220+j*4, columna-15*et, str(fi[1]['pacifico']))
	p.drawString(250+j*5, columna-15*et, str(fi[1]['hdi']))

	et=8
	p.drawString(20, columna-15*et, str(fi[2]['financiamiento'])[0:30])
	p.drawString(70+j, columna-15*et, str(fi[2]['mapfre']))
	p.drawString(120+j*2, columna-15*et, str(fi[2]['positiva']))
	p.drawString(170+j*3, columna-15*et, str(fi[2]['rimac']))
	p.drawString(220+j*4, columna-15*et, str(fi[2]['pacifico']))
	p.drawString(250+j*5, columna-15*et, str(fi[2]['hdi']))
	

	et=9

	p.drawString(20, columna-15*et, "Aseguradoras")
	p.drawString(70+j, columna-15*et, "Mapfre")
	p.drawString(120+j*2, columna-15*et, "La Positiva")
	p.drawString(170+j*3, columna-15*et, "Rimac")
	p.drawString(220+j*4, columna-15*et, "Pacifico")
	p.drawString(250+j*5, columna-15*et, "HDI")

	et =10
	p.drawString(20, columna-15*et, "Tasa")
	p.drawString(70+j, columna-15*et, str(a['tasamapfre']))
	p.drawString(120+j*2, columna-15*et, str(a['tasapositiva']))
	p.drawString(170+j*3, columna-15*et, str(a['tasarimac']))
	p.drawString(220+j*4, columna-15*et, str(a['tasapacifico']))
	p.drawString(250+j*5, columna-15*et, str(a['tasahdi']))

	et=11
	p.drawString(20, columna-15*et, "Prima Neta")
	p.drawString(70+j, columna-15*et, str(a['mapfre']))
	p.drawString(120+j*2, columna-15*et, str(a['positiva']))
	p.drawString(170+j*3, columna-15*et, str(a['rimac']))
	p.drawString(220+j*4, columna-15*et, str(a['pacifico']))
	p.drawString(250+j*5, columna-15*et, str(a['hdi']))

	et=12
	p.drawString(20, columna-15*et, "Prima Comercial")
	p.drawString(70+j, columna-15*et, str(a['mapfresubtotal']))
	p.drawString(120+j*2, columna-15*et, str(a['positivasubtotal']))
	p.drawString(170+j*3, columna-15*et, str(a['rimacsubtotal']))
	p.drawString(220+j*4, columna-15*et, str(a['pacificosubtotal']))
	p.drawString(250+j*5, columna-15*et, str(a['phdisubtotal']))
	
	et=13

	p.drawString(20, columna-15*et, "Total")
	p.drawString(70+j, columna-15*et, str(a['mapfresubtotal']))
	p.drawString(120+j*2, columna-15*et, str(a['positivatotal']))
	p.drawString(170+j*3, columna-15*et, str(a['rimactotal']))
	p.drawString(220+j*4, columna-15*et, str(a['pacificototal']))
	p.drawString(250+j*5, columna-15*et, str(a['phditotal']))

	columna = columna -40



	p.setFillColorRGB(1,0.54902,0)
	p.rect(20,columna-140,7.5*inch,.15*inch, fill=1)
	p.setFillColorRGB(0,0,0)
	p.drawString(122, columna-140+3, "Coberturas")

	for i in range(0,18):

		c[i]['descripcion'] = c[i]['descripcion'].encode('ascii','ignore').encode('ascii','replace')
		c[i]['mapfre'] = c[i]['mapfre'].encode('ascii','ignore').encode('ascii','replace')
		c[i]['positiva']= c[i]['positiva'].encode('ascii','ignore').encode('ascii','replace')
		c[i]['rimac']= c[i]['rimac'].encode('ascii','ignore').encode('ascii','replace')

		#c[i]['pacifico']= c[i]['pacifico'].encode('ascii','ignore').encode('ascii','replace')
		c[i]['hdi']= c[i]['hdi'].encode('ascii','ignore').encode('ascii','replace')
		
		p.drawString(20, columna-160-15*i, str(c[i]['descripcion'])[0:30])
		p.drawString(70+50, columna-160-15*i, str(c[i]['mapfre'])[0:30])
		p.drawString(120+50*2, columna-160-15*i, str(c[i]['positiva'])[0:30])
		p.drawString(170+50*3, columna-160-15*i, str(c[i]['rimac'])[0:30])
		#p.drawString(250+50*4, 700-15*i, str(c[i]['pacifico']))
		p.drawString(250+50*5, columna-160-15*i, str(c[i]['hdi'])[0:30])

	columna =columna-15*i


	p.setFillColorRGB(1,0.54902,0)
	p.rect(20,columna-180,7.5*inch,.15*inch, fill=1)
	p.setFillColorRGB(0,0,0)
	p.drawString(22, columna-180+3, "Deducibles")
	
	for k in range(0,14):


		d[k]['deducible'] = d[k]['deducible'].encode('ascii','ignore').encode('ascii','replace')
		d[k]['mapfre'] = d[k]['mapfre'].encode('ascii','ignore').encode('ascii','replace')
		d[k]['positiva']= d[k]['positiva'].encode('ascii','ignore').encode('ascii','replace')
		d[k]['rimac']= d[k]['rimac'].encode('ascii','ignore').encode('ascii','replace')
		#d[i]['pacifico']= d[i]['pacifico'].encode('ascii','ignore').encode('ascii','replace')
		d[k]['hdi']= d[k]['hdi'].encode('ascii','ignore').encode('ascii','replace')

		p.drawString(20, columna-200-15*k, str(d[k]['deducible'])[0:30])
		p.drawString(70+50, columna-200-15*k, str(d[k]['mapfre'])[0:30])
		p.drawString(120+50*2, columna-200-15*k, str(d[k]['positiva'])[0:30])
		p.drawString(170+50*3, columna-200-15*k, str(d[k]['rimac'])[0:30])
		#p.drawString(250+50*4, 320-15*i, str(d[i]['pacifico']))
		p.drawString(250+50*5, columna-200-15*k, str(d[k]['hdi'])[0:30])

	columna = columna-15*k


	p.setFillColorRGB(1,0.54902,0)
	p.rect(20,columna-220,7.5*inch,.15*inch, fill=1)
	p.setFillColorRGB(0,0,0)
	p.drawString(22, columna-220+3, "Servicios")
	

	for sk in range(0,5):


		s[sk]['services'] = s[sk]['services'].encode('ascii','ignore').encode('ascii','replace')
		s[sk]['mapfre'] = s[sk]['mapfre'].encode('ascii','ignore').encode('ascii','replace')
		s[sk]['positiva']= s[sk]['positiva'].encode('ascii','ignore').encode('ascii','replace')
		s[sk]['rimac']= s[sk]['rimac'].encode('ascii','ignore').encode('ascii','replace')
		s[sk]['pacifico']= s[sk]['pacifico'].encode('ascii','ignore').encode('ascii','replace')
		s[sk]['hdi']= s[sk]['hdi'].encode('ascii','ignore').encode('ascii','replace')

		p.drawString(20, columna-240-15*sk, str(s[sk]['services'])[0:30])
		p.drawString(70+50, columna-240-15*sk, str(s[sk]['mapfre'])[0:30])
		p.drawString(120+50*2, columna-240-15*sk, str(s[sk]['positiva'])[0:30])
		p.drawString(170+50*3, columna-240-15*sk, str(s[sk]['rimac'])[0:30])
		p.drawString(220+50*4, columna-240-15*sk, str(s[sk]['pacifico'])[0:25])
		p.drawString(250+50*5, columna-240-15*sk, str(s[sk]['hdi'])[0:30])


	

	# Close the PDF object cleanly, and we're done.
	p.showPage()
	p.save()
	return response

@csrf_exempt
def recibetasas(request):

	data = json.loads(request.body)

	data = json.dumps(data)

	f = open('/var/www/html/cotiza.json', 'w')
	f.write(data)
	f.close()

	return HttpResponse('nologeado', content_type="application/json")

@csrf_exempt
def recibecliente(request):

	data = json.loads(request.body)

	data = json.dumps(data)

	f = open('/var/www/html/cliente.json', 'w')
	f.write(data)
	f.close()

	return HttpResponse('nologeado', content_type="application/json")

@csrf_exempt
def recibeservicios(request):

	data = json.loads(request.body)

	data = json.dumps(data)

	f = open('/var/www/html/servicios.json', 'w')
	f.write(data)
	f.close()

	return HttpResponse('nologeado', content_type="application/json")


@csrf_exempt
def recibecoberturas(request):

	data = json.loads(request.body)

	data = json.dumps(data)

	f = open('/var/www/html/coberturas.json', 'w')
	f.write(data)
	f.close()



	return HttpResponse('nologeado', content_type="application/json")

@csrf_exempt
def recibegps(request):

	data = json.loads(request.body)

	data = json.dumps(data)

	f = open('/var/www/html/gps.json', 'w')
	f.write(data)
	f.close()

	return HttpResponse('nologeado', content_type="application/json")


@csrf_exempt
def recibefinanciamiento(request):

	data = json.loads(request.body)

	data = json.dumps(data)

	f = open('/var/www/html/financiamiento.json', 'w')
	f.write(data)
	f.close()

	return HttpResponse('nologeado', content_type="application/json")

@csrf_exempt
def recibededucibles(request):

	data = json.loads(request.body)

	data = json.dumps(data)

	f = open('/var/www/html/deducibles.json', 'w')
	f.write(data)
	f.close()

	return HttpResponse('nologeado', content_type="application/json")



@csrf_exempt
def subir(request):

	send_mail('Hermes','Evento Enviado','cotiza@hermes.pe', ['joelunmsm@gmail.com'], fail_silently=False)

	return HttpResponse('mmmmmmmmm', content_type="application/json")

def generapdf(request):
	# Create the HttpResponse object with the appropriate PDF headers.

	for i in range(0,27):

		TasaAsegur.objects.filter(anio=28-i).update(anio=0+i)
	


	return HttpResponse('total', content_type="application/json")



@csrf_exempt
def estadologin(request):

	if request.user.is_authenticated():

		return HttpResponse('logeado', content_type="application/json")

	else:

		return HttpResponse('nologeado', content_type="application/json")




@csrf_exempt
def exportarcobertura(request,data):

	
			print 'EC...',data

			cobertura = str(data).split('a')[0].split('x')

			aseguradora = str(data).split('a')[1].split('x')

			print cobertura,aseguradora,type(cobertura),type([2])

			#['1'] ['1', '1'] <type 'list'> <type 'list'>

			
			c =CobertAsegur.objects.filter(programa_id__in=cobertura,id_aseg_id__in=aseguradora).values('id','tipo__clase','antigued','programa__program','id_cob__descripcion','id_aseg__name_asegurad','id_uso__uso','modalidad__name_modalidad','value').order_by('-id')
			
			response = HttpResponse(content_type='text/csv')
			
			response['Content-Disposition'] = 'attachment; filename="Coberturas.csv"'

			writer = csv.writer(response)


			for x in c:

				#x['text_message'] = x['text_message'].encode('ascii','ignore')

				# x['text_message'] = x['text_message'].encode('ascii','replace')

				datos = x['id'],x['tipo__clase'],x['antigued'],x['programa__program'],x['id_cob__descripcion'],x['id_aseg__name_asegurad'],x['id_uso__uso'],x['modalidad__name_modalidad'],x['value']
				
				writer.writerow([datos])



			return response


@csrf_exempt
def exportarriesgo(request,data):

		auto = AutoValor.objects.all().values('id','id_modelo','id_modelo__name_model','id_marca__name_marca')

		for i in range(len(auto)):

			auto[i]['riesgo'] = ''

			auto[i]['aseguradora'] = ''

			if RiesgAseg.objects.filter(aseguradora_id=data,id_model_id=auto[i]['id_modelo']).values('id_riesg__tipo_riesgo').count()>0:

				auto[i]['riesgo'] = RiesgAseg.objects.filter(aseguradora_id=data,id_model_id=auto[i]['id_modelo']).values('id_riesg__tipo_riesgo')[0]['id_riesg__tipo_riesgo']

				auto[i]['aseguradora'] = RiesgAseg.objects.filter(aseguradora_id=data).values('aseguradora__name_asegurad')[0]['aseguradora__name_asegurad']

				print auto[i]['riesgo']


		response = HttpResponse(content_type='text/csv')
		
		response['Content-Disposition'] = 'attachment; filename="Riesgos.csv"'

		writer = csv.writer(response)


		for a in auto:


			datos = a['id'],a['riesgo'],a['id_modelo__name_model'],a['id_marca__name_marca'],a['aseguradora']
			
			writer.writerow([datos])



		return response



@csrf_exempt
def exportardeducible(request,data):

	

			cobertura = str(data).split('a')[0].split('x')

			aseguradora = str(data).split('a')[1].split('x')

			print cobertura,aseguradora,type(cobertura),type([2])

			
			c =DeducAsegur.objects.filter(id_deduc_id__in=cobertura,id_aseg_id__in=aseguradora).values('riesgo__tipo_riesgo','programa__program','id_deduc__deducible','id_aseg__name_asegurad','id_uso__uso','tipo__clase','value','modalidad__name_modalidad','value').order_by('-id')

			response = HttpResponse(content_type='text/csv')
			
			response['Content-Disposition'] = 'attachment; filename="Deducible.csv"'

			writer = csv.writer(response)


			for x in c:

				#x['text_message'] = x['text_message'].encode('ascii','ignore')

				# x['text_message'] = x['text_message'].encode('ascii','replace')

				datos = x['riesgo__tipo_riesgo'],x['programa__program'],x['id_deduc__deducible'],x['id_aseg__name_asegurad'],x['id_uso__uso'],x['tipo__clase'],x['value'],x['modalidad__name_modalidad'],x['value']


				writer.writerow([datos])



			return response

@csrf_exempt
def tasaadmin(request):

		if request.method == 'POST':


			demision = Parametros.objects.get(id=1).d_emision

			igv = Parametros.objects.get(id=1).igv

			monto = json.loads(request.body)['monto']['precio']
			data = json.loads(request.body)['data']


			print '::::::::::::',data

			tasahdi = data['tasahdi']
			tasarimac = data['tasarimac']
			tasapositiva = data['tasapositiva']
			tasapacifico = data['tasapacifico']
			tasamapfre = data['tasamapfre']

			aseguradora = Aseguradora.objects.all().values('id_asegurad','name_asegurad').order_by('name_asegurad')

			for i in range(len(aseguradora)):

				if aseguradora[i]['id_asegurad'] == 3:

					aseguradora[i]['tasahdi'] = round(float(tasahdi),2)

					aseguradora[i]['hdi'] = round(float(tasahdi)/100*float(monto),2)
					
					aseguradora[i]['phdisubtotal'] = round((100+float(demision))*float(aseguradora[i]['hdi'])/100,2)

					aseguradora[i]['phditotal'] = round((100+float(igv))*aseguradora[i]['phdisubtotal']/100,2)


				if aseguradora[i]['id_asegurad'] == 1:

					aseguradora[i]['tasapositiva'] = round(float(tasapositiva),2)

					aseguradora[i]['positiva'] = round(float(tasapositiva)/100*float(monto),2)

					aseguradora[i]['positivasubtotal'] = round((100+float(demision))*aseguradora[i]['positiva']/100,2)

					aseguradora[i]['positivatotal'] = round((100+float(igv))*aseguradora[i]['positivasubtotal']/100,2)
			
				if aseguradora[i]['id_asegurad'] == 2:

	
					aseguradora[i]['tasapacifico'] = round(float(tasapacifico),2)

					aseguradora[i]['pacifico'] = round(float(tasapacifico)/100*float(monto),2)

					aseguradora[i]['pacificosubtotal'] = round((100+float(demision))*aseguradora[i]['pacifico']/100,2)

					aseguradora[i]['pacificototal'] = round((100+int(igv))*aseguradora[i]['pacificosubtotal']/100,2)
			


				else:

					aseguradora[i]['pacifico'] = 'Consultar en la URL:'

					aseguradora[i]['pacificosubtotal'] = 'http://pacifico.com'

					aseguradora[i]['pacificototal'] = ''


				if aseguradora[i]['id_asegurad'] == 4:


						aseguradora[i]['tasamapfre'] = round(float(tasamapfre),2)

						aseguradora[i]['mapfre'] = round(float(tasamapfre)/100*float(monto),2)

						aseguradora[i]['mapfresubtotal'] = round((100+float(demision))*aseguradora[i]['mapfre']/100,2)

						aseguradora[i]['mapfretotal'] = round((100+float(igv))*aseguradora[i]['mapfresubtotal']/100,2)



				if aseguradora[i]['id_asegurad'] == 5:

						
						aseguradora[i]['tasarimac'] = round(float(tasarimac),2)

						aseguradora[i]['rimac'] = round(float(tasarimac)/100*float(monto),2)

						aseguradora[i]['rimacsubtotal'] = round((100+float(demision))*aseguradora[i]['rimac']/100,2)

						aseguradora[i]['rimactotal'] = round((100+float(igv))*aseguradora[i]['rimacsubtotal']/100,2)



			data_dict = ValuesQuerySetToDict(aseguradora)

			data = json.dumps(data_dict)


			return HttpResponse(data, content_type="application/json")



	


@csrf_exempt
def logearse(request):

	if request.user.is_authenticated():

		return HttpResponse('logeado', content_type="application/json")

	else:

		if request.method == 'POST':

			data = json.loads(request.body)

			user = json.loads(request.body)['username']
			
			psw = json.loads(request.body)['password']

			user = authenticate(username=user, password=psw)

			if user is not None:

				if user.is_active:

					login(request, user)

					return HttpResponse('logeado', content_type="application/json")

			else:
					
					return HttpResponse('noautorizado', content_type="application/json")
		


		return HttpResponse('nologeado', content_type="application/json")


@csrf_exempt
def parametros(request):

	data = request.body


	igv = data['igv']
	demision = data['demision']

	Parametros(igv=igv,d_emision=demision).save()

	return HttpResponse('data', content_type="application/json")


	fullname = models.CharField(max_length=100, blank=True)
	email = models.CharField(max_length=50, blank=True)
	chose_informat = models.IntegerField()


@csrf_exempt
def customers(request):

	d=Clientes.objects.all().values('id_cliente','fullname','email','chose_informat').order_by('id_cliente')

	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def listparametros(request):

	p= Parametros.objects.all().values('igv','d_emision').order_by('-id')

	data_dict = ValuesQuerySetToDict(p)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def listprimas(request):

	p= Primas.objects.all().values('id','aseguradora__name_asegurad','riesgo__tipo_riesgo','programa__program','primaminima').order_by('-id')

	print 'Primas...',p.count()

	data_dict = ValuesQuerySetToDict(p)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def addigv(request):

	data =  json.loads(request.body)

	igv = data['igv']
	demision = data['demision']

	p = Parametros.objects.get(id=1)
	p.igv = igv
	p.d_emision = demision
	p.save()

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def asegprogram(request,aseguradora):

	aseg = ProgAseg.objects.filter(id_aseg_id=aseguradora).values('id_prog','id_prog__program')

	data_dict = ValuesQuerySetToDict(aseg)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def pdfx(request):

	urlx = request.body

	print 'Generando PDF....',urlx

	f = open('/var/www/pdf.txt', 'a')
	f.write(str(urlx)+'\n')
	f.close()


	os.system('wkhtmltopdf '+urlx+' /var/www/html/output.pdf')

	return HttpResponse('data', content_type="application/json")

@csrf_exempt
def marca(request):

	d=Marca.objects.all().values('id_marca','name_marca')

	data_dict = ValuesQuerySetToDict(d)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")



@csrf_exempt
def modelo(request,id_marca):

	d=AutoValor.objects.filter(id_marca_id=id_marca).values('id_modelo','id_modelo__name_model','id_marca').annotate(model=Max('id_modelo__name_model')).order_by('id_modelo__name_model')
	
	data_dict = ValuesQuerySetToDict(d)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def listmodelo(request):

	d=Modelo.objects.all().values('id_model','name_model').order_by('-id_model');
	
	data_dict = ValuesQuerySetToDict(d)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def clase(request):
	
	d=Clase.objects.all().values('id_clase','clase').order_by('id_clase')
	
	data_dict = ValuesQuerySetToDict(d)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def catemodelo(request,modelo):


	modelos = AutoValor.objects.filter(id_modelo=modelo).values('id_modelo','id_modelo__name_model','id_marca__name_marca')

	for i in range(len(modelos)):

		if modelos[i]['id_marca__name_marca'] == 'Toyota' or modelos[i]['id_marca__name_marca'] == 'Nissan' :

			cat = 2

		else:

			cat = 1

	return HttpResponse(cat, content_type="application/json")


@csrf_exempt
def claseModelo(request,id_model):

	d=AutoValor.objects.filter(id_modelo=id_model).values('id','id_tipo','id_tipo__clase','id_modelo')
	
	data_dict = ValuesQuerySetToDict(d)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def riesgosclase(request):

	d = RiesgAseg.objects.all().values('aseguradora__name_asegurad','id_model__id_marca__name_marca','id_model__id_tipo__clase','id_riesg__tipo_riesgo','id_model__id_modelo__name_model','id').order_by('-id');
	
	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def datosfiltro(request,id_cliente):

	d = Clientes.objects.filter(id_cliente=id_cliente).values('id_cliente','fullname','email','celular','chose_marca__name_marca','chose_modelo__name_model','chose_tipo__clase','chose_timon__name_tipo','chose_modalid__name_modalidad','chose_uso__uso','chose_anio__anio_antig','chose_ubicl','chose_ubicp','chose_informat','value');
	
	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def categorias(request):

	d=Categorias.objects.all().values('id_categ','categoria').order_by('id_categ')

	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def anio(request):

	d=Anio.objects.all().values('id_anio','anio_antig').order_by('-id_anio')

	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def programas(request):

	d=Programa.objects.all().values('id_program','program').order_by('id_program')

	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def aseguradoras(request):

	d=Aseguradora.objects.all().values('id_asegurad','name_asegurad').order_by('id_asegurad')

	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def coberturas(request):

	d=Cobertura.objects.all().values('id_cobert','descripcion').order_by('id_cobert')

	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def deducciones(request):

	d=Deducibles.objects.all().values('id_deduc','deducible').order_by('id_deduc')

	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def financiamiento(request):

	d=FinanAsegu.objects.values('id','id_finan','id_finan__financiamiento','id_aseg','id_aseg__name_asegurad','cuota','tea')

	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


def pdfmargarita(request):


	return render(request, 'pdfmargarita.html')



def generate_pdf_view(request):

	try:
		# create an API client instance
		client = pdfcrowd.Client("username", "apikey")

		# convert an HTML file
		output_file = open('file.pdf', 'wb')
		client.convertFile('/var/www/cotizacion/frontend/resultadofiltro.html', output_file)
		output_file.close()

	except pdfcrowd.Error, why:
		print('Failed: {}'.format(why))

	return HttpResponse(output_file, content_type="application/json")

@csrf_exempt
def fiiiii(request):

	print 'Financiamiento......',json.loads(request.body)

	data = json.loads(request.body)


	body = ''

	financiamiento = Financiamiento.objects.all().values('id_financ','financiamiento').order_by('id_financ')

	print type(financiamiento)

	lista = []

	cober = []

	modelo = data['modelo']

	anio = data['anio']

	monto = data['precio']

	uso = data['uso']

	a = AutoValor.objects.filter(id_modelo_id=modelo)

	for m in a:

		tipo = m.id_tipo.id_clase

	print 'monto',monto

	if RiesgAseg.objects.filter(aseguradora_id=1,id_model_id=modelo):

		riesgopositiva = RiesgAseg.objects.get(aseguradora_id=1,id_model_id=modelo).id_riesg__tipo_riesgo
	
	if RiesgAseg.objects.filter(aseguradora_id=2,id_model_id=modelo):

		riesgopacifico = RiesgAseg.objects.get(aseguradora_id=2,id_model_id=modelo).id_riesg__tipo_riesgo
	
	if RiesgAseg.objects.filter(aseguradora_id=4,id_model_id=modelo):
	
		riesgomapfre = RiesgAseg.objects.get(aseguradora_id=4,id_model_id=modelo).id_riesg__tipo_riesgo
	
	if RiesgAseg.objects.filter(aseguradora_id=5,id_model_id=modelo):

		riesgorimac = RiesgAseg.objects.get(aseguradora_id=5,id_model_id=modelo).id_riesg__tipo_riesgo

	riesgohdi = 3
	riesgorimac= 3
	riesgopositiva = 3
	riesgomapfre = 3
	riesgopacifico = 3

	print 'riesgopacifico,riesgohdi,riesgopacifico,riesgorimac,riesgopositiva,riesgomapfre',riesgopacifico,riesgohdi,riesgopacifico,riesgorimac,riesgopositiva,riesgomapfre

	anio = int(Anio.objects.get(id_anio=anio).anio_antig)

	anioact = int(datetime.datetime.now().year)

	anio = anioact - anio

	demision = Parametros.objects.get(id=1).d_emision

	igv = Parametros.objects.get(id=1).igv

	aseguradora = Aseguradora.objects.all().values('id_asegurad','name_asegurad').order_by('name_asegurad')



	for i in range(len(financiamiento)):

		if FinanAsegu.objects.filter(id_finan=financiamiento[i]['id_financ'],id_aseg=3).count()==1:

			h = TasaAsegur.objects.filter(id_aseg_id=3,riesgo_id=riesgohdi,anio=anio)

			print 'Tasa PHDI.............', h.count() ,riesgohdi,anio

			if h.count() == 1:

				tasa = round(float(TasaAsegur.objects.get(id_aseg_id=3,riesgo_id=riesgohdi,anio=anio).value),2)

				PN= round(float(tasa)*float(monto)/100,2)

				m1 = round(float(igv)/100+1,2)

				m2 = round(float(PN)*float(m1),2)

				m3 = round(float(demision)/100+1,2)

				PT = round(float(m3)*float(m2),2)


				if int(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=3).cuota)==4:

					fact=round(float(PT)/4,2)

					print 'fact 4' , fact

				elif int(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=3).cuota)==11:

					part1= round(float(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=3).tea)+1,4)

					fact=round((float(PT)*part1)/11,2)

					print 'part1 11' , part1
					print 'fact 11' , fact

				else:

					part2= round(float(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=3).tea)+1,4)

					fact=round((float(PT)*part2)/12,2)

					print 'part1 12' , part2
					print 'fact 12' , fact

			financiamiento[i]['hdi'] = FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=3).cuota+str(" CUOTAS de  ")+str(fact)

		
		print 'sdfgsdfgsdfg',FinanAsegu.objects.filter(id_finan=financiamiento[i]['id_financ'],id_aseg=1).count()


		

		if FinanAsegu.objects.filter(id_finan=financiamiento[i]['id_financ'],id_aseg=1).count()==1:
			

			h = TasaAsegur.objects.filter(id_aseg_id=1,anio=anio,riesgo_id=riesgopositiva,id_uso_id=uso,tipo_id=tipo)


			print 'Tasa POSITIVAAAAAAAAAA.............', h.count() ,riesgopositiva,anio


			if h.count() == 1:

				tasa = round(float(TasaAsegur.objects.get(id_aseg_id=1,anio=anio,riesgo_id=riesgopositiva,id_uso_id=uso,tipo_id=tipo).value),2)

				print 'TASA POSITIVAAAAAAAAAA ......' ,tasa

				PN= round(float(tasa)*float(monto)/100,2)

				print 'POSTIVIA PRIMA NETAAAAAAAAAA ......' ,PN

				m1 = round(float(igv)/100+1,2)

				m2 = round(float(PN)*float(m1),2)

				m3 = round(float(demision)/100+1,2)

				PT = round(float(m3)*float(m2),2)

				print 'POSTIVIA PRIMA TOTAL ......' ,PT

				if int(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=1).cuota)==5:

					fact=round(float(PT)/5,4)

					print 'fact 4' , fact

				elif int(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=1).cuota)==10:

					part1= round(float(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=1).tea)+1,4)

					fact=round((float(PT)*part1)/10,2)

					print 'part1 11' , part1
					print 'fact 11' , fact

				else:

					part2= round(float(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=1).tea)+1,4)

					fact=round((float(PT)*part2)/12,2)

					print 'part1 12' , part2
					print 'fact 12' , fact

			financiamiento[i]['positiva'] = FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=1).cuota+str(" CUOTAS de  ")+str(fact)

		

		if FinanAsegu.objects.filter(id_finan=financiamiento[i]['id_financ'],id_aseg=2).count()==1:

			h = TasaAsegur.objects.filter(id_aseg_id=2,riesgo_id=riesgopacifico,anio=anio)

			print 'Tasa PACIFICO.............', h.count() ,riesgopacifico,anio

			if h.count() == 1:

				tasa = round(float(TasaAsegur.objects.get(id_aseg_id=2,riesgo_id=riesgopacifico,anio=anio).value),2)

				PN= round(float(tasa)*float(monto)/100,2)

				m1 = round(float(igv)/100+1,2)

				m2 = round(float(PN)*float(m1),2)

				m3 = round(float(demision)/100+1,2)

				PT = round(float(m3)*float(m2),2)


				if int(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=2).cuota)==4:

					fact=round(float(PT)/4,2)

					print 'fact 4' , fact

				elif int(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=2).tea)==0.082:

					part1= round(float(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=2).tea)+1,4)

					fact=round((float(PT)*part1)/10,2)

					print 'part1 11' , part1
					print 'fact 11' , fact

				else:

					part2= round(float(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=2).tea)+1,4)

					fact=round((float(PT)*part2)/10,2)

					print 'part1 12' , part2
					print 'fact 12' , fact

			financiamiento[i]['pacifico'] = FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=2).cuota+str(" CUOTAS de  ")+str(fact)




		if FinanAsegu.objects.filter(id_finan=financiamiento[i]['id_financ'],id_aseg=5).count()==1:


			h = TasaAsegur.objects.filter(id_aseg_id=5,riesgo_id=riesgorimac,anio=anio,tipo_id=tipo,ubicacion=1,id_uso_id=uso)

			print 'Tasa RIMAC.............', h.count() ,riesgorimac,anio

			if h.count() == 1:

				tasa = round(float(TasaAsegur.objects.get(id_aseg_id=5,riesgo_id=riesgorimac,anio=anio,tipo_id=tipo,ubicacion=1,id_uso_id=uso).value),2)

				PN= round(float(tasa)*float(monto)/100,2)

				m1 = round(float(igv)/100+1,2)

				m2 = round(float(PN)*float(m1),2)

				m3 = round(float(demision)/100+1,2)

				PT = round(float(m3)*float(m2),2)


				if int(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=5).cuota)==5:

					fact=round(float(PT)/5,2)

					print 'fact 4' , fact

				elif int(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=5).cuota)==10:

					part1= round(float(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=5).tea)+1,4)

					fact=round((float(PT)*part1)/10,2)

					print 'part1 11' , part1
					print 'fact 11' , fact

				else:

					part2= round(float(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=5).tea)+1,4)

					fact=round((float(PT)*part2)/12,2)

					print 'part1 12' , part2
					print 'fact 12' , fact

			financiamiento[i]['rimac'] = FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=5).cuota+str(" CUOTAS de  ")+str(fact)


		if FinanAsegu.objects.filter(id_finan=financiamiento[i]['id_financ'],id_aseg=5).count()==1:


			h = TasaAsegur.objects.filter(id_aseg_id=5,riesgo_id=riesgorimac,anio=anio,tipo_id=tipo,ubicacion=1,id_uso_id=uso)

			print 'Tasa RIMAC.............', h.count() ,riesgorimac,anio

			if h.count() == 1:

				tasa = round(float(TasaAsegur.objects.get(id_aseg_id=5,riesgo_id=riesgorimac,anio=anio,tipo_id=tipo,ubicacion=1,id_uso_id=uso).value),2)

				PN= round(float(tasa)*float(monto)/100,2)

				m1 = round(float(igv)/100+1,2)

				m2 = round(float(PN)*float(m1),2)

				m3 = round(float(demision)/100+1,2)

				PT = round(float(m3)*float(m2),2)


				if int(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=5).cuota)==5:

					fact=round(float(PT)/5,2)

					print 'fact 4' , fact

				elif int(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=5).cuota)==10:

					part1= round(float(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=5).tea)+1,4)

					fact=round((float(PT)*part1)/10,2)

					print 'part1 11' , part1
					print 'fact 11' , fact

				else:

					part2= round(float(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=5).tea)+1,4)

					fact=round((float(PT)*part2)/12,2)

					print 'part1 12' , part2
					print 'fact 12' , fact

			financiamiento[i]['rimac'] = FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=5).cuota+str(" CUOTAS de  ")+str(fact)



		if FinanAsegu.objects.filter(id_finan=financiamiento[i]['id_financ'],id_aseg=4).count()==1:


			h = TasaAsegur.objects.filter(id_aseg_id=4,anio=anio,id_uso_id=uso,riesgo_id=riesgomapfre,tipo_id=tipo)

			print 'Tasa MAPFRE.............', h.count() ,riesgomapfre,anio,uso

			if h.count() == 1:

				tasa = round(float(TasaAsegur.objects.get(id_aseg_id=4,riesgo_id=riesgomapfre,anio=anio,id_uso_id=uso,tipo_id=tipo).value),2)

				PN= round(float(tasa)*float(monto)/100,2)

				m1 = round(float(igv)/100+1,2)

				m2 = round(float(PN)*float(m1),2)

				m3 = round(float(demision)/100+1,2)

				PT = round(float(m3)*float(m2),2)


				if int(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=4).cuota)==4:

					fact=round(float(PT)/4,2)

					print 'fact 4' , fact

				elif int(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=4).cuota)==10:

					part1= round(float(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=4).tea)+1,4)

					fact=round((float(PT)*part1)/10,2)

					print 'part1 11' , part1
					print 'fact 11' , fact

				else:

					part2= round(float(FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=4).tea)+1,4)

					fact=round((float(PT)*part2)/12,2)

					print 'part1 12' , part2
					print 'fact 12' , fact

			financiamiento[i]['mapfre'] = FinanAsegu.objects.get(id_finan=financiamiento[i]['id_financ'],id_aseg=4).cuota+str(" CUOTAS de  ")+str(fact)


	data_dict = ValuesQuerySetToDict(financiamiento)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def primaneta(request):

	data = json.loads(request.body)

	print 'PrimaNeta',data

	monto = data['precio']


	orderId = data['orderId']
	uso = data['uso']
	modelo = data['modelo']

	a = AutoValor.objects.filter(id_modelo_id=modelo)

	for m in a:

		tipo = m.id_tipo.id_clase

	print 'monto',monto

	modalidad = data['modalidad']

	anio = data['anio']


	print 'ANIO.........',anio

	programa = data['programa']

	if RiesgAseg.objects.filter(aseguradora_id=1,id_model_id=modelo):

		riesgopositiva = RiesgAseg.objects.get(aseguradora_id=1,id_model_id=modelo).id_riesg__tipo_riesgo
	
	if RiesgAseg.objects.filter(aseguradora_id=2,id_model_id=modelo):

		riesgopacifico = RiesgAseg.objects.get(aseguradora_id=2,id_model_id=modelo).id_riesg__tipo_riesgo
	
	if RiesgAseg.objects.filter(aseguradora_id=4,id_model_id=modelo):
	
		riesgomapfre = RiesgAseg.objects.get(aseguradora_id=4,id_model_id=modelo).id_riesg__tipo_riesgo
	
	if RiesgAseg.objects.filter(aseguradora_id=5,id_model_id=modelo):

		riesgorimac = RiesgAseg.objects.get(aseguradora_id=5,id_model_id=modelo).id_riesg__tipo_riesgo

	riesgohdi = 3
	riesgorimac= 3
	riesgopositiva = 3
	riesgomapfre = 3
	riesgopacifico = 3

	print 'riesgopacifico,riesgohdi,riesgopacifico,riesgorimac,riesgopositiva,riesgomapfre',riesgopacifico,riesgohdi,riesgopacifico,riesgorimac,riesgopositiva,riesgomapfre

	anio = int(Anio.objects.get(id_anio=anio).anio_antig)

	anioact = int(datetime.datetime.now().year)

	anio = anioact - anio

	demision = Parametros.objects.get(id=1).d_emision

	igv = Parametros.objects.get(id=1).igv

	aseguradora = Aseguradora.objects.all().values('id_asegurad','name_asegurad').order_by('name_asegurad')

	for i in range(len(aseguradora)):

		if aseguradora[i]['id_asegurad'] == 3:

			h = TasaAsegur.objects.filter(id_aseg_id=3,riesgo_id=riesgohdi,anio=anio)

			print 'Tasa PHDI', h.count() ,riesgohdi,anio

			if h.count() == 1:

				aseguradora[i]['tasahdi'] = round(float(TasaAsegur.objects.get(id_aseg_id=3,riesgo_id=riesgohdi,anio=anio).value),2)
				
				print 'Value',aseguradora[i]['tasahdi']

				aseguradora[i]['hdi'] = round(float(TasaAsegur.objects.get(id_aseg_id=3,riesgo_id=riesgohdi,anio=anio).value)/100*float(monto),2)
				
				aseguradora[i]['phdisubtotal'] = round((100+float(demision))*float(aseguradora[i]['hdi'])/100,2)

				aseguradora[i]['phditotal'] = round((100+float(igv))*aseguradora[i]['phdisubtotal']/100,2)


		if aseguradora[i]['id_asegurad'] == 1:

			p= TasaAsegur.objects.filter(id_aseg_id=1,anio=anio,riesgo_id=riesgopositiva,tipo_id=tipo)

			print 'Tasa Positiva', p.count() ,'Riesgo' ,riesgopositiva,'Anio', anio,'Tipo',tipo

			if p.count()==1:

				aseguradora[i]['tasapositiva'] = round(float(TasaAsegur.objects.get(id_aseg_id=1,anio=anio,riesgo_id=riesgopositiva,id_uso_id=uso,tipo_id=tipo).value),2)

				print 'Tasa Positiva', p.count() ,riesgopositiva,anio,tipo,aseguradora[i]['tasapositiva'] 

				aseguradora[i]['positiva'] = round(float(TasaAsegur.objects.get(id_aseg_id=1,anio=anio,riesgo_id=riesgopositiva,id_uso_id=uso,tipo_id=tipo).value)/100*float(monto),2)

				aseguradora[i]['positivasubtotal'] = round((100+float(demision))*aseguradora[i]['positiva']/100,2)

				aseguradora[i]['positivatotal'] = round((100+float(igv))*aseguradora[i]['positivasubtotal']/100,2)
		
		if aseguradora[i]['id_asegurad'] == 2:

			if int(uso) == 1:


				t = TasaAsegur.objects.filter(id_aseg_id=2,anio=anio,riesgo_id=riesgopacifico)

				print 'Tasa Pacifico',t.count(),riesgopacifico,tipo,anio

				if t.count()==1:

					aseguradora[i]['tasapacifico'] = round(float(TasaAsegur.objects.get(id_aseg_id=2,anio=anio,riesgo_id=riesgopacifico).value),2)

					print aseguradora[i]['tasapacifico'] 

					aseguradora[i]['pacifico'] = round(float(TasaAsegur.objects.get(id_aseg_id=2,anio=anio,riesgo_id=riesgopacifico).value)/100*float(monto),2)

					aseguradora[i]['pacificosubtotal'] = round((100+float(demision))*aseguradora[i]['pacifico']/100,2)

					aseguradora[i]['pacificototal'] = round((100+int(igv))*aseguradora[i]['pacificosubtotal']/100,2)
			


			else:

				aseguradora[i]['pacifico'] = 'Consultar en la URL:'

				aseguradora[i]['pacificosubtotal'] = 'http://pacifico.com'

				aseguradora[i]['pacificototal'] = ''


		if aseguradora[i]['id_asegurad'] == 4:

			m = TasaAsegur.objects.filter(id_aseg_id=4,riesgo_id=riesgomapfre,anio=anio,tipo_id=tipo,ubicacion=1)

			print 'Tasa Mapfre', m.count(),riesgomapfre,anio,tipo

			if m.count()==1:

				aseguradora[i]['tasamapfre'] = round(float(TasaAsegur.objects.get(id_aseg_id=4,riesgo_id=riesgomapfre,anio=anio,tipo_id=tipo,ubicacion=1).value),2)

				aseguradora[i]['mapfre'] = round(float(TasaAsegur.objects.get(id_aseg_id=4,riesgo_id=riesgomapfre,anio=anio,tipo_id=tipo,ubicacion=1).value)/100*float(monto),2)

				aseguradora[i]['mapfresubtotal'] = round((100+float(demision))*aseguradora[i]['mapfre']/100,2)

				aseguradora[i]['mapfretotal'] = round((100+float(igv))*aseguradora[i]['mapfresubtotal']/100,2)



		if aseguradora[i]['id_asegurad'] == 5:

			r = TasaAsegur.objects.filter(id_aseg_id=5,anio=int(anio),id_uso_id=uso,riesgo_id=riesgorimac)

			if r.count()==1:

				print 'Tasa Rimac',r.count(),anio,uso
				
				aseguradora[i]['tasarimac'] = round(float(TasaAsegur.objects.get(id_aseg_id=5,anio=anio,id_uso_id=uso,riesgo_id=riesgorimac).value),2)

				aseguradora[i]['rimac'] = round(float(TasaAsegur.objects.get(id_aseg_id=5,anio=anio,id_uso_id=uso,riesgo_id=riesgorimac).value)/100*float(monto),2)

				aseguradora[i]['rimacsubtotal'] = round((100+float(demision))*aseguradora[i]['rimac']/100,2)

				aseguradora[i]['rimactotal'] = round((100+float(igv))*aseguradora[i]['rimacsubtotal']/100,2)



	data_dict = ValuesQuerySetToDict(aseguradora)

	data = json.dumps(data_dict)


	return HttpResponse(data, content_type="application/json")
'''
@csrf_exempt
def riesgos(request):

	d=Riesgo.objects.all().values('id_riesgo','tipo_riesgo').order_by('tipo_riesgo');

	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

'''
@csrf_exempt
def riesgomodelo(request,modelo):

	data=RiesgAseg.objects.filter(id_model=modelo).values('aseguradora__name_asegurad','id_model__id_modelo__name_model','id_model','id_riesg_id')

	data_dict = ValuesQuerySetToDict(data)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")



@csrf_exempt
def primaneta(request):

	data = json.loads(request.body)

	print 'PrimaNeta',data

	monto = data['precio']


	orderId = data['orderId']
	uso = data['uso']
	modelo = data['modelo']

	a = AutoValor.objects.filter(id_modelo_id=modelo)

	for m in a:

		tipo = m.id_tipo.id_clase

	print 'monto',monto

	modalidad = data['modalidad']

	anio = data['anio']


	print 'ANIO.........',anio

	programa = data['programa']

	if RiesgAseg.objects.filter(aseguradora_id=1,id_model_id=modelo):

		riesgopositiva = RiesgAseg.objects.get(aseguradora_id=1,id_model_id=modelo).id_riesg__tipo_riesgo
	
	if RiesgAseg.objects.filter(aseguradora_id=2,id_model_id=modelo):

		riesgopacifico = RiesgAseg.objects.get(aseguradora_id=2,id_model_id=modelo).id_riesg__tipo_riesgo
	
	if RiesgAseg.objects.filter(aseguradora_id=4,id_model_id=modelo):
	
		riesgomapfre = RiesgAseg.objects.get(aseguradora_id=4,id_model_id=modelo).id_riesg__tipo_riesgo
	
	if RiesgAseg.objects.filter(aseguradora_id=5,id_model_id=modelo):

		riesgorimac = RiesgAseg.objects.get(aseguradora_id=5,id_model_id=modelo).id_riesg__tipo_riesgo

	riesgohdi = 3
	riesgorimac= 3
	riesgopositiva = 3
	riesgomapfre = 3
	riesgopacifico = 3

	print 'riesgopacifico,riesgohdi,riesgopacifico,riesgorimac,riesgopositiva,riesgomapfre',riesgopacifico,riesgohdi,riesgopacifico,riesgorimac,riesgopositiva,riesgomapfre

	anio = int(Anio.objects.get(id_anio=anio).anio_antig)

	anioact = int(datetime.datetime.now().year)

	anio = anioact - anio

	demision = Parametros.objects.get(id=1).d_emision

	igv = Parametros.objects.get(id=1).igv

	aseguradora = Aseguradora.objects.all().values('id_asegurad','name_asegurad').order_by('name_asegurad')

	for i in range(len(aseguradora)):

		if aseguradora[i]['id_asegurad'] == 3:

			h = TasaAsegur.objects.filter(id_aseg_id=3,riesgo_id=riesgohdi,anio=anio)

			print 'Tasa PHDI', h.count() ,riesgohdi,anio

			if h.count() == 1:

				aseguradora[i]['tasahdi'] = round(float(TasaAsegur.objects.get(id_aseg_id=3,riesgo_id=riesgohdi,anio=anio).value),2)
				
				print 'Value',aseguradora[i]['tasahdi']

				aseguradora[i]['hdi'] = round(float(TasaAsegur.objects.get(id_aseg_id=3,riesgo_id=riesgohdi,anio=anio).value)/100*float(monto),2)
				
				aseguradora[i]['phdisubtotal'] = round((100+float(demision))*float(aseguradora[i]['hdi'])/100,2)

				aseguradora[i]['phditotal'] = round((100+float(igv))*aseguradora[i]['phdisubtotal']/100,2)


		if aseguradora[i]['id_asegurad'] == 1:

			p= TasaAsegur.objects.filter(id_aseg_id=1,anio=anio,riesgo_id=riesgopositiva,tipo_id=tipo)

			print 'Tasa Positiva', p.count() ,'Riesgo' ,riesgopositiva,'Anio', anio,'Tipo',tipo

			if p.count()==1:

				aseguradora[i]['tasapositiva'] = round(float(TasaAsegur.objects.get(id_aseg_id=1,anio=anio,riesgo_id=riesgopositiva,id_uso_id=uso,tipo_id=tipo).value),2)

				print 'Tasa Positiva', p.count() ,riesgopositiva,anio,tipo,aseguradora[i]['tasapositiva'] 

				aseguradora[i]['positiva'] = round(float(TasaAsegur.objects.get(id_aseg_id=1,anio=anio,riesgo_id=riesgopositiva,id_uso_id=uso,tipo_id=tipo).value)/100*float(monto),2)

				aseguradora[i]['positivasubtotal'] = round((100+float(demision))*aseguradora[i]['positiva']/100,2)

				aseguradora[i]['positivatotal'] = round((100+float(igv))*aseguradora[i]['positivasubtotal']/100,2)
		
		if aseguradora[i]['id_asegurad'] == 2:

			if int(uso) == 1:


				t = TasaAsegur.objects.filter(id_aseg_id=2,anio=anio,riesgo_id=riesgopacifico)

				print 'Tasa Pacifico',t.count(),riesgopacifico,tipo,anio

				if t.count()==1:

					aseguradora[i]['tasapacifico'] = round(float(TasaAsegur.objects.get(id_aseg_id=2,anio=anio,riesgo_id=riesgopacifico).value),2)

					print aseguradora[i]['tasapacifico'] 

					aseguradora[i]['pacifico'] = round(float(TasaAsegur.objects.get(id_aseg_id=2,anio=anio,riesgo_id=riesgopacifico).value)/100*float(monto),2)

					aseguradora[i]['pacificosubtotal'] = round((100+float(demision))*aseguradora[i]['pacifico']/100,2)

					aseguradora[i]['pacificototal'] = round((100+int(igv))*aseguradora[i]['pacificosubtotal']/100,2)
			


			else:

				aseguradora[i]['pacifico'] = 'Consultar en la URL:'

				aseguradora[i]['pacificosubtotal'] = 'http://pacifico.com'

				aseguradora[i]['pacificototal'] = ''


		if aseguradora[i]['id_asegurad'] == 4:

			m = TasaAsegur.objects.filter(id_aseg_id=4,riesgo_id=riesgomapfre,anio=anio,tipo_id=tipo,ubicacion=1)

			print 'Tasa Mapfre', m.count(),riesgomapfre,anio,tipo

			if m.count()==1:

				aseguradora[i]['tasamapfre'] = round(float(TasaAsegur.objects.get(id_aseg_id=4,riesgo_id=riesgomapfre,anio=anio,tipo_id=tipo,ubicacion=1).value),2)

				aseguradora[i]['mapfre'] = round(float(TasaAsegur.objects.get(id_aseg_id=4,riesgo_id=riesgomapfre,anio=anio,tipo_id=tipo,ubicacion=1).value)/100*float(monto),2)

				aseguradora[i]['mapfresubtotal'] = round((100+float(demision))*aseguradora[i]['mapfre']/100,2)

				aseguradora[i]['mapfretotal'] = round((100+float(igv))*aseguradora[i]['mapfresubtotal']/100,2)



		if aseguradora[i]['id_asegurad'] == 5:

			r = TasaAsegur.objects.filter(id_aseg_id=5,anio=int(anio),id_uso_id=uso,riesgo_id=riesgorimac)

			if r.count()==1:

				print 'Tasa Rimac',r.count(),anio,uso
				
				aseguradora[i]['tasarimac'] = round(float(TasaAsegur.objects.get(id_aseg_id=5,anio=anio,id_uso_id=uso,riesgo_id=riesgorimac).value),2)

				aseguradora[i]['rimac'] = round(float(TasaAsegur.objects.get(id_aseg_id=5,anio=anio,id_uso_id=uso,riesgo_id=riesgorimac).value)/100*float(monto),2)

				aseguradora[i]['rimacsubtotal'] = round((100+float(demision))*aseguradora[i]['rimac']/100,2)

				aseguradora[i]['rimactotal'] = round((100+float(igv))*aseguradora[i]['rimacsubtotal']/100,2)



	data_dict = ValuesQuerySetToDict(aseguradora)

	data = json.dumps(data_dict)


	return HttpResponse(data, content_type="application/json")



@csrf_exempt
def riesgos(request):

	d=Riesgo.objects.all().values('id_riesgo','tipo_riesgo').order_by('tipo_riesgo');

	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def listagps2(request):


	d=Gps.objects.filter(value=1).values('sumaminima','id','id_aseg__name_asegurad','id_prog__program','value').order_by('-id')[:10]

	print d.count()

	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def listagps(request):


	d=Gps.objects.all().exclude(value=1).values('sumaminima','id','id_aseg__name_asegurad','id_prog__program','id_auto__id_modelo__name_model','id_auto__id_marca__name_marca','id_auto__id_modelo__name_model','id_uso__uso','anio_antig','value','anio_antig__anio_antig').order_by('-id')[:10]

	print d.count()

	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")



@csrf_exempt
def riesgomodelo(request,modelo):

	data=RiesgAseg.objects.filter(id_model=modelo).values('aseguradora__name_asegurad','id_model__id_modelo__name_model','id_model','id_riesg_id')

	data_dict = ValuesQuerySetToDict(data)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def getgps(request,modelo):


	print 'Modelo....',modelo
	gpspositiva = 'No'
	gpsrimac = 'No'
	gpspacifico = 'No'
	gpsmapfre = 'No'
	gpshdi = 'No'

	auto =AutoValor.objects.filter(id_modelo_id=modelo)

	for a in auto:
		id_auto = a.id

		'''
		f = open('/var/www/html/gps.txt', 'a')
		f.write(str(modelo)+' '+str(id_auto)+'\n')
		f.close()
		'''

		if Gps.objects.filter(id_auto =id_auto,id_aseg=1).count() > 0 :
			gpspositiva = 'Si'
		if Gps.objects.filter(id_auto =id_auto,id_aseg=5).count() > 0:
			gpsrimac = 'Si'
		if Gps.objects.filter(id_auto =id_auto,id_aseg=2).count() > 0:
			gpspacifico = 'Si'
		if Gps.objects.filter(id_auto =id_auto,id_aseg=4).count() > 0:
			gpsmapfre = 'Si'
		if Gps.objects.filter(id_auto =id_auto,id_aseg=3).count() > 0:
			gpshdi = 'Si'

	print id_auto

	'''
	f = open('/var/www/html/gps.txt', 'a')
	f.write('......'+'\n')
	f.close()
	'''
	

	

	

	data = {'gpshdi':gpshdi,'gpsmapfre':gpsmapfre,'gpsrimac':gpsrimac,'gpspacifico':gpspacifico,'gpspositiva':gpspositiva}

	data = json.dumps(data)
	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def cobertura(request,orden_id,uso,anio,modalidad,programa,modelo):


	tipo = AutoValor.objects.filter(id_modelo_id=modelo)

	for t in tipo:

		tipo = t.id_tipo_id

	pro = programa.split('z')

	promapfre = pro[0]
	propositiva = pro[2]
	prorimac = pro[1]

	body = ''

	today = date.today()

	anio = Anio.objects.get(id_anio=anio).anio_antig

	difanio =  int(today.year)-int(anio)

	print 'difanio',difanio

	anioset = 10
	

	if difanio <= 10 :

		anioset = 10

	if difanio > 10 and difanio <= 15:

		anioset = 15

	if difanio > 15 and difanio <= 20:

		anioset = 20
	

	print 'Anioset.........................................................',anioset

	if RiesgAseg.objects.filter(aseguradora_id=1,id_model_id=modelo):

		riesgopositiva = RiesgAseg.objects.get(aseguradora_id=1,id_model_id=modelo).id_riesg__tipo_riesgo
	
	if RiesgAseg.objects.filter(aseguradora_id=2,id_model_id=modelo):

		riesgopacifico = RiesgAseg.objects.get(aseguradora_id=2,id_model_id=modelo).id_riesg__tipo_riesgo
	
	if RiesgAseg.objects.filter(aseguradora_id=4,id_model_id=modelo):
	
		riesgomapfre = RiesgAseg.objects.get(aseguradora_id=4,id_model_id=modelo).id_riesg__tipo_riesgo
	
	if RiesgAseg.objects.filter(aseguradora_id=5,id_model_id=modelo):

		riesgorimac = RiesgAseg.objects.get(aseguradora_id=5,id_model_id=modelo).id_riesg__tipo_riesgo

	cobertura = Cobertura.objects.all().values('id_cobert','descripcion').order_by('id_cobert')

	lista = []

	cober = []


	for i in range(len(cobertura)):

		cobertura[0]['rimac'] = 'Valor Pactado'
		cobertura[1]['rimac'] = 'Valor Pactado'
		cobertura[2]['rimac'] = 'Valor Pactado'
		cobertura[3]['rimac'] = 'US$ 150 000'
		cobertura[4]['rimac'] = 'US$ 80000 x Vehiculo'
		cobertura[5]['rimac'] = 'Max 5 ocupantes'
		cobertura[6]['rimac'] = 'US$ 20 000'
		cobertura[7]['rimac'] = 'US$ 4 000'
		cobertura[8]['rimac'] = 'US$ 2 000'
		cobertura[9]['rimac'] = 'No Aplica'
		cobertura[10]['rimac'] = 'US$ 1000'
		cobertura[11]['rimac'] = 'US$ 1500'
		cobertura[12]['rimac'] = 'Persona Juridica o Endoso al Banco'
		cobertura[13]['rimac'] = 'US$ 50000'
		cobertura[14]['rimac'] = 'Valor Pactado'
		cobertura[15]['rimac'] = 'US$ 10000'
		cobertura[16]['rimac'] = 'Si cubre'
		cobertura[17]['rimac'] = 'No aplica'
		break

	for i in range(len(cobertura)):
		
		cobertura[0]['positiva'] = 'Valor Asegurado'
		cobertura[1]['positiva'] = 'Valor Asegurado'
		cobertura[2]['positiva'] = 'Valor Asegurado'
		cobertura[3]['positiva'] = 'US$ 150 000'
		cobertura[4]['positiva'] = 'US$ 50000 x Vehiculo'
		cobertura[5]['positiva'] = 'Max 5 ocupantes'
		cobertura[6]['positiva'] = 'US$ 20 000'
		cobertura[7]['positiva'] = 'US$ 4 000'
		cobertura[8]['positiva'] = 'US$ 1 000'
		cobertura[9]['positiva'] = 'No Aplica'
		cobertura[10]['positiva'] = 'US$ 1 000'
		cobertura[11]['positiva'] = 'Dentro del valor del vehiculo'
		cobertura[12]['positiva'] = 'Endoso al Banco'
		cobertura[13]['positiva'] = 'US$ 50000'
		cobertura[14]['positiva'] = 'Valor Asegurado'
		cobertura[15]['positiva'] = 'US$ 10000'
		cobertura[16]['positiva'] = 'Si cubre'
		cobertura[17]['positiva'] = 'No aplica'
		break

	for i in range(len(cobertura)):
		
		cobertura[0]['mapfre'] = 'Valor Pactado (Hasta 120% del valor comercial)'
		cobertura[1]['mapfre'] = 'Valor Pactado (Hasta 120% del valor comercial)'
		cobertura[2]['mapfre'] = 'Valor Pactado (Hasta 120% del valor comercial)'
		cobertura[3]['mapfre'] = 'US$ 150 000'
		cobertura[4]['mapfre'] = 'US$ 50000 x Vehiculo'
		cobertura[5]['mapfre'] = 'Max 5 ocupantes'
		cobertura[6]['mapfre'] = 'US$ 20 000'
		cobertura[7]['mapfre'] = 'US$ 4 000'
		cobertura[8]['mapfre'] = 'US$ 2 000'
		cobertura[9]['mapfre'] = 'US$ 10 000 (piloto y copiloto)'
		cobertura[10]['mapfre'] = 'Originales sin limite, No originales US$ 1000'
		cobertura[11]['mapfre'] = 'US$ 1500'
		cobertura[12]['mapfre'] = 'Persona Juridica o Endoso al Banco'
		cobertura[13]['mapfre'] = 'US$ 50000'
		cobertura[14]['mapfre'] = 'No Aplica'
		cobertura[15]['mapfre'] = 'No Aplica'
		cobertura[16]['mapfre'] = 'Si cubre'
		cobertura[17]['mapfre'] = 'US$ 500'
		break



	for i in range(len(cobertura)):

		cober.append(i)

		if CobertAsegur.objects.filter(id_cob=cobertura[i]['id_cobert'],id_aseg_id=3,id_uso=uso).count()==1:

			lista.append(i)

			cobertura[i]['hdi'] = CobertAsegur.objects.get(id_cob=cobertura[i]['id_cobert'],id_aseg_id=3,id_uso=uso).value

		p = CobertAsegur.objects.filter(id_cob=cobertura[i]['id_cobert'],id_aseg_id=1,id_uso=uso,modalidad_id=modalidad,antigued=20,programa_id=propositiva).values('programa__program','antigued')
			
		if p.count()==1:

			lista.append(i)

			cobertura[i]['positiva'] = CobertAsegur.objects.get(id_cob=cobertura[i]['id_cobert'],id_aseg_id=1,id_uso=uso,antigued=20,modalidad_id=modalidad,programa_id=propositiva).value

		if CobertAsegur.objects.filter(id_cob=cobertura[i]['id_cobert'],id_aseg_id=2,id_uso_id= uso).count()==1:

			lista.append(i)

			cobertura[i]['pacifico'] = CobertAsegur.objects.get(id_cob=cobertura[i]['id_cobert'],id_aseg_id=2,id_uso_id= uso).value

		p = CobertAsegur.objects.filter(id_cob=cobertura[i]['id_cobert'],id_aseg_id=4,id_uso=uso,programa_id=promapfre,tipo_id=tipo).values('programa__program','antigued','id_cob')

		if p.count()==1:
		
			lista.append(i)

			cobertura[i]['mapfre'] = CobertAsegur.objects.get(id_cob=cobertura[i]['id_cobert'],id_aseg_id=4,id_uso=uso,programa_id=promapfre,tipo_id=tipo).value

		p = CobertAsegur.objects.filter(id_cob=cobertura[i]['id_cobert'],id_aseg_id=5,id_uso_id=uso,programa_id=prorimac)
		
		if p.count()==1:

			lista.append(i)
			
			cobertura[i]['rimac'] = CobertAsegur.objects.get(id_cob=cobertura[i]['id_cobert'],id_aseg_id=5,id_uso_id=uso,programa_id=prorimac).value


	data_dict = ValuesQuerySetToDict(cobertura)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def deducible(request,orden_id,uso,anio,modalidad,programa,modelo):

	tipo = AutoValor.objects.filter(id_modelo_id=modelo)

	riesgomapfre = 3

	if RiesgAseg.objects.filter(aseguradora_id=1,id_model_id=modelo):

		riesgopositiva = RiesgAseg.objects.get(aseguradora_id=1,id_model_id=modelo).id_riesg__tipo_riesgo
	
	if RiesgAseg.objects.filter(aseguradora_id=2,id_model_id=modelo):

		riesgopacifico = RiesgAseg.objects.get(aseguradora_id=2,id_model_id=modelo).id_riesg__tipo_riesgo
	
	if RiesgAseg.objects.filter(aseguradora_id=4,id_model_id=modelo):
	
		riesgomapfre = RiesgAseg.objects.get(aseguradora_id=4,id_model_id=modelo).id_riesg__tipo_riesgo
	
	if RiesgAseg.objects.filter(aseguradora_id=5,id_model_id=modelo):

		riesgorimac = RiesgAseg.objects.get(aseguradora_id=5,id_model_id=modelo).id_riesg__tipo_riesgo

	for t in tipo:

		tipo = t.id_tipo_id

	print 'riesgomapfre',riesgomapfre

	pro = programa.split('z')

	promapfre = pro[0]
	propositiva = pro[2]
	prorimac = pro[1]

	body = ''

	deducible = Deducibles.objects.all().values('id_deduc','deducible').order_by('id_deduc')
	anio = int(Anio.objects.get(id_anio=anio).anio_antig)

	lista = []

	cober = []

	for i in range(len(deducible)):

		deducible[0]['mapfre']= 'Taller Preferente: 15 % del Monto indemnizable, minimo US$ 15000 Afiliado concesionario: 20% del monto indemnizable minimo US$ 200 Taller no afiliado. 20% del monto indemnizable, minimo US$ 300'
		deducible[1]['mapfre']= 'Sin deducible'
		deducible[2]['mapfre']= 'Deducible dano propio'
		deducible[3]['mapfre']= 'Sin deducible'		
		deducible[4]['mapfre']= 'Deducible dano propio'
		deducible[5]['mapfre']= 'Deducible adicional del 10% del monto indemnizable'		
		deducible[6]['mapfre']= '15% del monto indem Min $150'
		deducible[7]['mapfre']= 'Deducible dano propio'
		deducible[8]['mapfre']= '20% del monto indem. Min $150'
		deducible[9]['mapfre']= 'Sin cobertura'
		deducible[10]['mapfre']= 'Sin cobertura'
		deducible[11]['mapfre']= 'Deducible adicional del 20% del monto indemnizable'
		deducible[12]['mapfre']= 'Deducible adicional del 20% del monto indemnizable'
		deducible[13]['mapfre']= '10% del monto indem Min $150'
		break

	for i in range(len(deducible)):

		deducible[0]['positiva']= 'Taller Multimarca: 10 % del Monto indemnizable, minimo US$ 15000 -Taller preferente: 12% del monto indemnizable minimo US$ 150 -Afiliado concecionario 15% del monto indemnizable, minimo US$ 250 - DIVEMOTOR  20% del monto indemnizable, minimo $500 - Taller no afiliado: 20% del monto indemnizable, minimo US$ 300'
		deducible[1]['positiva']= 'Sin deducible'
		deducible[2]['positiva']= 'Deducible dano propio'
		deducible[3]['positiva']= 'Con GPS: sin deducible Sin GPS sin cobertura'		
		deducible[4]['positiva']= '20% del monto indem Min $ 500'
		deducible[5]['positiva']= 'Deducible dano propio'		
		deducible[6]['positiva']= '10% del monto indem Min $150'
		deducible[7]['positiva']= '20% del monto indem Min $300'
		deducible[8]['positiva']= 'Hasta 25 anos doble deducible'
		deducible[9]['positiva']= '20% del monto indem Min $300'
		deducible[10]['positiva']= '20% del monto indemnizable'
		deducible[11]['positiva']= '20% del monto indem Min $300'
		deducible[12]['positiva']= '20% del monto indem Min $300'
		deducible[13]['positiva']= '10% del monto indem Min $150'
		break
		

	for i in range(len(deducible)):

		deducible[0]['rimac']= 'Taller Multimarca: 15 % del Monto indemnizable, minimo US$ 150 -Afiliado concesionario 20% del monto indemnizable, minimo US$ 200'
		deducible[1]['rimac']= '20% del monto indemnizable'
		deducible[2]['rimac']= '20% del monto indemnizable Min $200'
		deducible[3]['rimac']= 'Con GPS: sin deducible Sin GPS: sin cobertura'		
		deducible[4]['rimac']= '20% del monto indem Min $ 200'
		deducible[5]['rimac']= '10% del monto indemnizable minimo $150 (Talleres Multimarca)'		
		deducible[6]['rimac']= 'Deducible dano propio'
		deducible[7]['rimac']= '20% del monto indem Min $500'
		deducible[8]['rimac']= 'Varon 20% del monto indem Min $300 todo evento'
		deducible[9]['rimac']= '20% del monto indem Min $300'
		deducible[10]['rimac']= 'Deducible Dano Propio o deducible x Imprudencia el que sea mayor'
		deducible[11]['rimac']= '-Talleres afiliados multimarca 15% del monto indeminizable, minimo US$ 300- Afiliado concesionario: 20% del monto indeminizable, minimo US$ 500'
		deducible[12]['rimac']= 'Deducible Ausencia de control'
		deducible[13]['rimac']= '10% del monto indem Min $150'
		break
		


	for i in range(len(deducible)):


		if DeducAsegur.objects.filter(id_deduc=deducible[i]['id_deduc'],id_aseg_id=3,id_uso=uso).count()==1:

			deducible[i]['hdi'] = DeducAsegur.objects.get(id_deduc=deducible[i]['id_deduc'],id_aseg_id=3,id_uso=uso).value

		p= DeducAsegur.objects.filter(id_deduc=deducible[i]['id_deduc'],id_aseg_id=1,id_uso=uso,modalidad_id=modalidad,programa_id=propositiva,tipo_id=tipo).values('id_deduc__deducible')

		if p.count()==1:

			deducible[i]['positiva'] = DeducAsegur.objects.get(id_deduc=deducible[i]['id_deduc'],id_aseg_id=1,id_uso=uso,modalidad_id=modalidad,programa_id=propositiva,tipo_id=tipo).value


		if DeducAsegur.objects.filter(id_deduc=deducible[i]['id_deduc'],id_aseg_id=2).count()==1:

			deducible[i]['pacifico'] = DeducAsegur.objects.get(id_deduc=deducible[i]['id_deduc'],id_aseg_id=2).value


		p = DeducAsegur.objects.filter(id_deduc=deducible[i]['id_deduc'],id_aseg_id=4,programa_id=promapfre,id_uso_id=uso,riesgo_id=riesgomapfre,tipo_id=tipo).values('id_deduc__deducible')


		if p.count()==1:
		
			deducible[i]['mapfre'] = DeducAsegur.objects.get(id_deduc=deducible[i]['id_deduc'],id_aseg_id=4,programa_id=promapfre,id_uso_id=uso,riesgo_id=riesgomapfre,tipo_id=tipo).value
	


		if DeducAsegur.objects.filter(id_deduc=deducible[i]['id_deduc'],id_aseg_id=5,id_uso_id=uso).count()==1:
		
			deducible[i]['rimac'] = DeducAsegur.objects.get(id_deduc=deducible[i]['id_deduc'],id_aseg_id=5,id_uso_id=uso).value
		


	data_dict = ValuesQuerySetToDict(deducible)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def servic(request):

	body = ''

	servicio = Servicios.objects.all().values('id_serv','services').order_by('id_serv')

	print type(servicio)

	lista = []

	cober = []

	for i in range(len(servicio)):

		cober.append(i)

		if ServicAsegur.objects.filter(id_serv=servicio[i]['id_serv'],id_aseg_id=3).count()==1:

			lista.append(i)

			servicio[i]['hdi'] = ServicAsegur.objects.get(id_serv=servicio[i]['id_serv'],id_aseg_id=3).valor


		if ServicAsegur.objects.filter(id_serv=servicio[i]['id_serv'],id_aseg_id=1).count()==1:

			lista.append(i)

			servicio[i]['positiva'] = ServicAsegur.objects.get(id_serv=servicio[i]['id_serv'],id_aseg_id=1).valor


		if ServicAsegur.objects.filter(id_serv=servicio[i]['id_serv'],id_aseg_id=2).count()==1:

			lista.append(i)

			servicio[i]['pacifico'] = ServicAsegur.objects.get(id_serv=servicio[i]['id_serv'],id_aseg_id=2).valor


		if ServicAsegur.objects.filter(id_serv=servicio[i]['id_serv'],id_aseg_id=5).count()==1:

			lista.append(i)

			servicio[i]['rimac'] = ServicAsegur.objects.get(id_serv=servicio[i]['id_serv'],id_aseg_id=5).valor


		if ServicAsegur.objects.filter(id_serv=servicio[i]['id_serv'],id_aseg_id=4).count()==1:

			lista.append(i)

			servicio[i]['mapfre'] = ServicAsegur.objects.get(id_serv=servicio[i]['id_serv'],id_aseg_id=4).valor

	data_dict = ValuesQuerySetToDict(servicio)


	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")




@csrf_exempt
def servicio(request):

	d=ServicAsegur.objects.values('id','id_serv','id_serv__services','id_aseg__name_asegurad','valor')

	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def postin(request):

	if request.method == 'POST':

		print json.loads(request.body)

	return HttpResponse('xxxxx', content_type="application/json")


@csrf_exempt
def precio(request,id_model,anio):

	precioact =AutoValor.objects.get(id_modelo=id_model).valor


	return HttpResponse(precioact, content_type="application/json")


@csrf_exempt
def preciodreprecio(request,precio):

	precio = float(precio)

	precio = '{0:.2f}'.format(precio)


	return HttpResponse(precio, content_type="application/json")

@csrf_exempt
def listaservice(request):

	d=Servicios.objects.all().values('id_serv','services').order_by('id_serv')
	
	data_dict = ValuesQuerySetToDict(d)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def listfinanase(request):

	d=FinanAsegu.objects.all().values('id','id_finan','id_finan__financiamiento','id_aseg__name_asegurad','cuota','tea').order_by('-id')

	data_dict = ValuesQuerySetToDict(d)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def listafinance(request):

	d=FinanAsegu.objects.all().values('id_finan','id_aseg','cuota','tea').order_by('id_finan')

	data_dict = ValuesQuerySetToDict(d)	
	
	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def listafinanciamiento(request):

	d=Financiamiento.objects.all().values('id_financ','financiamiento').order_by('id_financ')
	
	data_dict = ValuesQuerySetToDict(d)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def uso(request):

	d=Uso.objects.all().values('id_uso','uso').order_by('id_uso')
	
	data_dict = ValuesQuerySetToDict(d)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def timon(request):

	d=Timon.objects.all().values('id_timon','name_tipo').order_by('id_timon')
	
	data_dict = ValuesQuerySetToDict(d)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def modalidad(request):

	d=Modalidad.objects.all().values('id_modalidad','name_modalidad').order_by('id_modalidad')
	
	data_dict = ValuesQuerySetToDict(d)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def date_handler(obj):

	return obj.isoformat() if hasattr(obj, 'isoformat') else obj

def ValuesQuerySetToDict(vqs):
	return [item for item in vqs]


@csrf_exempt
def add(request):

	if request.method == 'POST':

		data =  json.loads(request.body)
#		
		print 'hahahah',data

		#{u'categoria': {u'categoria': u'I', u'id_categ': 1}, u'igv': 18, u'clase': [{u'clase': u'Cami\xf3n', u'id_clase': 2}], u'anio': {u'id_anio': 16, u'anio_antig': 2004}, u'uso': {u'uso': u'Particular', u'id_uso': 1}, u'cobertura': [{u'descripcion': u'Riesgos de la Naturaleza', u'id_cobert': 20}], u'riesgo': {u'id_riesgo': 153, u'tipo_riesgo': u'Alta Gama I S/.1700'}, u'marca': {u'id_marca': 178, u'name_marca': u'LADA'}, u'value': u'111', u'demision': 3, u'aniox': 0, u'modelo': {u'id_model': 8062, u'name_model': u'C-61'}, u'programa': [{u'id_program': 3, u'program': u'Corporativo HDI'}], u'ubicacion': {u'id': 1, u'label': u'Lima'}, u'modalidad': [{u'id_modalidad': 2, u'name_modalidad': u'Todo Riesgo'}], u'aseguradora': {u'id_asegurad': 2, u'name_asegurad': u'Pacifico'}}


		cobertura = data['cobertura']
		aseguradora = data['aseguradora']
		programa = data['programa']
		modalidad = data['modalidad']
		uso = data['uso']
		clase = data['clase']
		#anio = data['anio']
		value = data['value']

		
		if type(cobertura) == dict:

			cobertura=[cobertura]

		if type(aseguradora) == dict:

			aseguradora=[aseguradora]

		if type(programa) == dict:

			programa=[programa]

		if type(modalidad) == dict:

			modalidad=[modalidad]

		if type(uso) == dict:

			uso=[uso]

		if type(clase) == dict:

			clase=[clase]

		# if type(anio) == dict:

		# 	anio=[anio]


		for c in cobertura:

			for a in aseguradora:

				for p in programa:

					for m in modalidad:

						for u in uso:

							for cl in clase:

								#for an in anio:
						
								CobertAsegur(tipo_id = int(cl['id_clase']),programa_id=int(p['id_program']),id_cob_id=int(c['id_cobert']),id_aseg_id=int(a['id_asegurad']),id_uso_id=int(u['id_uso']),value=value,modalidad_id=int(m['id_modalidad'])).save()



		data = json.dumps('data_dict')

		return HttpResponse(data, content_type="application/json")

@csrf_exempt
def addservice(request):

	if request.method == 'POST':

		data =  json.loads(request.body)

		aseguradora = data['aseguradora']['id_asegurad']
		value = data['valor']
		servicio = data['servicio']['id_serv']

		ServicAsegur(id_aseg_id=aseguradora,id_serv_id=servicio,valor=value).save()

		return HttpResponse(json.dumps(request.body), content_type="application/json")

@csrf_exempt
def addfinanz(request):

	if request.method == 'POST':

		data =  json.loads(request.body)

		print data

		aseguradora = data['aseguradora']['id_asegurad']
		cuota = data['cuota']
		tea = data['tea']
		financiamiento = data['financiamiento']['id_financ']
		FinanAsegu(id_aseg_id=aseguradora,id_finan_id=financiamiento,cuota=cuota,tea=tea).save()

		return HttpResponse(json.dumps(request.body), content_type="application/json")

@csrf_exempt
def addfinanciamiento(request):

	if request.method == 'POST':

		data =  json.loads(request.body)

		print 'Dfifnanana',data['financiamiento']

		Financiamiento(financiamiento=data['financiamiento']).save()


		return HttpResponse(json.dumps(request.body), content_type="application/json")

@csrf_exempt
def addtasa(request):

	if request.method == 'POST':

		data =  json.loads(request.body)

		# uso = data['uso']['id_uso']
		# aseguradora = data['aseguradora']['id_asegurad']
		# modalidad = data['modalidad']['id_modalidad']
		# anio = data['anio']['id_anio']
		# value = data['value']
		# categoria = data['categoria']['id_categ']
		# riesgo = data['riesgo']['id_riesgo']
		# programa = data['programa']['id_program']
		# ubicacion = data['ubicacion']['id']
		# clase_id = data['clase']['id_clase']

		uso = data['uso']
		aseguradora = data['aseguradora']
		modalidad = data['modalidad']
		anio = data['anio']
		value = data['value']
		riesgo = data['riesgo']
		programa = data['programa']
		ubicacion = data['ubicacion']
		clase = data['clase']

		if type(uso) == dict:

			uso=[uso]
	
		if type(aseguradora) == dict:

			aseguradora=[aseguradora]

		if type(modalidad) == dict:

			modalidad=[modalidad]

		if type(programa) == dict:

			programa=[programa]

		if type(anio) == dict:

			anio=[anio]


		if type(clase) == dict:

			clase=[clase]

		if type(riesgo) == dict:

			riesgo=[riesgo]

		if type(ubicacion) == dict:

			ubicacion=[ubicacion]


		for a in aseguradora:

			for p in programa:

				for m in modalidad:

					for u in uso:

						for r in riesgo:

							for an in anio:

								for cl in clase:

									for ub in ubicacion:

										TasaAsegur(ubicacion=ub['id'],riesgo_id=r['id_riesgo'],id_aseg_id=a['id_asegurad'],id_uso_id=u['id_uso'],tipo_id=cl['id_clase'],modalidad_id=m['id_modalidad'],value=value,anio_id=an['id_anio'],programa_id=p['id_program']).save()


		
			
		return HttpResponse(json.dumps(request.body), content_type="application/json")

@csrf_exempt
def addriesgoclase(request):

	if request.method == 'POST':

		data =  json.loads(request.body)

		#{u'riesgo': {u'id_riesgo': 153, u'tipo_riesgo': u'Alta Gama I S/.1700'}, u'aseguradora': {u'id_asegurad': 2, u'name_asegurad': u'Pacifico'}}

		#{u'modelos': [[{u'id_modelo__name_model': u'ACURA', u'model': u'ACURA', u'id_modelo': 6372, u'checkmodel': True}, {u'id_modelo__name_model': u'COMPACT', u'model': u'COMPACT', u'id_modelo': 5183, u'checkmodel': True}, {u'id_modelo__name_model': u'INTEGRA', u'model': u'INTEGRA', u'id_modelo': 8101, u'checkmodel': True}, {u'id_modelo__name_model': u'LEGEND', u'model': u'LEGEND', u'id_modelo': 5184, u'checkmodel': True}, {u'id_modelo__name_model': u'MDX', u'model': u'MDX', u'id_modelo': 5185, u'checkmodel': True}, {u'id_modelo__name_model': u'RSX', u'model': u'RSX', u'id_modelo': 5186, u'checkmodel': True}, {u'id_modelo__name_model': u'TL', u'model': u'TL', u'id_modelo': 5187, u'checkmodel': True}, {u'id_modelo__name_model': u'VIGOR', u'model': u'VIGOR', u'id_modelo': 5188, u'checkmodel': True}]], u'datax': {u'riesgo': {u'id_riesgo': 153, u'tipo_riesgo': u'Alta Gama I S/.1700'}, u'aseguradora': {u'id_asegurad': 3, u'name_asegurad': u'HDI'}}}

		riesgo = data['datax']['riesgo']['id_riesgo']

		aseguradora = data['datax']['aseguradora']['id_asegurad']


		for m in data['modelos'][0]:

			for i in m:

				if i=='checkmodel':

					if m['checkmodel'] == True:

						print m['id_modelo']

						#print 'modelo', AutoValor.objects.filter(id_modelo=m['id_modelo']).values('id','id_marca','id_modelo')

						id_modelo=AutoValor.objects.filter(id_modelo_id=m['id_modelo']).values('id','id_marca','id_modelo')[0]['id']

						print id_modelo

						RiesgAseg(id_riesg_id=int(riesgo),id_model_id=id_modelo,aseguradora_id=int(aseguradora)).save()




				
		data = json.dumps('data_dict')

		return HttpResponse(data, content_type="application/json")

@csrf_exempt
def addprima(request):

	if request.method == 'POST':

		data = json.loads(request.body)

		
		#{u'categoria': {u'categoria': u'I', u'id_categ': 1}, u'igv': 18, u'anio': {u'id_anio': 16, u'anio_antig': 2004}, u'uso': {u'uso': u'Particular', u'id_uso': 1}, u'riesgo': {u'id_riesgo': 153, u'tipo_riesgo': u'Alta Gama I S/.1700'}, u'marca': {u'id_marca': 178, u'name_marca': u'LADA'}, u'demision': 3, u'aniox': 0, u'modelo': {u'id_model': 8062, u'name_model': u'C-61'}, u'programa': {u'id_program': 2, u'program': u'Corporativo RIMAC'}, u'valor': u'145', u'ubicacion': {u'id': 1, u'label': u'Lima'}, u'modalidad': {u'id_modalidad': 3, u'name_modalidad': u'Responsabilidad Civil'}, u'aseguradora': {u'id_asegurad': 1, u'name_asegurad': u'Positiva'}}

		riesgo = data['riesgo']['id_riesgo']
		aseguradora = data['aseguradora']['id_asegurad']
		programa = data['programa']['id_program']
		primaminima = data['valor']

		print riesgo,aseguradora,programa,primaminima

		Primas(riesgo_id=riesgo,aseguradora_id=aseguradora,primaminima=primaminima,programa_id=programa).save()


	return HttpResponse('data', content_type="application/json")



@csrf_exempt
def adddeduccion(request):



	if request.method == 'POST':

		data =  json.loads(request.body)
#		
		print 'hahahah',data

		#{u'categoria': {u'categoria': u'I', u'id_categ': 1}, u'igv': 18, u'clase': [{u'clase': u'Cami\xf3n', u'id_clase': 2}], u'anio': {u'id_anio': 16, u'anio_antig': 2004}, u'uso': {u'uso': u'Particular', u'id_uso': 1}, u'cobertura': [{u'descripcion': u'Riesgos de la Naturaleza', u'id_cobert': 20}], u'riesgo': {u'id_riesgo': 153, u'tipo_riesgo': u'Alta Gama I S/.1700'}, u'marca': {u'id_marca': 178, u'name_marca': u'LADA'}, u'value': u'111', u'demision': 3, u'aniox': 0, u'modelo': {u'id_model': 8062, u'name_model': u'C-61'}, u'programa': [{u'id_program': 3, u'program': u'Corporativo HDI'}], u'ubicacion': {u'id': 1, u'label': u'Lima'}, u'modalidad': [{u'id_modalidad': 2, u'name_modalidad': u'Todo Riesgo'}], u'aseguradora': {u'id_asegurad': 2, u'name_asegurad': u'Pacifico'}}


		cobertura = data['deduccion']
		aseguradora = data['aseguradora']
		programa = data['programa']
		modalidad = data['modalidad']
		uso = data['uso']
		clase = data['clase']
		#anio = data['anio']
		value = data['value']
		riesgo =data['riesgo']

		
		if type(cobertura) == dict:

			cobertura=[cobertura]

		if type(aseguradora) == dict:

			aseguradora=[aseguradora]

		if type(programa) == dict:

			programa=[programa]

		if type(modalidad) == dict:

			modalidad=[modalidad]

		if type(uso) == dict:

			uso=[uso]

		if type(clase) == dict:

			clase=[clase]

		if type(clase) == dict:

			clase=[clase]

		if type(riesgo) == dict:

			riesgo=[riesgo]

		# if type(anio) == dict:

		# 	anio=[anio]


		for c in cobertura:

			for a in aseguradora:

				for p in programa:

					for m in modalidad:

						for u in uso:

							for r in riesgo:

								for cl in clase:

									DeducAsegur(riesgo_id=int(r['id_riesgo']),tipo_id = int(cl['id_clase']),programa_id=int(p['id_program']),id_deduc_id=int(c['id_deduc']),id_aseg_id=int(a['id_asegurad']),id_uso_id=int(u['id_uso']),value=value,modalidad_id=int(m['id_modalidad'])).save()



		data = json.dumps('data_dict')

		return HttpResponse(data, content_type="application/json")


@csrf_exempt
def addauto(request):

	data =  json.loads(request.body)

	model = json.loads(request.body)['model']

	clase = model['clase']

	if type(clase) == dict:

		clase=[clase]

	for i in data['item'][0]:

		for c in clase:

			AutoValor(id_tipo_id=c['id_clase'],id_modelo_id=i['id_modelo'],id_marca_id=i['id_marca']).save()	


	return HttpResponse(json.dumps(request.body), content_type="application/json")


@csrf_exempt
def addmarca(request):

	data =  json.loads(request.body)

	marca = data['data']
	
	Marca(name_marca=marca).save()

	return HttpResponse(marca, content_type="application/json")

@csrf_exempt
def addservicio(request):

	data =  json.loads(request.body)

	ser = data['data']
	
	Servicios(services=ser).save()

	return HttpResponse(marca, content_type="application/json")

@csrf_exempt
def addfinanzas(request):

	data =  json.loads(request.body)

	finan = data['data']

	Financiamiento(financiamiento=finan).save()

	return HttpResponse(marca, content_type="application/json")

@csrf_exempt
def editauto(request):

	data =  json.loads(request.body)
	tipo = data['clase']['id_clase']
	marca = data['name_marca']['id_marca']
	modelo = data['name_model']['id_model']
	auto = AutoValor.objects.get(id=data['id'])	
	auto.id_tipo_id=tipo
	auto.id_marca_id=marca
	auto.id_modelo_id=modelo
	auto.save()

	return HttpResponse('marca', content_type="application/json")


@csrf_exempt
def addmodelo(request):

	data =  json.loads(request.body)

	modelo = data['data']
	
	Modelo(name_model=modelo).save()

	return HttpResponse(json.dumps(request.body), content_type="application/json")

@csrf_exempt
def addriesgo(request):

	data =  json.loads(request.body)

	riesgo = data['data']
	
	Riesgo(tipo_riesgo=riesgo).save()

	return HttpResponse(json.dumps(request.body), content_type="application/json")

@csrf_exempt
def man_tasas(request):

	coberturas = TasaAsegur.objects.all().values('id_aseg','tipo','id','programa','riesgo','modalidad','id_uso','ubicacion','programa__program','riesgo__tipo_riesgo','id','id_aseg__name_asegurad','id_uso__uso','tipo__clase','modalidad__name_modalidad','value','anio','anio__anio_antig').order_by('-id')

	data_dict = ValuesQuerySetToDict(coberturas)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def man_autos(request):

	autos = AutoValor.objects.all().values('id','id_tipo__clase','id_modelo__name_model','id_marca__name_marca').order_by('-id')

	data_dict = ValuesQuerySetToDict(autos)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def man_cob(request):

	coberturas = CobertAsegur.objects.all().values('id','tipo__clase','antigued','id_cob','programa','programa__program','id_aseg','modalidad','id_cob__descripcion','id_aseg__name_asegurad','id_uso','id_uso__uso','modalidad__name_modalidad','value').order_by('-id')

	data_dict = ValuesQuerySetToDict(coberturas)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

	
def man_serv(request):

	servicios = ServicAsegur.objects.all().values('id','id_serv','id_aseg','id_serv__services','id_aseg__name_asegurad','valor').order_by('-id')

	data_dict = ValuesQuerySetToDict(servicios)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

def man_finan(request):

	financiamiento = FinanAsegu.objects.all().values('id','id_finan','id_finan__financiamiento','id_aseg','id_aseg__name_asegurad','cuota','tea').order_by('-id')

	data_dict = ValuesQuerySetToDict(financiamiento)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


# @csrf_exempt
# def financiamiento(request):

# 	financiamiento = FinanAsegu.objects.all().values('id','id_finan','id_finan__financiamiento','id_aseg','id_aseg__name_asegurad','cuota','tea').order_by('-id')

# 	data_dict = ValuesQuerySetToDict(financiamiento)

# 	data = json.dumps(data_dict)

# 	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def deduc_cob(request):

	deducib = DeducAsegur.objects.all().values('riesgo__tipo_riesgo','id_aseg','id_uso','tipo','modalidad','id','programa','id_deduc','programa__program','id','id_deduc__deducible','id_aseg__name_asegurad','id_uso__uso','tipo__clase','value','modalidad__name_modalidad','value').order_by('-id')

	data_dict = ValuesQuerySetToDict(deducib)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def eliminarries(request):

	print json.loads(request.body)

	data = json.loads(request.body)

	RiesgAseg.objects.get(id=data['id']).delete()

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def eliminarcob(request):

	print json.loads(request.body)

	data = json.loads(request.body)

	CobertAsegur.objects.get(id=data['id']).delete()

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def eliminardedu(request):

	data = json.loads(request.body)

	DeducAsegur.objects.get(id=data['id']).delete()

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def eliminarpolitica(request):

	data = json.loads(request.body)

	Gps.objects.get(id=data['id']).delete()

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def eliminarserv(request):

	data = json.loads(request.body)

	ServicAsegur.objects.get(id=data['id']).delete()
	
	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def eliminarprima(request):

	data = json.loads(request.body)

	Primas.objects.get(id=data['id']).delete()
	
	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def eliminarfinan(request):

	data = json.loads(request.body)
	FinanAsegu.objects.get(id=data['id']).delete()
	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def eliminartasa(request):

	data = json.loads(request.body)

	TasaAsegur.objects.get(id=data['id']).delete()
	
	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def eliminarauto(request):

	data = json.loads(request.body)

	AutoValor.objects.get(id=data['id']).delete()
	
	return HttpResponse(data, content_type="application/json")



@csrf_exempt
def addaseguradora(request):

	data = json.loads(request.body)['data']

	Aseguradora(name_asegurad=data).save()

	return HttpResponse('data', content_type="application/json")

@csrf_exempt
def addmodalidad(request):

	data = json.loads(request.body)['data']

	Modalidad(name_modalidad=data).save()

	return HttpResponse('data', content_type="application/json")

@csrf_exempt
def adduso(request):

	data = json.loads(request.body)['data']

	Uso(uso=data).save()

	return HttpResponse('data', content_type="application/json")

@csrf_exempt
def addclase(request):

	clase = json.loads(request.body)['data']


	Clase(clase=clase).save()

	return HttpResponse('data', content_type="application/json")

@csrf_exempt
def addprograma(request):

	program = json.loads(request.body)['data']

	Programa(program=program).save()

	return HttpResponse('data', content_type="application/json")




@csrf_exempt
def addcobertura(request):

	data = json.loads(request.body)['data']

	Cobertura(descripcion=data).save()

	return HttpResponse('data', content_type="application/json")

@csrf_exempt
def adddeducible(request):

	data = json.loads(request.body)['data']
	
	Deducibles(deducible=data).save()

	return HttpResponse('data', content_type="application/json")

@csrf_exempt
def addpoliticagps(request):

	if request.method == 'POST':

		data = json.loads(request.body)['gps']

		print 'ya pueeee.....',data['value']
		modelitos = json.loads(request.body)['modelitos']

		# uso = data['uso']
		aseguradora = data['aseguradora']
		programa = data['programa']
		# modalidad=data['modalidad']
		value = data['value']
		ubicacion = data['ubicacion']['id']
		anio=data['anio']


		if type(aseguradora) == dict:

			aseguradora=[aseguradora]

		# if type(modalidad) == dict:

		# 	modalidad=[modalidad]

		if type(modelitos) == dict:

			modelitos=[modelitos]

		if type(programa) == dict:

			programa=[programa]

		# if type(uso) == dict:

		# 	uso=[uso]

		if type(anio) == dict:

			anio=[anio]


		for a in aseguradora:

			for p in programa:

				# for u in uso:

				for an in anio:

					for m in modelitos[0]:

						for i in m:

							if i=='checkmodel':

								if m['checkmodel'] == True:


									print 'hahahah',an,anio

									
									# precio = AutoValor.objects.filter(id_modelo_id=m['id_modelo']).values('id','id_marca','id_modelo','valor')[0]

									# precio = AutoValor.objects.filter(id_modelo_id=m['id_modelo']).values('id','id_marca','id_modelo','valor')[0]['valor']
									
									# value = 'No'

									# if precio > 5000:

									# 	value = 'Si'

									# riesgo = RiesgAseg.objects.filter(id_model_id=id_modelo).values('id_riesg__tipo_riesgo')[0]('id_riesg__tipo_riesgo')

									# if 'Alt' in riesgo:

									# 	value = 'Si'

									
									Gps(id_uso_id=1,anio_antig_id=an['id_anio'],id_prog_id=p['id_program'],id_auto_id=m['id_modelo'],value='Si',id_aseg_id=a['id_asegurad']).save()

		return HttpResponse(data, content_type="application/json")



@csrf_exempt
def addpoliticagps2(request):

	if request.method == 'POST':

		data = json.loads(request.body)
		gps = data['gps']

		print 'gps..',gps
		aseguradora = gps['aseguradora']
		programa = gps['programa']
		sumaminima = gps['sumaminima']

		if type(aseguradora) == dict:

			aseguradora=[aseguradora]

		if type(programa) == dict:

			programa=[programa]

		for a in aseguradora:

			for p in programa:


				Gps(sumaminima=sumaminima,id_prog_id=p['id_program'],id_aseg_id=a['id_asegurad'],id_auto_id=1,id_riesg_id=1,anio_antig_id=1,id_uso_id=1,region=1,value=1).save()





		return HttpResponse('data', content_type="application/json")
	
@csrf_exempt
def cotiSave(request):

	if request.method == 'POST':

		print json.loads(request.body)

		dato = json.loads(request.body)['dato']
		precio = json.loads(request.body)['precio']
		name =''
		cel = ''
		email = ''
	
		for i in dato:

			if i == 'name':
				name=dato['name']

			if i == 'cel':
				cel=dato['cel']

			if i == 'email':
				email=dato['email']


		timon=dato['timon']['id_timon']
		anio=dato['anio']['id_anio']
		uso=dato['uso']['id_uso']
		marca=dato['marca']['id_marca']
		modelo=dato['claseModelo']['id_modelo']
		modalidad=dato['modalidad']['id_modalidad']
		tipo=dato['claseModelo']['id_tipo']

		statuscheck=dato['statuscheck']
		statusubicL=dato['statusubicL']
		statusubicP=dato['statusubicP']

		
	
		Clientes(fullname=name,email=email,celular=cel,chose_tipo_id=int(tipo),chose_marca_id=int(marca),chose_anio_id=int(anio),chose_modelo_id=int(modelo),chose_timon_id=int(timon),chose_modalid_id=int(modalidad),chose_uso_id=int(uso),value=float(precio),chose_ubicl=int(statusubicL),chose_ubicp=int(statusubicP),chose_informat=int(statuscheck)).save()

		id_cliente =  Clientes.objects.all().values('id_cliente').order_by('-id_cliente')[0]['id_cliente']


	return HttpResponse(json.dumps(id_cliente), content_type="application/json")


@csrf_exempt
def enviaemail(request):

	if request.method == 'POST':

		data = json.loads(request.body)

		#go.db.models.query.ValuesQuerySet'>
		#{u'orderId': u'425', u'anio': u'28', u'uso': u'1', u'precio': u'4444', u'modelo': u'6372', u'programa': u'3', u'modalidad': u'2'}

		orderId = data['orderId']

		cli = Clientes.objects.get(id_cliente=orderId)

		name = cli.fullname

		email = cli.email

		modelo = data['modelo']

		cli = data['orderId']

		precio = data['precio']

		a = AutoValor.objects.filter(id_modelo_id=modelo)

		#url = data['urld']

		for m in a:

			marca = m.id_marca.name_marca
			tipo = m.id_tipo.clase
			modelo = m.id_modelo.name_model

		print 'Mensaje..............'
		msj = 'Estimado cliente '+ str(name) +' , el siguiente link detalla la cotizacion del auto ' + str(marca) +' '+ str(modelo)+ ' valorizado en ' +str(precio)+'. Adjunto el link: '+ str('http://cotizador.hermes.pe:800/html/pdfout.pdf')

		
		id = Clientes.objects.get(id_cliente=cli).id_cliente

		flag  = Clientes.objects.get(id_cliente=id).chose_informat

		if flag == 1:

			print 'Enviando email....',email

			f = open('/var/www/html/email.txt', 'a')
			f.write(str(email)+'\n')
			f.close()

			send_mail('Hermes',msj,'cotiza@hermes.pe', [email], fail_silently=False)

		
	return HttpResponse(json.dumps('id_cliente'), content_type="application/json")


@csrf_exempt
def savecob(request):

	data = json.loads(request.body)

	print data

	clase = data['clase']['id_clase']

	uso = data['uso']['id_uso']
	##anio = data['antigued']
	aseguradora = data['aseguradora']['id_asegurad']
	modalidad = data['modalidad']['id_modalidad']
	programa = data['programa']['id_program']
	valor = data['value']

	c = CobertAsegur.objects.get(id=data['id'])
	
	c.tipo_id=clase

	c.id_aseg_id=aseguradora
	c.modalidad_id=modalidad
	c.programa_id=programa
	

	c.id_uso_id=uso
	##c.antigued=anio
	
	c.value = valor
	c.save()

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def saveprimas(request):

	data = json.loads(request.body)

	print data

	primaminima = data['primaminima']
	programa = data['programa']['id_program']
	aseguradora = data['aseguradora']['id_asegurad']
	riesgo= data['riesgo']['id_riesgo']

	prima = Primas.objects.get(id=data['id'])
	
	prima.aseguradora_id = aseguradora
	prima.riesgo_id = riesgo
	prima.programa_id=programa
	prima.primaminima = primaminima
	prima.save()


	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def savededu(request):

	data = json.loads(request.body)


	clase = data['clase']['id_clase']
	
	uso = data['uso']['id_uso']
	#anio = data['anio']['id_anio']
	aseguradora = data['aseguradora']['id_asegurad']
	modalidad = data['modalidad']['id_modalidad']
	programa = data['programa']['id_program']
	valor = data['value']
	riesgo = data['riesgo']['id_riesgo']

	c = DeducAsegur.objects.get(id=data['id'])
	c.tipo_id=clase
	c.id_aseg_id=aseguradora
	c.modalidad_id=modalidad
	c.programa_id=programa
	c.anio_id=anio
	c.id_uso_id=uso
	c.value = valor
	c.riesgo_id=riesgo
	c.save()


	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def saveservicio(request):

	print 'uyuyuyuyuyu'

	if request.method == 'POST':

		data = json.loads(request.body)

		print 'Saving servicio.....',data

		servicio = data['servicio']['id_serv']

		value = data['valor']

		aseguradora = data['aseguradora']['id_asegurad']
		
		c = ServicAsegur.objects.get(id=data['id'])
		c.id_aseg_id=aseguradora
		c.id_serv_id = servicio
		c.valor=value
		c.save()

		return HttpResponse(data, content_type="application/json")


@csrf_exempt
def savefinanc(request):

	data = json.loads(request.body)
	print data 

	#{u'id_aseg__name_asegurad': u'Positiva', u'id_finan__financiamiento': u'Cuotas Sin Interes', u'clase': {u'clase': u'Auto', u'id_clase': 1}, u'tea': 676, u'cuota': u'787', u'riesgo': {u'id_riesgo': 84, u'tipo_riesgo': u'Alta Gama hasta $40k'}, u'aseguradora': {u'id_asegurad': 1, u'name_asegurad': u'Positiva'}}

	cuota = data['cuota']
	tea = data['tea']
	fi = data['id_finan']
	id=data['id']

	print fi
	aseguradora = data['aseguradora']['id_asegurad']

	c = FinanAsegu.objects.get(id=id)
	c.id_finan_id=fi
	c.id_aseg_id=aseguradora
	c.cuota=cuota
	c.tea=tea
	c.save()


	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def savetasa(request):

	data = json.loads(request.body)


	clase = data['clase']['id_clase']
	uso = data['uso']['id_uso']
	anio = data['anio']['id_anio']
	aseguradora = data['aseguradora']['id_asegurad']
	modalidad = data['modalidad']['id_modalidad']
	programa = data['programa']['id_program']
	riesgo=data['riesgo']['id_riesgo']
	valor = data['value']


	c = TasaAsegur.objects.get(id=data['id'])

	c.tipo_id=clase
	c.id_aseg_id=aseguradora
	c.modalidad_id=modalidad
	c.id_uso_id=uso
	c.programa_id=programa
	c.anio_id=anio
	c.riesgo_id=riesgo
	c.value=valor

	c.save()


	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def savepoliticas(request):

	data = json.loads(request.body)

	print data


	anio = data['anio']['id_anio']
	aseguradora = data['aseguradora']['id_asegurad']
	programa = data['programa']['id_program']
	valor = data['value']


	c = Gps.objects.get(id=data['id'])

	c.id_aseg_id=aseguradora
	c.programa_id=programa
	c.anio_antig_id=anio
	c.value=valor

	c.save()


	return HttpResponse(data, content_type="application/json")
