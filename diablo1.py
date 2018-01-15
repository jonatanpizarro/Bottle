from bottle import run, get, post, request, view, route, template
from random import randint

@get('/hello/diablo1')
def hello():
	adivina = randint(1,100)
	num=" "
    return template('template' , num=num , adivina=adivina)

@post('/hello/diablo1')
def hello1():
	num=request.forms.get('fname')
	adivina=request.forms.get('adivina')


	if adivina==num:
		return template('template',num="Has ganado", adivina=adivina)
	elif adivina>num:
		return template('template' ,num="El numero es mayor", adivina=adivina)
	elif adivina<num:
		return template('template' ,num="El numero es menor", adivina=adivina)


run(host='localhost', port=8080)