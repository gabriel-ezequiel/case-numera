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
## 📝 Discription
This is a Case proposed by the company Numera, which was given a context of a fictitious company, where the company is having a problem of data decentralization and the need to centralize this data in a single location, for this it was proposed to create an API that centralizes this data.

Three endpoints were given, each of which has a different structure, namely:
- Endpoint 1: Data from a Json file
    - Link: https://raw.githubusercontent.com/gabriel-ezequiel/case-numera/refs/heads/main/datasets/dataset1.json
- Endpoint 2: Data from a Json file, with a different structure from Endpoint 1
    - Link: https://raw.githubusercontent.com/gabriel-ezequiel/case-numera/refs/heads/main/datasets/dataset2.json
- Endpoint 3: Data from an XML file
    - Link: https://raw.githubusercontent.com/gabriel-ezequiel/case-numera/refs/heads/main/datasets/dataset3.xml

To solve this problem, it was proposed to centralize this data in a database, where the API will consume this data and centralize it in a single location.

With this in mind, I analyzed each of the endpoints to understand the structure of each of them, and how I could centralize this data in a database. After analyzing, I decided to create two tables in the database, namely:
- users: where I understood that each form answered is a different user, so I created a table to store user data.
- question_and_answer: I thought of creating a table to store the questions and answers of each user, thus centralizing this data.

This is the structure of each of the tables:
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

After structuring the database and a format to centralize the data, I consumed each of the endpoints to put the data in the database, after that I created an API to consume this centralized data.

I created 6 endpoints to consume this data, namely:
- **/users/**: where it returns all users
- **/user/{user_id}**: where it returns a specific user
- **/user_with_questions_and_answers/{user_id}**: where it returns a specific user with their questions and answers
- **/users_with_questions_and_answers/**: where it returns all users with their questions and answers
- **/user_questions_and_answers_without_user/{user_id}**: where it returns the questions and answers of a specific user without the user information
- **/all_user_questions_and_answers_without_users/**: where it returns all questions and answers without user information

<!-- objective -->
## 🎯 Objective
The objective of this project is to centralize the data from 3 different endpoints in a single location, after that create an API to consume this centralized data.

<!-- technologies -->
## 🚀 Technologies
The project was developed using the following technologies:
- Python
    - FastAPI
    - Uvicorn
    - aiosqlite
    - requests
    - xmltodict
- SQLite
- docker

<!-- how to run -->
## 🚴 How to run

You can use docker to run the project for that just run the command below.

### 🐳 Using Docker
```bash
# Clone this repository
$ git clone https://github.com/gabriel-ezequiel/case-numera.git

# Go into the repository
$ cd case-numera

# Run the docker-compose
$ docker-compose up

# The server will start at port:8000 - access http://localhost:8000/
```

<!-- contributors -->
## 🤝 Contributors
<a href="https://github.com/gabriel-ezequiel/case-numera/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=gabriel-ezequiel/case-numera" />
</a>