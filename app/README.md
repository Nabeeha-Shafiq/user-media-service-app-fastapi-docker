# Docker Containerized CRUD Application

# Project Description 
This project aims to give hands on practise on coding via FastAPI , maintaining standard file structure , good code practices like fucntion descripors and pep8 , the app is also containerized via Docler compose with 3 services 
1- FastAPI Web Service 

2- PostgreSQL DB Service

3- MongoDB Service

# Tech Stack Used
Backend Code : FastAPI (Python Language)
Containerization : Docker Compose
Database (User Management) : PostgreSQL

project_root/

├── app/

│   ├── core/           #database connections, logging

│   ├── api/            #api routers

│   ├── crud/           #db integration login

│   ├── schemas/        # Pydantic models for request,response 

│   ├── models/         #SQLalchemy+MongoDB models

│   └── main.py         #main app logic

├── docker-compose.yml  #sets up 3 services

├── Dockerfile          #builds app image

├── requirements.txt    #listed python dependencies

├── .env        #$environment variables for security

├── .gitignore          #ignore in git commits

└── README.md           #project documentation alongside

