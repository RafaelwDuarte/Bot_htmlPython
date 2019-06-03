import http.client, urllib.parse, requests
from html.parser import HTMLParser
import rstr
import random
import copy
import datetime

#Inicialização de variaveis 
Action = str()
dados_form_con = list()
dados_form = list()

#Conta Requisições
numero_vezes = int(input("Numero de Requisições: "))
cont = 0 
#Seta data 
today  = datetime.datetime.today()
today = today.strftime("%Y-%m-%d %H:%M")

#Loga Inicio
arquivo = open('log.log','a')
arquivo.write("\n" + "\n" + "---> Inicio do Script  " + today + " -  Numero de repetições:  " + str(numero_vezes))
arquivo.close()

#Requisição HTTP
r = requests.get('http://www.agexcom.com.br/hackform/index.php')
http_code = r.status_code

#Pesquisar no parser e monta uma lista com os parametros
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if "input" in tag:
            Action=dict(attrs)["name"]
            dados_form_con.append(Action)
        if "select" in tag:
            Action=dict(attrs)["name"]
            dados_form_con.append(Action)
#Parser no HTML
parser = MyHTMLParser()
parser.feed(r.text)

#Remove Dados
dados_form_con.remove("submit")
dados_form_con.remove("gender")

while cont < numero_vezes: 

    #Copia de Lista
    dados_form = copy.copy(dados_form_con)

    #Popula lista
    dados_form[0] = '{0}{1}{2}{3}{4}{5}{6}'.format(rstr.uppercase(1), rstr.rstr('aeiou', 1), rstr.lowercase(1), rstr.rstr('aeiou', 1), rstr.lowercase(1), rstr.rstr('aeiou', 1), rstr.lowercase(1))
    dados_form[1] = '{0}{1}'.format(rstr.uppercase(1), rstr.lowercase(5,16))
    gender = ['Masculino','Feminino']
    dados_form[2] = random.choice(gender)
    dados_form[3] = '{0}{1}/{2}{3}/{4}{5}{6}'.format(rstr.rstr('012', 1), rstr.digits(1), rstr.rstr('01', 1), rstr.rstr('012', 1), rstr.rstr('12', 1), rstr.rstr('09', 2), rstr.digits(1))
    dados_form[4] = '{0}@{1}.com.{2}'.format(rstr.uppercase(exclude='@#<"^;:´`?+=[]~*{}'), rstr.lowercase(5,15), rstr.lowercase(2))
    dados_form[5] = '{0}{1}'.format(rstr.rstr('3,8,9', 1), rstr.digits(7))
    sist = ['Debian', 'Ubuntu', 'Windows', 'Mac OS']
    dados_form[6] = random.choice(sist)

    #Log
    arquivo = open('log.log','a')
    arquivo.write("\n" + "\n" + "-------Forumlario  " + str(cont+1) + "\n" + " Http code: " + str(http_code) + "\n" + " Campos:")
    for i in dados_form_con:
        arquivo.writelines(i)
        arquivo.write(',')
    arquivo.close()
    arquivo = open('log.log','a')
    arquivo.write("\n " + "Dados: ")
    for i in dados_form:
        arquivo.write(i)
        arquivo.write(',')
    arquivo.close()
    cont = cont + 1
print ("Concluído com Sucesso")


