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

	mot = random.choice(liste1)
	mot2 = random.choice(liste2)
	mot3 = random.choice(liste3)

	data = {'phrase':mot + ' ' + mot2 + ', je conseille ' + mot3 + '.'}

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