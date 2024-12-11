# CodeLeapTest

Hoje 10/12/2024 às 🕥 19:30 estou iniciando o teste para ingresso na Code Leap como programador Backend.

Estrutura de Dados do Servidor

A URL base do backend é

https://dev.codeleap.co.uk/careers/

A estrutura de dados do item é a seguinte:

{
    "id": "número",
    "username": "string",
    "created_datetime": "datetime",
    "title": "string",
    "content": "string"
}

Para criar um post, envie uma requisição HTTP POST com a estrutura de dados abaixo. Lembre-se de que ainda não temos um ID:

POST para

https://dev.codeleap.co.uk/careers/

A estrutura de dados do item é a seguinte:

{
    "username": "string",
    "title": "string",
    "content": "string"
}

Para obter a lista de posts, acesse o servidor com a seguinte requisição GET. Este é um exemplo do que será retornado pelo servidor:

GET para

https://dev.codeleap.co.uk/careers/

A estrutura de dados do item é a seguinte:

{
    "id": "número",
    "username": "string",
    "created_datetime": "datetime",
    "title": "string",
    "content": "string"
}
Para atualizar um item, acesse o servidor com a requisição PATCH abaixo. Note que devemos enviar o ID na URL desta vez também. Você não pode alterar as propriedades “id”, “username” ou “created_datetime”.

PATCH para

https://dev.codeleap.co.uk/careers/{OBJECT_ID}/

A estrutura de dados do item é a seguinte:

{
    "title": "string",
    "content": "string"
}
Por último, para deletar um item, basta acessar o servidor com uma requisição DELETE com o ID na URL. Por favor, note que nada será retornado do servidor.

DELETE para

https://dev.codeleap.co.uk/careers/{OBJECT_ID}/

A estrutura de dados do item é a seguinte:

{}

Direções Técnicas do Backend
A parte de backend deste teste não requer nenhuma interface de usuário. Sua tarefa é construir apenas a API para lidar com a parte de frontend deste teste.

Seu aplicativo Django deve ser capaz de receber requisições conforme descrito na “Estrutura de Dados do Servidor” acima.
