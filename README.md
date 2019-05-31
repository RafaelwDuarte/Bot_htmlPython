# Bot_Python_Html

Bot para Preenchimento de Formulários HTML em Python

Objetivo:
Criar um bot para fazer preenchimento de formulários em páginas web.

Funcionalidades:
- O script deve solicitar ao usuário o endereço da página que contém o formulário
- Exemplo: http://www.agexcom.com.br/hackform/index.php
- O bot deve acessar o site, identificar os campos do formulário e o action
- Em seguida, deve solicitar que o usuário informe a origem dos dados para cada campo
- A origem pode ser uma lista carregada a partir de um arquivo, uma constante ou uma expressão regular
- O usuário deve informar a quantidade de envios que ele quer fazer
- O bot deve montar um payload dos campos com dados aleatórios a partir das origens e enviar para a página definida no action do formulário
- Para cada envio, deve ser montado um payload diferente
- Mostrar na tela um indicador de progressão da tarefa
- A cada envio, gravar o payload em um arquivo de log

Módulos padrão ou de terceiros:
- HTML Client: para acessar a página web e enviar os dados do formulário
- HTML Parser: para identificar os campos do formulário
- Geração de strings: Geração de conteúdo aleatório obedecendo o formato de uma expressão regular

Referências:
- https://docs.python.org/3/library/http.client.html
- https://pypi.org/project/requests/
- https://docs.python.org/3/library/html.parser.html
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- https://pypi.org/project/rstr/
