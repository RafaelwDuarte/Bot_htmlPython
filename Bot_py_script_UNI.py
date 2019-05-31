import http.client, urllib.parse, requests
from html.parser import HTMLParser
import rstr
import random

Action = str()
dados_form = list()

#Requisição HTTP
r = requests.get('http://www.agexcom.com.br/hackform/index.php')
#Codigo de resposta
print(r.status_code)

#Pesquisar no parser e monta um dicionario com os parametros
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if "input" in tag:
            Action=dict(attrs)["name"]
            dados_form.append(Action)
        if "select" in tag:
            Action=dict(attrs)["name"]
            dados_form.append(Action)


parser = MyHTMLParser()
parser.feed(r.text)

#print(dados_form)
print(dados_form)
#for i in dados_form:
dados_form.remove("submit")
dados_form.remove("gender")

dados_form[0] = '{0}{1}{2}{3}{4}{5}{6}'.format(rstr.uppercase(1), rstr.rstr('aeiou', 1), rstr.lowercase(1), rstr.rstr('aeiou', 1), rstr.lowercase(1), rstr.rstr('aeiou', 1), rstr.lowercase(1))
dados_form[1] = '{0}{1}'.format(rstr.uppercase(1), rstr.lowercase())
gender = ['Masculino','Feminino']
dados_form[2] = random.choice(gender)
dados_form[3] = '{0}{1}/{2}{3}/{4}{5}{6}'.format(rstr.rstr('012', 1), rstr.digits(1), rstr.rstr('01', 1), rstr.rstr('012', 1), rstr.rstr('12', 1), rstr.rstr('09', 2), rstr.digits(1))
dados_form[4] = '{0}@{1}.com.{2}'.format(rstr.uppercase(exclude='@#<"^;:´`?+=[]~*{}'), rstr.lowercase(5,15), rstr.lowercase(2))
dados_form[5] = '{0}{1}'.format(rstr.rstr('3,8,9', 1), rstr.digits(7))
sist = ['Debian', 'Ubuntu', 'Windows', 'Mac OS']
dados_form[6] = random.choice(sist)

print(dados_form)