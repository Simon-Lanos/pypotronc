from django.shortcuts import render_to_response
import random

def create(request):

	number1 = random.randint(0,9)
	number2 = random.randint(0,9)
	number3 = random.randint(0,9)

	liste1 = ['Vu', 'En ce qui concerne', 'Quelle que soit', 'Quoi qu\'on dise concernant',
	'Avec', 'Si vous voulez mon avis concernant', 'Afin de circonvenir à', 'Dans le but de pallier à',
	'Pour réagir face à', 'Malgré',]

	liste2 = ['la politique','l\'ambiance','la situation','l\'inconstance','cette inflexion',
	'cette inflexion','la restriction','l\'orientation','la dégradation','cette difficulté',
	'la baisse de confiance',]

	liste3 = ['une remise a zéro', 'd\'appeler dédé le fils d\'un ventriloque', 'd\'enterrer les preuves',
	'de vendre nos parts chez LIDL', 'de créer une école du numérique', 'de faire des crêpes bretonnes',
	'd\'embaucher des stagières bac+5', 'de ne pas oublier sa girafe dans son sellier', 
	'de rendre nos politiciens responsable', 'de ranger vos bébés dans une poubelle']

	print(number1)
	print(number2)
	print(number3)

	mot = liste1[number1]
	mot2 = liste2[number2]
	mot3 = liste3[number3]

	data = {'phrase':mot + ' ' + mot2 + ', je conseille ' + mot3 + '.'}

	return render_to_response('default.html', data)

def code(request):

	liste1 = ['++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.',
	'$toto = yolo; echo $toto;', """let toto = ['coucou', 'rule 34', 'yolo', 1337, 'tintin', 'Krankenhaus', 2048];
	for let rows in toto {
		console.log(toto[rows])
		}
	"""]

	number1 = random.randint(0,2)

	data = {'phrase':liste1[number1], 'languages':['php', 'javascript', 'brainF*ck']}

	return render_to_response('default.html', data)