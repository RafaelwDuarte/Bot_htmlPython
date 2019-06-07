import http.client, urllib.parse, requests, json, rstr, random, datetime, copy
from html.parser import HTMLParser

#Inicialização de variaveis 
Action = str()
dados_form_con = list()
dados_form = list()
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
    


#Popula lista com valores randomicos

def random_data(mode, numero_vezes, Progreso):
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
        payload(site, act, cont, numero_vezes)
        log(cont, mode, dados_form)
        

#Popula com dados de arquivo externo
def extrenal_data(mode, numero_vezes, dnomes, dsobre, dgenero,dnascimento,demail,dfone,dso, Progreso):
    cont = 0 
    arquivos_2 = open(dnomes,'r')
    nomes = arquivos_2.readlines()
    arquivos_2.close()
    arquivos_2 = open(dsobre,'r')
    sobrenomes = arquivos_2.readlines()
    arquivos_2.close()
    arquivos_2 = open(dgenero,'r')
    genero = arquivos_2.readlines()
    arquivos_2.close()
    arquivos_2 = open(dnascimento,'r')
    nascimento = arquivos_2.readlines()
    arquivos_2.close()
    arquivos_2 = open(demail,'r')
    email = arquivos_2.readlines()
    arquivos_2.close()
    arquivos_2 = open(dfone,'r')
    fone = arquivos_2.readlines()
    arquivos_2.close()
    arquivos_2 = open(dso,'r')
    so = arquivos_2.readlines()
    arquivos_2.close()
    while cont < numero_vezes:
        dados_form[0]=nomes[cont].rstrip('\n')
        dados_form[1]=sobrenomes[cont].rstrip('\n')
        dados_form[2]=genero[cont].rstrip('\n')
        dados_form[3]=nascimento[cont].rstrip('\n')
        dados_form[4]=email[cont].rstrip('\n')
        dados_form[5]=fone[cont].rstrip('\n')
        dados_form[6]=so[cont].rstrip('\n')
        cont = cont + 1
        payload(site, act, cont, numero_vezes)
        log(cont, mode, dados_form)
#Popula com constantes 
def constantes(mode, numero_vezes, Progreso):
    cont = 0
    dados_form[0]=input("Nome: ")
    dados_form[1]=input("Sobrenome: ")
    genero=input("Genero: [M]Masculino / [F]Feminino \n")
    if (genero=="M"):
        dados_form[2]="Masculino"
    elif (genero=="F"):
        dados_form[2]="Feminino"
    else:
        print("Opção Invalida")
        exit
    dados_form[3]=input("Data de Nascimento(Padrão dd/mm/aaaa): \n")
    dados_form[4]=input("Email: \n")
    dados_form[5]=input("Telefone: \n")
    genero=input("Sistema Operacional \n -[D]Debian, [U]Ubuntu, [W]Windows, [M]Mac OS \n")
    if (genero=="D"):
        dados_form[6]="Debian"
    elif (genero=="U"):
        dados_form[6]="Ubuntu"
    elif (genero=="W"):
        dados_form[6]="Windows"
    elif (genero=="M"):
        dados_form[6]="Mac OS"
    else:
        print("Opção Invalida")
        exit
    while cont < numero_vezes:
        cont = cont + 1
        payload(site, act, cont, numero_vezes)
        log(cont, mode, dados_form)

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

    mode = str(input("Escolha a letra do modo de inserção de dados" + "\n" "[R]random" + "\n" + "[E]arquivo externo" + "\n" + "[C]Passar dados Manualmente \n"))
    if (mode == "R"):
        random_data(mode, numero_vezes, Progreso )

    elif (mode == "E"):
        dnomes = input("caminho do arquivo de nomes: \n")
        dsobre = input("caminho do arquivo de sobrenomes: \n")
        dgenero = input("caminho do arquivo de generos: \n")
        dnascimento = input("caminho do arquivo de datas de nascimento: \n")
        demail = input("caminho do arquivo de emails: \n")
        dfone = input("caminho do arquivo de telefones \n")
        dso = input("caminho do arquivo de sistema operacional \n")
        extrenal_data(mode, numero_vezes, dnomes, dsobre, dgenero,dnascimento,demail,dfone,dso, Progreso)

    elif (mode == "C"):
        constantes(mode, numero_vezes, Progreso)

    else:
        print ("Opção Invalida")
        arquivo = open('log.log','a')
        arquivo.write(" - Opção invavida")
        arquivo.close()
        exit
#Log 
def log(cont, mode, dados_form):
    arquivo = open('log.log','a')
    arquivo.write("\n" + "\n" + "-------Forumlario  " + str(cont) + "\n" + "\n" + "mode: " + mode + "\n")    
    for i in dados_form:
        arquivo.writelines(i)
        arquivo.write(',')
    arquivo.write("\n")
    arquivo.close()
    arquivo = open('log.log','a')

#Juntando as listas 
def together_list():
    cont1 = 0
    while cont1 < len(dados_form):
        dados.append(dados_form_con[cont1]+":")
        dados.append(dados_form[cont1]+",")
        cont1 = cont1 + 1

mode()



wait = input("  ")
