from django.shortcuts import render_to_response
import random

def create(request):

	liste1 = ['Vu', 'En ce qui concerne', 'Quelle que soit', 'Quoi qu\'on dise concernant',
	'Avec', 'Si vous voulez mon avis concernant', 'Afin de circonvenir à', 'Dans le but de pallier à',
	'Pour réagir face à', 'Malgré',]

	liste2 = ['la politique','l\'ambiance','la situation','l\'inconstance','cette inflexion',
	'cette inflexion','la restriction','l\'orientation sexuelle de votre enfant','la dégradation','cette difficulté',
	'la baise de confiance',' un mauvais coup ',]

	liste3 = ['une remise a zéro', 'd\'appeler dédé le fils d\'un ventriloque', 'd\'enterrer les preuves',
	'de vendre nos parts de la NWS', 'de créer une école du numérique', 'de faire des crêpes bretonnes',
	'd\'embaucher des stagières bac+5', 'de ne pas oublier sa girafe dans son sellier', 
	'de rendre nos politiciens responsable', 'de ranger vos bébés dans une poubelle',' un fist ',' de fermer vos gueules ']

	liste4 = ['qu\'un pain dans la gueule', 'qu\'une biture au vin blanc', 'qu\'une éradication de masse',
			  'qu\'une reconfiguration', 'qu\'un plan social', 'qu\'une élévation spirituelle',
			  'qu\'un renouvellement de mandat', 'que l\'admnistration d\'une carotte par voie anale',
			  'qu\'un masque au Nutella', 'qu\'une tortue au pouvoir', 'qu\'un reboot',
			  'qu\'une balle entre les yeux']

	liste5 = ['rapidement', 'en urgence', 'doucement',
			  'en douceur', 'violemment', 'par un professionnel',
			  'au CESi', 'dans la minute',
			  'dans la seconde', 'avec prudence', 'déguisé en prostituée bulgare',
			  'avec classe']

	if request.GET != {}:
		uid = request.GET['id']
		uid = uid.split('-')
		print(uid)
		try:
			mot = liste1[int(uid[0])]
		except IndexError as e:
			return render_to_response('404.html')

		try:
			mot2 = liste2[int(uid[1])]
		except IndexError as e:
			return render_to_response('404.html')

		try:
			mot3 = liste3[int(uid[2])]
		except IndexError as e:
			return render_to_response('404.html')
		try:
			mot4 = liste4[int(uid[3])]
		except IndexError as e:
			return render_to_response('404.html')
		try:
			mot5 = liste5[int(uid[4])]
		except IndexError as e:
			return render_to_response('404.html')

	else :
		mot = random.choice(liste1)
		mot2 = random.choice(liste2)
		mot3 = random.choice(liste3)
		mot4 = random.choice(liste4)
		mot5 = random.choice(liste5)

	idGet = '?id=' + str(liste1.index(mot)) + '-' + str(liste2.index(mot2)) + '-' + str(liste3.index(mot3)) + '-' +  str(liste4.index(mot4)) + '-' + str(liste5.index(mot5))

	data = {'phrase':mot + ' ' + mot2 + ', je conseille ' + mot3 + ', ainsi ' + mot4 + ' ' + mot5 + '.', 'GET':idGet}

	return render_to_response('default.html', data)

def code(request):

	liste1 = ['++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.',
	'$toto = yolo; echo $toto;', """let toto = ['coucou', 'rule 34', 'yolo', 1337, 'tintin', 'Krankenhaus', 2048];
	for let rows in toto {
		console.log(toto[rows])
		}
	"""]

	data = {'phrase':random.choice(liste1), 'languages':['php', 'javascript', 'brainF*ck']}

	return render_to_response('default.html', data)