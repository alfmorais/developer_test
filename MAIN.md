# Take5 - Contratação Desenvolvedor Back-end

## Conhecimento dos Frameworks
Essa seção terá um breve descritivo das tecnologias que foram utilizadas e o conhecimento aprofundado das tecnologias utilizadas no projeto pelo Desenvolvedor. 

### Git
Git é um software de controle de versões distribuído, open source e muito utilizado para controle de versões no desenvolvimento de software. Tenho conhecimento do Git e suas ferramentas através dos cursos [Git e GitHub do básico ao avançado (c/ gist e GitHub Pages) do Matheus Battisti](https://www.udemy.com/course/git-e-github-do-basico-ao-avancado-c-gist-e-github-pages/) e [Introdução ao Git e ao GitHub](https://web.digitalinnovation.one/course/introducao-ao-git-e-ao-github/learning/75b9fe49-6ed4-4480-83a7-7e37fc356aa9/?back=/browse). 

### Django
Django é um framework para desenvolvimento rápido para web, escrito em Python, que utiliza o padrão model-template-view. Tenho conhecimento do Django através dos cursos [Desenvolvimento para Internet e Banco de Dados com Python e Django](https://web.digitalinnovation.one/course/desenvolvimento-para-internet-e-banco-de-dados-com-python-e-django/learning/d1e01e99-4468-4119-8962-82e5ea80b118/?back=/browse), [Programação Web com Python e Django Framework: Essencial](https://www.udemy.com/course/programacao-web-com-django-framework-do-basico-ao-avancado/) e do livro [Aprenda Django 3 com exemplos - Antonio Melé](https://novatec.com.br/livros/aprenda-django3-com-exemplos/).

### Django Rest Framework 
Django Rest Framework (DRF)é um framework flexível e poderoso para desenvolvimento de APIS para Web. O conhecimento adquirido do DRF foi através do curso [Crie APIs REST com Python e Django REST Framework: Essencial](https://www.udemy.com/course/criando-apis-rest-com-django-rest-framework-essencial/) e a [Documentação Técnica do Framework](https://www.django-rest-framework.org/).

### PL-SQL (MySQL, MSSQL)
O MySQL é um sistema de gerenciamento de banco de dados, que utiliza a linguagem SQL como interface. Toda aplicação foi desenvolvida com o MySQL, porém não tinha estudado esse banco de dados antes. Os materiais de consulta estão referenciados nas Referências.

## Teste

### Parte 1

#### Dê um fork deste projeto

#### Crie uma branch dentro do seu fork com o seu email como nome. 

#### Para os próximos passos, gostaríamos que você efetuasse os pushs conforme sua evolução.

### Parte 2

#### Dentro do diretório deste projeto, inicialize um projeto Django, com o nome de "take5"

#### Rode as migrações do seu projeto para inicializar as tabelas do django

#### Inicie o servidor e verifique se sua aplicação está funcionando

#### Dentro do projeto, inicialize uma aplicação chamada "survey"

#### Inclua survey no projeto take5

#### Crie modelos para sua aplicação: 

- Survey (Pesquisa)
- SurveyQuestion (Perguntas da pesquisa)
- SurveyQuestionAlternative (Alternativas para as perguntas da pesquisa)
- SurveyUserAnswer (Respostas dos usuários para a Pesquisa)

O códgio foi criado no arquivo models.py da aplicação survey e pode ser consultado abaixo: 

~~~python
from django.db import models


# Create your models here.
# This class are our database models regarding survey
class Survey(models.Model):
    """
    This class will created a survey name in our database
    """
    survey_id = models.AutoField(primary_key=True)
    survey_name = models.CharField(max_length=255)


class SurveyQuestion(models.Model):
    """
    This class will created a survey question in our database
    """
    survey = models.ForeignKey('Survey', on_delete=models.CASCADE)
    question_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=255)


class SurveyQuestionAlternative(models.Model):
    """
    This class will created a question alternative for our survey question
    """
    survey_question = models.ForeignKey(
        'SurveyQuestion', on_delete=models.CASCADE
    )
    first_alternative = models.CharField(max_length=255)
    second_alternative = models.CharField(max_length=255)
    third_alternative = models.CharField(max_length=255)


class SurveyUserAnswer(models.Model):
    """
    This class will created a answer for our survey question
    """
    user_answer = models.ForeignKey(
        'SurveyQuestionAlternative',
        on_delete=models.CASCADE
    )
~~~

#### Gere a migração do Banco de Dados para que suas tabela sejam criadas

A migração do banco de dados foi gerada através dos comandos <b>django-admin</b> no terminal da IDE.

1° Comando:

~~~cmd
python manage.py makemigrations survey
~~~

2° Comando

~~~cmd
python manage.py migrate
~~~

#### Cadastre uma pesquisa utilizando uma das formas abaixo descritas:

1. Criar uma pesquisa utilizando o Painel do Django
2. Criar uma pesquisa utilizando o Shell (_Caso opte por esta opção é necessário inserir os comandos utilizados no arquivo shell.py localizado neste projeto_)

Nesse projeto iremos fazer da seguinte maneira: criar uma pesquisa utilizando o Painel do Django. 
A pesquisa inicialmente foi elaborada em arquivo.txt e depois vamos inserir no Painel do Django. Abaixo a pesquisa inicial: 

~~~txt
Questionário Django

Qual é o framework Python que tem o seguinte slogan: "DjangoThe web framework for perfectionists with deadlines."

a) Flask
b) FastAPI
c) Django

Qual é o comando para criar um projeto em Django?

a) django-admin startproject <name_project>
b) python manage.py runserver
c) uvicorn main:app --reload

Qual é o comando para iniciar o servidor local do Django?

a) flask run
b) python manage.py runserver
c) uvicorn main:my_awesome_api --reload
~~~

### Parte 3

#### Instale o Django Rest Framework no projeto, utilizando o PIP e incluindo ele no seu settings.py

#### Crie uma view para apresentar suas pesquisas, associando ela a uma URL do seu projeto

#### Crie um serializer para pegar Survey, SurveyQuestion e SurveyQuestionAlternative. Tente utilizar o prefetch_related nas queries para diminuir a quantidade de queryes necessárias para a apresentação dos dados

#### Acesse a página da sua pesquisa e copie o JSON de resultado para o arquivo result.json situado no diretório raiz deste projeto

## Agradecimento

## Referências
https://www.django-rest-framework.org/
https://buildmedia.readthedocs.org/media/pdf/django/3.2.x/django.pdf
https://www.youtube.com/watch?v=OUZIaoCSJas
https://www.delftstack.com/pt/howto/django/django-mysqldb/
https://stackoverflow.com/questions/24462007/how-to-deal-with-this-error-1049-unknown-database-users-ohyunjun-work-astra/24462224
https://stackoverflow.com/questions/7759170/mysql-table-doesnt-exist-but-it-does-or-it-should
https://dev.mysql.com/doc/refman/8.0/en/identifier-case-sensitivity.html
