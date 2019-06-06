import http.client, urllib.parse, requests, json, rstr, random, datetime, copy
from html.parser import HTMLParser

#Inicialização de variaveis 
Action = str()
dados_form_con = list()
dados_form = list()
dados = list()
act = list()

#Requisição HTTP
site = input("Site: ")
#r = requests.get('http://www.agexcom.com.br/hackform/index.php')
r = requests.get(site)
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
        if "form" in tag:
            Action=dict(attrs)['action']
            act.append(Action)

#Parser no HTML
parser = MyHTMLParser()
parser.feed(r.text)

#Remove Dados
dados_form_con.remove("submit")
dados_form_con.remove("gender")
dados_form = copy.copy(dados_form_con)

#Copia de Lista
def copy_list():
    dados_form = copy.copy(dados_form_con)

#Postagem do formulario 
def payload(site, act):
    payload={dados_form_con[0]:dados_form[0],dados_form_con[1]:dados_form[1],dados_form_con[2]:dados_form[2],dados_form_con[3]:dados_form[3],dados_form_con[4]:dados_form[4],dados_form_con[5]:dados_form[5],dados_form_con[6]:dados_form[6]}
    site = site + "/" + act[0] 
    enviar = requests.post(site, payload)
    print("Envio Inciando")
    print( "Status Code:", enviar.status_code)
    print("Envio", enviar.reason)


#Popula lista com valores randomicos

def random_data(mode, numero_vezes):
    cont = 0 
    while cont < numero_vezes:
        dados_form[0] = '{0}{1}{2}{3}{4}{5}{6}'.format(rstr.uppercase(1), rstr.rstr('aeiou', 1), rstr.lowercase(1), rstr.rstr('aeiou', 1), rstr.lowercase(1), rstr.rstr('aeiou', 1), rstr.lowercase(1))
        dados_form[1] = '{0}{1}'.format(rstr.uppercase(1), rstr.lowercase(5,16))
        gender = ['Masculino','Feminino']
        dados_form[2] = random.choice(gender)
        ano_inic = ["198","197","196","195","194","193","192","199","200","201"]
        ano_random = random.choice(ano_inic) + rstr.digits(1)
        data_rand_nasc = '{0}{1}/{2}{3}/'.format(rstr.rstr('012', 1), rstr.digits(1), rstr.rstr('01', 1), rstr.rstr('012', 1))
        data_rand_nasc = data_rand_nasc + ano_random
        dados_form[3] = data_rand_nasc
        dados_form[4] = '{0}@{1}.com.{2}'.format(rstr.lowercase(exclude='@#<"^;:´`?+=[]~*{}'), rstr.lowercase(5,15), rstr.lowercase(2))
        dados_form[5] = '{0}{1}'.format(rstr.rstr('3,8,9', 1), rstr.digits(7))
        sist = ['Debian', 'Ubuntu', 'Windows', 'Mac OS']
        dados_form[6] = random.choice(sist)
        together_list()
        cont = cont + 1
        payload(site, act)
        log(cont, mode)
        

#Popula com dados de arquivo externo
def extrenal_data(mode, numero_vezes, dm):
    cont = 0 
    arquivos_2 = open(dm,'r')
    while cont < numero_vezes:
        texto = arquivos_2.readlines()
        dados_form_con=texto
        cont = cont + 1
        together_list()  
        payload(site, act)
        log(cont, mode)

    arquivos_2.close()
    

#Menu
def mode():

    copy_list()

    #Conta Requisições
    numero_vezes = int(input("Numero de Requisições: "))

    #Seta data 
    today  = datetime.datetime.today()
    today = today.strftime("%Y-%m-%d %H:%M")

    #Loga Inicio
    arquivo = open('log.log','a')
    arquivo.write("\n" + "\n" + "---> Inicio do Script  " + today + " -  Numero de repetições:  " + str(numero_vezes))
    arquivo.close()

    mode = str(input("Escolha a letra do modo de inserção de dados" + "\n" "[r] random" + "\n" + "[e] arquivo externo" + "\n"))
    if (mode == "r"):
        random_data(mode, numero_vezes)

    elif (mode == "e"):
        dm = input("caminho do arquivo: ")
        extrenal_data(mode, numero_vezes, dm)

    else:
        print ("Opção Invalida")
        arquivo = open('log.log','a')
        arquivo.write(" - Opção invavida")
        arquivo.close()
        exit
#Log 
def log(cont, mode):
    arquivo = open('log.log','a')
    arquivo.write("\n" + "\n" + "-------Forumlario  " + str(cont) + "\n" + "\n" + "mode: " + mode + "\n")    
    for i in dados_form_con:
        arquivo.writelines(i)
        arquivo.write(',')
    arquivo.write("\n")
    arquivo.close()
    arquivo = open('log.log','a')
    for i in dados_form:
        arquivo.write(i)
        arquivo.write(',')
        cont = cont + 1
    arquivo.write("\n")
    arquivo.close()

#Juntando as listas 
def together_list():
    cont1 = 0
    while cont1 < len(dados_form):
        dados.append(dados_form_con[cont1]+":")
        dados.append(dados_form[cont1]+",")
        cont1 = cont1 + 1

mode()

wait = input("---------")
