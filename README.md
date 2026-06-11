# AP1 - Catálogo de Produtos

## Integrantes
- Gabriel Gasparini

## Descrição
Projeto Django REST com as entidades Produto e Categoria.
Foi criada a classe Categoria com relacionamento ForeignKey
com a classe Produto existente.

## Como executar localmente
git clone https://github.com/gabrielgw700-lang/catalogo-produtos
cd catalogo-produtos
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## Criação do usuário admin
python manage.py createsuperuser
Acessar: http://127.0.0.1:8000/admin/

## Endpoints 
- GET /api/produtos/
- GET /api/categorias/
- POST /api/produtos/
- POST /api/categorias/

## Link da API
http://catalogo-produtos-env.eba-jp6chvm6.us-east-2.elasticbeanstalk.com/api/