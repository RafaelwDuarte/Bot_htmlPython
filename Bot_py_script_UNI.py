import http.client, urllib.parse, requests, json, rstr, random, datetime, copy
from html.parser import HTMLParser

#Inicialização de variaveis 
Action = str()
dados_form_con = list()
dados_form = list()
sumary = list()
dados = list()
act = list()
nomes = list()
sobrenomes = list()
genero = list()
nascimento = list()
email = list()
fone = list()
so = list()
Progreso = int(1)

#Requisição HTTP
site = input("Site: ")
#r = requests.get('http://www.agexcom.com.br/hackform')
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
sumary = copy.copy(dados_form_con)

#Postagem do formulario 
def payload(site, act, cont, numero_vezes):
    payload={dados_form_con[0]:dados_form[0],dados_form_con[1]:dados_form[1],dados_form_con[2]:dados_form[2],dados_form_con[3]:dados_form[3],dados_form_con[4]:dados_form[4],dados_form_con[5]:dados_form[5],dados_form_con[6]:dados_form[6]}
    site = site + "/" + act[0] 
    enviar = requests.post(site, payload)
    envioresp = enviar.status_code
    Progreso = cont
    if (envioresp == 200):
        print ("Requisição" , Progreso , "/" , numero_vezes, " - Sucesso")
    else:
        print ("Requisição" , Progreso , "/" , numero_vezes, " - Erro") 
    #print("Envio", enviar.reason)

#Juntando as listas 
def together_list():
    cont1 = 0
    while cont1 < len(dados_form):
        dados.append(dados_form_con[cont1]+":")
        dados.append(dados_form[cont1]+",")
        cont1 = cont1 + 1
#Log 
def log(cont, dados_form):
    arquivo = open('log.log','a')
    arquivo.write("\n" + "\n" + "-------Forumlario  " + str(cont) + "\n" + "\n")    
    for i in dados_form:
        arquivo.writelines(i)
        arquivo.write(',')
    arquivo.write("\n")
    arquivo.close()
    arquivo = open('log.log','a')

def Popula(numero_vezes, Progreso):
    cont = 0  
    while cont < numero_vezes:
        conti = 0
        for dados_form_con in sumary:
            print ("Campo: ", dados_form_con)
            mode = str(input("Escolha a letra do modo de inserção de dados" + "\n" "[R]random - Campos fixos" + "\n" + "[E]arquivo externo" + "\n" + "[C]Passar dados Manualmente \n"))
            if (mode == "R" or mode == "r"):
                mode2 = str(input("(N)nome \n (SN)Sobrenome \n (G)Genero \n (DN)DataDeNascimento \n (E)Email \n (T)Telefone \n (SO)SistemaOperacional \n"))
                if (mode2 == "N"):
                    dados_form[conti] = '{0}{1}{2}{3}{4}{5}{6}'.format(rstr.uppercase(1), rstr.rstr('aeiou', 1), rstr.lowercase(1), rstr.rstr('aeiou', 1), rstr.lowercase(1), rstr.rstr('aeiou', 1), rstr.lowercase(1))
                elif (mode2 == "SN"):
                    dados_form[conti] = '{0}{1}'.format(rstr.uppercase(1), rstr.lowercase(5,16))
                elif (mode2 == "G"):
                    gender = ['male','female']
                    dados_form[conti] = random.choice(gender)
                elif (mode2 == "DN"):
                    ano_inic = ["198","197","196","195","194","193","192","199","200","201"]
                    ano_random = random.choice(ano_inic) + rstr.digits(1)
                    data_rand_nasc = '{0}{1}/{2}{3}/'.format(rstr.rstr('012', 1), rstr.digits(1), rstr.rstr('01', 1), rstr.rstr('012', 1))
                    data_rand_nasc = data_rand_nasc + ano_random
                    dados_form[conti] = data_rand_nasc
                elif (mode2 == "E"):
                    dados_form[conti] = '{0}@{1}.com.{2}'.format(rstr.lowercase(exclude='@#<"^;:´`?+=[]~*{}'), rstr.lowercase(5,15), rstr.lowercase(2))
                elif (mode2 == "T"):
                    dados_form[conti] = '{0}{1}'.format(rstr.rstr('3,8,9', 1), rstr.digits(7))
                elif (mode2 == "SO"):
                    sist = ['Debian', 'Ubuntu', 'Windows', 'Mac OS']
                    dados_form[conti] = random.choice(sist)
                else:
                    print ("Opção invalida")
            elif (mode == "E" or mode == "e"):
                    arqex = input("Insira caminho arquivo: \n")
                    try:
                        with open(arqex) as ArquivoExt:
                            dados_form[conti] = ArquivoExt.readline().rstrip('\n')
                    except:
                        print("Arquivo ou caminho com erro ou fora do padrão")
            elif (mode == "C" or mode == "c"):
                dados_form[conti] = input("")
            together_list()
            conti = conti + 1
        cont = cont + 1
        payload(site, act, cont, numero_vezes)
        log(cont , dados_form)

    

def menu():

    #Conta Requisições
    numero_vezes = int(input("Numero de Requisições: "))

    #Seta data 
    today  = datetime.datetime.today()
    today = today.strftime("%Y-%m-%d %H:%M")

    #Loga Inicio
    arquivo = open('log.log','a')
    arquivo.write("\n" + "\n" + "---> Inicio do Script  " + today + " -  Numero de repetições:  " + str(numero_vezes))
    arquivo.close()

    Popula(numero_vezes, Progreso)

menu()
wait = input("---------")

