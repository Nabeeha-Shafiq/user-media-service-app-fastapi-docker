#a pyhton base image cz like core is python
# this is like the bread and butter need for the app 
#like python is the ultimate basic need here 
#, and the slim-buster is like a tag==version its not just a fancy name 
#it is a version known for being lightweight and functional avoiding documentation 
FROM python:3.10-slim-buster
#this is the directory from where all app will be run in the container
#this was not set to project root cz
WORKDIR /app

#now since /app directory sey kaam ho raha hey main os gotaa copy the requiremtnts txt there
COPY ./requirements.txt /app/requirements.txt
#this would install all dependencies in requiremrnts.txt
#why the r 
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./app /app
# now this is a multiple services app meaning it has 
#postresql db sercive 1---> container 1
#mongodb service 2 ---> container 2
#fastapi servise 3 ----> container 3
# so we need docker compose to bing all these services on a singular network
#the port on which application will bind


EXPOSE 8000 
#only for docuentation puposes just to clear out things about port mapping

#the netwoek 0.0.0.0 has this feature that it can not only listen to local and private connections 
#but it can bind with any available connections , other containers and all 
# main command that will be used to run all app , like the one command i use locally 
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]