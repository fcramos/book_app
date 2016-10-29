##Book App

###_Descrição_
API endpoint de livros

###_Instalação_

Execute os seguintes comandos:
```
$ git clone https://github.com/lype86/book_app.git
$ cd book_app
$ virtualenv venv -p /usr/bin/python3
$ source venv/bin/activate
$ pip install -r requirements.txt
```

###_Preparação_

Crie o arquivo book_app/settings.ini da seguinte forma:
```
[settings]
SECRET_KEY=<chave com 54 caracteres s/ exceção>
ALLOWED_HOSTS=localhost, 127.0.0.1, <ip do host>
DEBUG=<True ou False>
```
 
###_Execução_
```
$ python manage.py migrate
$ python manage.py runserver 0.0.0.0:8000
```
