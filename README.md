# Raspa Doc - PM

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

### Tópicos 

:small_blue_diamond: [Descrição do projeto](#descrição-do-projeto)

:small_blue_diamond: [Tecnologias utilizadas](#Tecnologias-utilizadas)

:small_blue_diamond: [Funcionalidades](#funcionalidades)

:small_blue_diamond: [Pré-requisitos](#pré-requisitos)

:small_blue_diamond: [Como rodar a aplicação](#como-rodar-a-aplicação-arrow_forward)

:small_blue_diamond: [Endpoints](#Endpoints)

:small_blue_diamond: [Informações do JSON](#Informações-do-JSON-floppy_disk)

:small_blue_diamond: [Desenvolvedores](#Desenvolvedores)

## Descrição do projeto 
<p align="justify">
  Microserviço realizado no projeto de extensão Fábrica de Software (2023.1), da universidade UNIPÊ (centro universitário de João Pessoa), para a PM-PB.
</p>
<p align="justify">
  O microserviço tem como funcionalidade extrair textos de arquivos PDFs, dependendo do tipo do documento que foi escolhido pelo usuário (Boletim Oficial ou genérico), e armazená-los em um banco de dados para que possa ser utilizado depois. Possuindo endpoints (urls), que retornam dados JSOn, para que usuário possa ver o status da requisição e os dados que foram extraidos do documento.
</p>

## Tecnologias utilizadas
<p align="center">
  <img src="http://img.shields.io/static/v1?label=Python&message=3.10.4&color=blue&style=for-the-badge&logo=PYTHON"/>
  <img src="https://img.shields.io/static/v1?label=Django Rest&message=framework&color=red&style=for-the-badge&logo=DJANGO"/>
  <img src="https://img.shields.io/static/v1?label=Celery&message=Async queue&color=dark green&style=for-the-badge&logo=CELERY"/>
  <img src="https://img.shields.io/static/v1?label=PdfPlumber&message=Library&color=blue&style=for-the-badge&logo=PDFPLUMBER"/>
  <img src="http://img.shields.io/static/v1?label=PostgreSQL&message=Database&color=red&style=for-the-badge&logo=POSTGRESQL"/>
</p>

- [Python docs](https://docs.python.org/3.10/)
- Django Rest Framework ([docs](https://www.django-rest-framework.org/)) - Um framework baseado em Django (que tem como dependencia o mesmo) responsável pela criação da API, criação das rotas e a base do projeto
- Celery ([docs](https://docs.celeryq.dev/en/stable/)) - Celery é um sistema de filas de tarefas assíncronas, que realiza as atividades dependendo da fila e não em tempo de envio do usuário. No projeto, ele é utilizado para fazer o upload do documento e a extração dos textos, para que não seja necessário o usuário esperar a conclusão da tarefa anterior para enviar outros documentos. O celery utiliza o método de multi-threading.
-  PDFPlumber ([docs](https://pypi.org/project/pdfplumber/)) - PDFPlumber é um projeto open-source, feito em python, baseado em outra biblioteca (a PDFMiner, tendo ela como dependencia também), que tem como funcionalidade extrair dados de arquivos PDFs, podendo utilizar esses dados para a manipulação. Em nosso projeto, a PDFPlumber é responsável por extrair os dados dos PDFs enviados pelo usuário, dados esses que serão manipulados e formatados para que possamos retornar o JSON.
-  PostgreSQL ([docs](https://www.postgresql.org/docs/)) - No projeto, foi responsável pelo armazenamento dos dados.

## Funcionalidades

:heavy_check_mark: Extrair texto de forma detalhada e especifica (caso da opção de Boletim Oficial)

:heavy_check_mark: Extrair de texto de forma genérica, extraindo todo o conteúdo de uma página do PDF e salvando (caso da opção Genérica)

:heavy_check_mark: Pesquisar dados de um documento pelo UUID da requisição  

:heavy_check_mark: Ver status da Requisição (Em espera, Em andamento, Concluído, Erro de raspagem ou Erro de upload)

:heavy_check_mark: Ver todos os dados raspados existentes no banco de dados

## Pré-requisitos

### Celery
- Para conseguir rodar o celery, é necessário, primeiro, instalar um broker (Um app responsável pela execução e mantimento das tarefas do celery). No projeto, foi utilizado o  broker chamado RABBITMQ ([docs](https://www.rabbitmq.com/documentation.html)).
- Para fazer a instalação do RabbitMQ, é necessário ir para [Dowload Windows](https://www.rabbitmq.com/install-windows.html) e descer até a parte chamada "Dependencies" e baixar e instalar o Erlang (uma dependencia necessária para o RabbitMQ. Caso queria instalar diretamente: [Download Erlang 25.3.2](https://www.erlang.org/patches/otp-25.3.2)). Após baixar, a instalação é feita de forma simples, basta clicar em prosseguir (next) até o final.
- Após a instalação do Erlang, faça o download do RabbitMQ na parte, logo abaixo de dependencies, chamada "Direct Downloads", e clique no link que estará na grade de "Downloads". A instalação também é feita de forma simples, basta clicar em prosseguir (next) até o final.
![Visualização da página dita nos texos acima](https://github.com/arthurhenrique02/testeProjetoPM/assets/109195033/e70b9599-94fc-4b61-90d0-71451902e90c)
- Feito a instalação do Erlang e do RabbitMQ, abra o explorador de arquivos, vá em Disco local, clique em arquivos de programas e procure uma pasta chamada RabbitMQ Server. Após localizá-la, entre na pasta, clique na pasta chama rabbitmq_server-... (após o traço averá a versão do server do RabbitMQ, por exemplo 3.11.17), entre na pasta chamada sbin, e execute como administrador o arquivo chamado 'rabbitmq-server'. Após a execução deste arquivo, o Broker para o Celery estará funcionando e você estará habilitado a utilizá-lo.
- Caminho e arquivo que será executado como administrador:
![Captura de tela 2023-07-06 170546](https://github.com/arthurhenrique02/testeProjetoPM/assets/109195033/8c3796df-7d8c-4573-af4c-fac5e5d16669)

### PostgresSQL
- Para conseguir habilitar o banco de dados do postgres é necessário que instale-o. [Download PostgreSQL](https://www.postgresql.org/download/), para instalar a versão do windows, clique na opção windows e, após entrar na página de download para windows, clique na opção "Download the installer" (localizado no primeiro parágrafo).

![PostgreDownload](https://github.com/arthurhenrique02/raspaDocPM/assets/109195033/a17d79a7-83ee-4493-b403-44b4c37f0864)

- Basta clicar prosseguir (next) até o final e estará feita a instalação.
- #### Configurando o banco de dados:
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - Após a instalação, procure pelo app chamado "pg admin" e entre no mesmo, faça a configuração do seu app (usuário e senha. Recomendado que coloque 'admin' nos dois campos). Este usuário e senha não poderão ser recuperados, então lembre deles.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - Feito a configuração, clique em Servers, depois em localhost (caso não exista o 'localhost', clique com o direito em 'Server', clique em create e crie), após colocar sua senha, clique com o botão direito em databases, clique em create e crie um banco de dados chamado 'RaspaDocDB' coloque o usuário como 'postgres' e o DB estará pronto para uso.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Após os cliques (servers -> localhost -> databases -> create -> database) a seguinte tela deverá aparecer:
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ![Captura de tela 2023-07-06 174133](https://github.com/arthurhenrique02/testeProjetoPM/assets/109195033/14909b16-b025-4026-b685-63be9ca9c399)

### Para as outras dependencias
- Não há nenhum outro requerimento à parte para as outras dependencias, basta fazer um pip install -r requirements.txt (mas calma, faça isso apenas na explicação do parte de [Como rodar a aplicação](#como-rodar-a-aplicação-arrow_forward))


## Como rodar a aplicação :arrow_forward:

Baixe o projeto na aba ![Capturar](https://github.com/arthurhenrique02/testeProjetoPM/assets/109195033/dea87f4a-14ed-4830-a650-eb86236133f9)
(clique no botao e baixe o zip do projeto, depois faça a extracao do mesmo em sua máquina
No terminal).
Ou clone o projeto: 

&nbsp; &nbsp; :small_blue_diamond: Crie uma pasta, entre na mesma e clique com o botao direito dentro da área, após isso clique em 'Git Bash here' e digite o comando:
```
    git init
```
&nbsp; &nbsp; :small_blue_diamond: Após inicializar um repositório, digite o seguinte comando para clonar: 

```
    git clone https://github.com/arthurhenrique02/testeProjetoPM.git
```

Após o download/clone do projeto, abra-o em uma ide (estaremos utilizando o [Visual Studio Code](https://code.visualstudio.com/) para os prints de demonstração).

Crie um ambiente virtual(venv) para baixar as dependências, basta digitar o seguinte código no terminal da ide: 
```
python -m venv venv
```
Após ter criado o ambiente virtual precisaremos ativá-lo: 

<ul>
<li><strong>No Unix ou MacOS, usando o bash shell: </strong><code>source venv/bin/activate</code></li>
<li><strong>No Unix ou MacOS, usando o csh shell: </strong><code>source venv/bin/activate.csh</code></li>
<li><strong>No Unix ou MacOS, usando o fish shell: </strong><code>source venv/bin/activate.fish</code></li>
<li><strong>No Windows usando o Command Prompt:</strong> <code>.\venv\Scripts\activate</code></li>
<li><strong>No Windows usando o PowerShell: </strong><code>venv\Scripts\Activate.ps1</code></li>
</ul>
Use apenas um dos comandos dependendo do sistema operacional em que você irá rodar o projeto. Após a utilização do comando, a ide deverá aparecer da seguinte forma no terminal:


&nbsp; &nbsp; &nbsp; &nbsp;![demonstração de sucesso na inicialização da venv](https://github.com/arthurhenrique02/testeProjetoPM/assets/109195033/f4952ef1-9659-47dc-ab09-f4a82412609b)

&nbsp; &nbsp; &nbsp; &nbsp;Deverá aparecer o texto '(venv)' antes do caminho da sua pasta

<br>
<br>

Depois do ambiente ser ativado baixe todas as dependências na venv pelo pip: 

```
pip install -r requirements.txt
```



Depois de ter todas as dependências na sua maquina e o ambiente ativado rodaremos o comando para migrar as tabelas necessárias para o BD: 

```
python(ou py) manage.py migrate
```

Agora criaremos um super usuário para que será necessário para o envio de documentos para raspagem, pois a API utiliza usuários cadastrados no banco de dados: 

```
python(ou py) manage.py createsuperuser
```

Aqui está um exemplo de como irá aparecer: 

![resultado superuser](https://github.com/arthurhenrique02/testeProjetoPM/assets/118818233/d01762ad-9517-4ae9-9a58-a1092864877b)

Após todos esse passos, o projeto estará pronto para ser inicializado.
Então, para que o projeto possa ser utilizado após sua inicialização, precisaremos inicalizar o celery:

&nbsp; &nbsp; Abra um outro terminal clicando no + no canto superior direito do terminal atual (Segue exemplo no Vs Code: ![terminal](https://github.com/arthurhenrique02/testeProjetoPM/assets/109195033/34f0ab1b-0ed1-479e-9023-48878b31016d))

&nbsp; &nbsp; Após abertura de outro terminal, digite o seguinte código no mesmo (no caso do windows):
```
    celery -A raspaDoc worker -l info --pool=solo
```
&nbsp; &nbsp; Ou, no caso de linux:
```
    celery -A raspaDoc worker -l info
```
Deverá aparecer o seguinte código no terminal, após a execução do comando acima:

![rodar celery](https://github.com/arthurhenrique02/testeProjetoPM/assets/109195033/9112bc81-6345-4800-9393-5471899f664d)

Após iniciar o celery, volte pro terminal anterior e digite o seguinte código para iniciar o servidor da API:
```
python manage.py runserver
```
Deverá aparecer o seguinte código no terminal, após a execução do comando acima:

![rodar servidor](https://github.com/arthurhenrique02/testeProjetoPM/assets/109195033/e25ee162-3c69-4ca3-8b92-803b4115d3a9)

Após seguir todos os passos anteriores, a API estará funcionando e você poderá acessá-la a partir de seu browser, basta apertar CTRL + BOTÃO ESQUERDO DO MOUSE no link do servidor que aparecer ao rodar o servidor, ou digitar 'localhost:8000' no seu browser. Segue exemplos:

https://github.com/arthurhenrique02/testeProjetoPM/assets/109195033/fc911d5a-dd11-4ec0-ab4b-49a484c93683

Após acessar a API, vemos que retornar um 'erro' porque não encontrou a mesma, isso ocorre pois a API não possui um endpoint padrao, então é necessário que acessemos as endpoints '/admin' ou '/requisicoes' ou '/raspagem' para que possamos encontrar os dados dela.

## Endpoints

### /admin

Endpoint criada pelo próprio django que permite você entrar com um super usuário e manipular os dados que existem na aplicação. Como o próprio nome ja diz, é uma endpoint para a administração da aplicação.

Ao acessá-la a primeira vez, será pedido usuário e senha (esse foram criados ao utilizar o comando de createsuperuser, no qual o mesmo foi feito na parte de [Como rodar a aplicação](#como-rodar-a-aplicação-arrow_forward))
Área de login do django:

![djangoAdminLogin](https://github.com/arthurhenrique02/testeProjetoPM/assets/109195033/76b1d8d9-244a-4851-ad4f-c7250dad4bfb)

Após fazer o login com usuário e senha criados será redirecionado para a seguinte página:

![posLoginDjango](https://github.com/arthurhenrique02/testeProjetoPM/assets/109195033/5490d8df-ec4d-466d-b469-d46b72da537b)

Na página acima é possivel manipular os dados que estão no banco de dados do projeto.

### /requisicoes

A endpoint de requisições, como o próprio nome já diz, é para visualização dos dados de requisições. Nele encontramos os dados de todas as requisições feita para aquela API.

![image](https://github.com/arthurhenrique02/testeProjetoPM/assets/109195033/6e0e73d2-5600-4eae-85a9-9b8ecd9d871e)

Na endpoint acima apenas é possível verificar os dados, não possível inserir dados na mesma.

### /raspagem

A endpoint de raspagem é responsável pela inserção de dados ao banco de dados. É nela que as inserções de PDFs para raspagem serão feitas.
Ao enviar um dado na endpoint de raspagem, será criado uma requisição na endpoint de requisicoes, e também será criado uma task para que o módulo chamado 'miner.py' faça a análise do tipo de raspagem que o usuário solicitou (boletim oficial ou genérico) e faça a raspagem de acordo, salvando no banco de dados e mostrando no JSON da endpoint.
Esta endpoint conterá os dados de todas as raspagens que foram feitas.
Sendo necessário que acesse-a para coleta do JSON e para inserção de novos documentos à serem raspados.

Na imagem a seguir é possivel ver que a endpoint retorna JSONs com os dados de cada raspagem:
![endpointRaspagem](https://github.com/arthurhenrique02/testeProjetoPM/assets/109195033/6236243e-204c-459c-b19f-54061dd4585c)

Ao final da rolagem, no próprio browser, é possível ver que há uma área para inserção de novos documentos (recurso provido pelo próprio Django), ele poderá ser utilizado para seus testes (ou, caso prefira, pode utilizar apps como [Postman](https://www.postman.com/downloads/) ou [Insomnia](https://insomnia.rest/download)):
![finalEndpointRaspagem](https://github.com/arthurhenrique02/testeProjetoPM/assets/109195033/d54dbfc9-8c20-4afe-b4b7-6e49b7446e6f)


## Informações do JSON :floppy_disk:

### Paginação:

Paginação existe nas duas endpoints, ela é responsável por retornar TODO o conteúdo do banco de dados em apenas um JSON, tornando-o a API mais rápida e eficaz, já que, dependendo do tamanho do bancos de dados, poderia demorar horas ou dias para que criasse apenas um JSON com todos os dados do mesmo. A paginação faz com que separe o JSON por paginas ao atingir uma determinada quantidade de dados no elemento. No projeto, a quantidade de elementos limite é dada por 30 documentos, ou seja, na mesma página JSON teremos dados de raspagem de 30 documentos, a mesma coisa serve para a endpoint de requisições (teremos dados de 30 requisiçoes).

#### Mas como acessariamos os dados de outras páginas?

No inicio do JSON, há as chaves de acesso chamadas 'next' e 'previous', nelas haveram links, caso haja mais de uma página JSON, ou nulo caso não haja nenhuma. Pode-se utilizar esses links para acessar as outras páginas, ele funcionará normalmente
A chave next mostra a proxima página do JSON, por exemplo: se está na pagina um e utiliza o link que está na chave next para ir para a proxima, será mostrado todos os JSON da página dois.
A chave previous mostra a pagina anterior do JSON, por exemplo: se está na página dois e deseja verificar a página um, basta utilizar o link que está na chave previous e ele te mostrará.

#### O que seria as chavse count e result?

A chave count basicamente mostra a quantidade total de elementos que o JSON está retornando (nesse caso, a quantidade de dados que estão no banco de dados).
A chave result retorna os dados do banco de dados.

### Exemplos sobre a paginação:

Quando não há mais que 30 elementos na página:

![exemploPaginaçãoSemElementos](https://github.com/arthurhenrique02/testeProjetoPM/assets/109195033/98832e5d-ff58-4ad7-8e92-5095f50757cc)

No exemplo acima vemos que ambos (next e previous) retornam nulo, pois não há nenhuma outra página JSON para acessar que não seja a atual.

Quando há mais que 30 elementos da página (no exemplo estaremos acessando a pagina dois para que possamos ver o link da chave previous também):

![exemploPaginacaoComElementos](https://github.com/arthurhenrique02/testeProjetoPM/assets/109195033/e91e7147-a5da-43cd-8ef9-9a96e706cc7d)

No exemplo acima vemos que ambos (next e previous) possuem links para acesso para outras páginas, pois este banco de dados possui mais que 30 elementos

#### Posso alterar a quantidade de dados que um JSON retorna?

Sim, a quantidade pode ser alterada, basta modificar a quantidade que deseja na URL. Alterando a informação 'limit' para que a página atual mostre quantos elementos você deseja. Por exemplo: se deseja apenas mostrar 10 elementos por vez, pode-se definir o limit como 10 utilizando a seguinte URL:
```
  raspagem/?limit=10
```
(O exemplo foi feito com raspagem, mas pode-se fazer na endpoint de requisicoes também.)
Após utilizar a URL acima, serão mostrados dados de apenas 10 documentos e serão incrementadas outras páginas á paginação.

![exemploPaginacaoLimiteDez](https://github.com/arthurhenrique02/testeProjetoPM/assets/109195033/5bb79d2a-02a3-4906-88fb-bbb1677ce4c1)

### Endpoint de requisições (/requisicoes):
A endpoint de requições possui o uuid, data e hora e o status de todas as requisições que foram feitas para a API.
Todos os dados desta endpoint serão preenchidos automaticamente ao enviar um documento para raspagem. O uuid é gerado aleatoriamente, mantendo o aspecto unico do mesmo, data e hora são pegas de acordo com a região que a API está (horário de Brasília) e o status será inserido automaticamento como 'em espera' (pois o documento estará salvo na fila do celery aguardando sua vez para a raspagem).

#### Para que serve o uuid?
O uuid serve para que o usuário possa pesquisar os dados na endpoint de raspagem (/raspagem), esta parte será explicada posteriormente na sub-tópico para endpoint de raspagem.

#### Para que servem data e hora?
Data e hora do envio do documento serve para que se possa checar com mais precisão qual documento você está há procura e, em caso de utilização empresarial, ver até mesmo quem estava enviando naquele momento. Mantendo, assim, uma espécie de backlog.

#### E o status, para que serve?
O status serve para ver o progresso da raspagem do documento enviado.

Temos vários tipos de status, são eles:

&nbsp; &nbsp; - Em espera (ES): status padrão que é inserido assim que o documento é enviado, serve para dizer que o documento está aguardando sua vez na raspagem

&nbsp; &nbsp; - Em andamento (EA): A raspagem do documento foi inicializada e os dados do mesmo já estão sendo extraídos

&nbsp; &nbsp; - Concluído (OK): A raspagem do documento foi um sucesso e os dados foram extraídos, podendo ser acessados na endpoint /raspagem 

&nbsp; &nbsp; - Erro de raspagem (ER): Ocorreu algum erro nas raspagem do documento, não foi possível realizá-la.

&nbsp; &nbsp; - Erro de upload (EU): Ocorreu algum erro no momento de envio do arquivo para a API, tente reenviá-lo (caso deseje).

A parte de status será atualizada com algum desses status listados acima automaticamente, durante a progressão da API, então não precisa ficar preocupado em atualizá-lo

Exemplos visuais:

![exemploEndpointRequisicoes](https://github.com/arthurhenrique02/testeProjetoPM/assets/109195033/db14049b-74ca-4b55-865f-f9e8d0601760)

No exemplo acima, vemos que existe algumas requisições com status 'concluído' e outros com status 'erro de raspagem'. Também é possível ver o uuid de cada uma e a data e hora em que foram enviadas

### Endpoint de raspagem (/raspagem): 

O JSON irá retornar diferentes quantidades de dados dependendo do modelo escolhido. Pois a opção Boletim Oficial faz uma raspagem mais detalhada (verificando por seções do documento), e retorna um JSON maior, e a opção Genérica faz a raspagem a partir das páginas do documento, retornando um JSON menor.

#### Boletim Oficial (BOF):
O JSON do Boletim Oficial (BOF) conterá 7 dados diferentes, sendo eles:

&nbsp; &nbsp; - O id do documento;

&nbsp; &nbsp; - O nome do usuário que enviou o documento;

&nbsp; &nbsp; - O modelo do documento enviado (opção selecionada pelo usuário, nesse caso "BOF");

&nbsp; &nbsp; - O documento em formato pdf;

&nbsp; &nbsp; - Todas as seções que o documento possui ([seções](#seções));

&nbsp; &nbsp; - Todas as subseções que o documento possui ([subseções](#subseções));

&nbsp; &nbsp; - Os textos relacionados a cada documento([textos](#textos)).

#### Inicio do JSON:

O inicio do JSON vai conter algumas das informações listadas anteriormente (id do docuemnto, nome do usuário que enviou, modelo do documento enviado e o documento).
Como podemor observar na imagem a seguir:

![inicioJsonBOF](https://github.com/arthurhenrique02/testeProjetoPM/assets/109195033/6ef55911-9c70-48aa-b645-6ee4d121272d)
#### Seções: 

O JSON de seções irá conter uma lista de seções e cada elemento da lista irá conter 3 informações:

&nbsp; &nbsp; - secao_id: o id de cada seção.

&nbsp; &nbsp; - nome: o nome da seção, contendo a numeração da parte e o seu título.

&nbsp; &nbsp; - documento: o documento em que essa seção está.

![JSON secoes](https://github.com/arthurhenrique02/testeProjetoPM/assets/118818233/c03cb19c-835d-4781-af64-a230be5b61b7)

#### Subseções: 

O JSON de subseções irá conter uma lista de subseções e cada subseção irá conter 3 informações:

&nbsp; &nbsp; - subsecao_id:o id de cada subseção.

&nbsp; &nbsp; - nome: o nome da subseção, contendo a sua numeração e o seu título.

&nbsp; &nbsp; - documento: o documento em que essa subseção está.

![list-subsecoes JSON](https://github.com/arthurhenrique02/testeProjetoPM/assets/118818233/0f92ff60-ded7-445f-b577-61566a2f9230)

#### Textos: 

O campo de textos conterá quantidade de dados diferentes dependendo do modelo de raspagem:

#### Textos do Boletim Oficial:

Uma lista de todos os textos do pdf com os seguintes dados:

&nbsp; &nbsp; - texto_id: o id correspondente ao texto na tabela de textos.

&nbsp; &nbsp; - paginas: o número da pagina descrita no documento de onde o conteudo do texto foi retirado.

&nbsp; &nbsp; - subsecao: nome da subseção em que esse texto está localizado.

&nbsp; &nbsp; - subsec_da_subsec: nome da subseção contida na subseção em que o texto está localizado.

&nbsp; &nbsp; - conteudo: textos contidos na subseção da subseção informada.

&nbsp; &nbsp; - documento: o documento de onde os dados foram retirados.

![list textos JSON BOF](https://github.com/arthurhenrique02/testeProjetoPM/assets/118818233/8041c224-f0c4-4f6f-81ea-03c8587434e9)


#### GEN:

O JSON do modelo de raspagem genérico(GEN) retornará apenas 5 dados, sendo eles:

&nbsp; &nbsp; - O id do documento;

&nbsp; &nbsp; - o nome do usuário responsável pelo envio;

&nbsp; &nbsp; - O modelo do documento enviado (explicado no subtópido de [Boletim Oficial](#boletim-oficial-bof) o seu funcionamento);

&nbsp; &nbsp; - O documento em formato pdf (também explicado no subtópido de [Boletim Oficial](#boletim-oficial-bof) o seu funcionamento);

&nbsp; &nbsp; - Os textos de cada página do documento.

![JSON modelo GEN](https://github.com/arthurhenrique02/testeProjetoPM/assets/118818233/68dd001d-4c34-4750-a0a3-8081c3f8f276)

#### Textos:

O JSON de textos retornará o conteúdo referente a aquela página do documento, por exemplo: Retornatará o conteúdo da página um, página dois, sem a divisão por seções (como ocorre no Boletim Oficial)

Retonará os seguintes dados:

&nbsp; &nbsp; - texto_id: o id correspondente ao texto na tabela de textos genéricos.

&nbsp; &nbsp; - pagina: O número da pagina do próprio pdf (exemplo: 1, 2, 3), diferentemente do Boletim Oficial que retira os dados do próprio texto.

&nbsp; &nbsp; - conteudo: textos de cada pagina.

&nbsp; &nbsp; - documento: o documento de onde os dados foram retirados.

![JSON textos genericos](https://github.com/arthurhenrique02/testeProjetoPM/assets/118818233/4f5849e2-a051-4e14-8158-2477458ba59d)

## Resolvendo Problemas :exclamation:

Foram encontrados alguns problemas gerados durante o desenvolvimento desse projeto aqui está a como conseguimos resolvê-los.

### Modulo de raspagem(miner.py) não conseguindo acessar o banco de dados:

Por segurança, o Django não permite que módulos fora do escopo das APPS acessem o banco de dados então, para conseguirmos acessar este banco de dados no módulo de raspagem, fizemos uma lógica para que pudessemos acessá-lo e enviar os dados dentro do mesmo arquivo em que está a lógica de raspagem(miner).
Porém, como esse arquivo não está conectado diretamente a nenhum app do django, não foi possivel acessar o banco de dados de forma convencional.
Dessa forma, implementamos um código para que o miner consiga enviar dados para o BD sem precisar estar num app.

Este foi o código:

![imagem solução Django](https://github.com/arthurhenrique02/testeProjetoPM/assets/118818233/f2458639-6b12-403d-9180-af3887c1564b)

### Erro ao salvar no Banco de dados PostgreSQL:

Diferentemente do SQLite, que não precisava de nenhuma formatação no texto para que pudessemos salvar no banco de dados, o PostgreSQL necessita desta formatação. Sendo necessário tirar os meta-caracteres nulos (\x00) para que seja possível salvar no Banco de Dados. Para isso tivemos que utilizar o metodo '.replace' para retirar todos esses metas-caracteres (tanto para a raspagem do Boletim Oficial, como o Genérico)

Este foi o código:

![replaceMetaCharacter](https://github.com/arthurhenrique02/testeProjetoPM/assets/109195033/9f0f9298-cc19-461d-bc23-f44a08a69b81)


## Desenvolvedores

| [<img src="https://avatars.githubusercontent.com/u/109195033?v=4" width=115><br><sub>Arthur Henrique</sub>](https://github.com/arthurhenrique02) |  [<img src="https://avatars.githubusercontent.com/u/56697105?v=4" width=115><br><sub>Henrique Freitas</sub>](https://github.com/HenriqueOFreitas) |  [<img src="https://avatars.githubusercontent.com/u/118818233?v=4" width=115><br><sub>Gabriel de Almeida</sub>](https://github.com/gabrielAM12) |
| :---: | :---: | :---:

## Licença 

The [MIT License]() (MIT)

Copyright :copyright: 2023 - RaspaDoc
