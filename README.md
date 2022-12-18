# Poketeam v2
API em django rest (v3.11.1)


Pré Requisitos:
  - python 3.10

Como instalar
    No Linux utilize o seguinte

```
  -> python3 -m venv .venv

```

Em seguinte entre no ambiente utilizando o comando

```
source .venv/bin/activate
```


Após isso instale as dependencias


```
pip install -r requirements.txt

```


Rode as migrações utilizando o comando


```
python manage.py migrate

```

Rode o Seed com o comando


```
python manage.py seed

```
Rode o sistema localmente utilizando o comando

```
  python manage.py runserver

```

O sistema estará rodando em https://localhost:8000

para saber como utilizar a API acesse o Guiá de rotas