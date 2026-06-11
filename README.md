# AP2 - Catálogo de Produtos

Aluno: Gabriel Wiltgen Gasparini
Disciplina: BDCC_CDIA_26.1_8001 - Prof. Jonh Carvalho

## Sobre o projeto

Esse projeto é a evolução da AP1. Peguei o projeto Django REST que já tinha
(com Produto e Categoria) e adaptei pra rodar em produção na AWS.

O que mudei:
- Troquei o banco SQLite por PostgreSQL no RDS
- As imagens dos produtos agora vão pro S3 (usando django-storages e boto3)
- Criei os modelos Pedido e ItemPedido pro carrinho
- Subi tudo no Elastic Beanstalk
- Coloquei as senhas e chaves como variável de ambiente em vez de deixar no código

## Link da API

http://catalogo-produtos-ap2.eba-jp6chvm6.us-east-2.elasticbeanstalk.com/api/

## Endpoints

- /api/produtos/
- /api/categorias/
- /api/pedidos/
- /api/itens-pedido/
- /admin/ (painel admin)

## Arquitetura

O Elastic Beanstalk roda o Django com gunicorn. Ele conecta no banco
PostgreSQL que está no RDS, e as imagens são salvas no bucket do S3.

Browser -> Elastic Beanstalk (Django) -> RDS (PostgreSQL)

## Variáveis de ambiente

Configurei essas variáveis no painel do Elastic Beanstalk:
RDS_HOSTNAME, RDS_DB_NAME, RDS_USERNAME, RDS_PASSWORD, RDS_PORT,
USE_S3, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME

## Como acessar o admin

Entra em /admin/ e loga com:
usuario: admin
senha: Ibmec2026admin


## Rodar local

git clone https://github.com/gabrielgw700-lang/catalogo-produtos
cd catalogo-produtos
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver



Exemplo: /api/produtos/?meta_cor=azul

## Evidências

As evidências de funcionamento das alterações feitas durante o processo da ap2 estao em:
    -evidencias/Admin Djngo.png
    -evidencias/Endpoints.png
    -evidencias/Imagem salva no buckt do S3.png
    -evidencias/RDS.png