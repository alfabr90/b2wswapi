# b2wswapi
API REST para a B2W construída em Python (3.6) e usando MongoDB (4.0) como banco de dados NoSQL.

Requisitos:
* Flask (1.0.2)
* PyMongo (3.7.1)

O arquivo `instance/config.py` contém as variáveis necessárias para conexão com o banco de dados. Para iniciar o serviço que contém a API, deve-se executar:
```Shell
> ./start.sh
```

As funcionalidades que a API fornece são:
* Adicionar um planeta (informando seus nome, clima e terreno)
    * Antes de inserir o planeta desejado, a API busca no [swapi.co](https://swapi.co) pela quantidade de filmes em que esse planeta apareceu e armazena esse dado no atributo `quant_filmes`
* Listar planetas
* Buscar planetas por nome
* Buscar um planeta por ID (esse deve ser o `_id` gerado pelo MongoDB)
* Remover um planeta por ID (semelhante à funcionalidade anterior)

Para realizar os testes automatizados, basta executar:
```Shell
> pytest
```

ou

```Shell
> coverage run -m pytest
```
