<h1 align="center">Case - Numera</h1>

<div align="center">
<a href="https://github.com/gabriel-ezequiel/case-numera/graphs/contributors" target="_blank"><img src="https://img.shields.io/github/contributors/gabriel-ezequiel/case-numera.svg?style=for-the-badge" alt="Contributors"></a>
<a href="https://github.com/gabriel-ezequiel/case-numera/network/members" target="_blank"><img src="https://img.shields.io/github/forks/gabriel-ezequiel/case-numera.svg?style=for-the-badge" alt="Forks"></a>
<a href="https://github.com/gabriel-ezequiel/case-numera/stargazers" target="_blank"><img src="https://img.shields.io/github/stars/gabriel-ezequiel/case-numera.svg?style=for-the-badge" alt="Stargazers"></a>
<a href="https://github.com/gabriel-ezequiel/case-numera/issues" target="_blank"><img src="https://img.shields.io/github/issues/gabriel-ezequiel/case-numera.svg?style=for-the-badge" alt="Issues"></a>
<a href="https://github.com/gabriel-ezequiel/case-numera/blob/master/LICENSE" target="_blank"><img src="https://img.shields.io/github/license/gabriel-ezequiel/case-numera.svg?style=for-the-badge" alt="Not specified"></a>
<a><img src="https://img.shields.io/github/repo-size/gabriel-ezequiel/case-numera?style=for-the-badge" alt="Repo Size"></a>
<a><img src="https://img.shields.io/github/languages/count/gabriel-ezequiel/case-numera?style=for-the-badge" alt="language-count"></a>
<a href="https://github.com/gabriel-ezequiel/case-numera/pulls" target="_blank"><img src="https://img.shields.io/github/issues-pr/gabriel-ezequiel/case-numera?style=for-the-badge" alt="Open Pull Requests"></a>
<a href="https://linkedin.com/in/gabriel-de-castro-ezequiel" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555" alt="LinkedIn"></a>
</div>

<!-- description -->
## 📝 Descrição
Esse é um Case proposto pela empresa Numera, que foi dado um contexto de uma empresa fictícia, onde a empresa esta tendo um problema de descentralização dos dados e a necessidade de centralizar esses dados em um único local, para isso foi proposto a criação de uma API que centralize esses dados.

Foi dados 3 endpoints que cada um dos endpoints possuem diferente escrutura, sendo elas:
- Endpoint 1: Dados de um arquivo Json
  - Link: https://numera-case.web.app/v1/survey/1/answers
- Endpoint 2: Dados de um arquivo Json, com uma estrutura diferente do Endpoint 1
  - Link: https://numera-case.web.app/v1/survey/2/answers
- Endpoint 3: Dados de um arquivo XML
  - Link: https://numera-case.web.app/v1/survey/3/answers

Para resolver esse problema foi proposto centralizar esses dados em um banco de dados, onde a API irá consumir esses dados e centralizar em um único local.

Com isso em mente, analisei cada um dos endpoints para entender a estrutura de cada um deles, e como poderia centralizar esses dados em um banco de dados. Depois que analisei resolvi fazer 2 tabelas no banco de dados sendo elas:
- users: onde entendi que cada um formulario respondido é um usuário diferente, assim criei uma tabela para armazenar os dados dos usuários.
- question_and_answer: esse pensei em criar uma tabela para armazenar as perguntas e respostas de cada um dos usuários, assim centralizando esses dados.

Essa são a estrutura de cada uma das tabelas:
- users:
  - id
  - contact_id
  - status
  - date_submitted
  - session_id
  - language
  - date_started
  - ip_address
  - referer
  - user_agent
  - country
- question_and_answer:
  - id
  - user_id
  - question
  - answer

Depois que estruturei o banco de dados um formato para centralizar os dados, comsumi cada um dos endpoints para colocar os dados no banco de dados, depois disso criei uma API para consumir esses dados centralizados.

Criei 6 endpoints para consumir esses dados, sendo eles:
- **/users/**: onde retorna todos os usuários
- **/user/{user_id}**: onde retorna um usuário específico
- **/user_with_questions_and_answers/{user_id}**: onde retorna um usuário específico com suas perguntas e respostas
- **/users_with_questions_and_answers/**: onde retorna todos os usuários com suas perguntas e respostas
- **/user_questions_and_answers_without_user/{user_id}**: onde retorna as perguntas e respostas de um usuário específico sem as informações do usuário
- **/all_user_questions_and_answers_without_users/**: onde retorna todas as perguntas e respostas sem as informações do usuários



<!-- objective -->
## 🎯 Objective
O objetivo desse projeto é centralizar os dados de 3 endpoints diferentes em um único local, depois disso criar uma API para consumir esses dados centralizados.


<!-- technologies -->
## 🚀 Technologies
O projeto foi desenvolvido utilizando as seguintes tecnologias:
- Python
  - FastAPI
  - Uvicorn
  - aiosqlite
  - requests
  - xmltodict
- SLQite
- docker

<!-- O projeto foi desenvolvido utilizando as seguintes tecnologias: PT-BR
- Python -->

<!-- how to run -->
## 🚴 How to run

Você pode usar o docker para rodar o projeto para isso basta rodar o comando abaixo.

<!-- voce pode usar o docker para rodar o projeto para isso basta rodar o comando abaixo. PT-BR -->

### 🐳 Using Docker
```bash
# Clone this repository
$ git clone https://github.com/gabriel-ezequiel/case-numera.git

# Go into the repository
$ cd case-numera

# Run the docker-compose
$ docker-compose up

# The server will start at port:8000 - access http://localhost:8000/docs
```
