link for youtube -> https://www.youtube.com/watch?v=0sOvCWFmrtA&list=PLzcSkN75M0CKWlTLVF6zrwaAWVpN0JCC7&index=1&t=65990s&ab_channel=freeCodeCamp.org


py -3 -m venv venv  <--- creates virtual environment for the project for windows

python3 -m venv venv <---- creates virtual environment for the project for mac

don't forget to select correct python select interpreter 

venv\Scripts\activate.bat <------ to use virtual environment in terminal for windows

source venv/bin/activate <------ to use virtual environment in terminal for mac

venv\Scripts\deactivate.bat

pip install fastapi[all] <----- to install fastapi


uvicorn main:app --reload



pip install psycopg2 <--- to install psycopg2 

pip install sqlalchemy <--- to instal SQLAlchemy

pip install passlib[bcrypt] <--- to install bcrypt and passlib

pip install python-jose[cryptography] <--- to install jose


alembic section
----------------------------------------------------------------------------------

pip install alembic <---- to install alembic

0. alembic --help 
1. alembic init alembic
   
   some code changing in env.py

2. alembic revision -m "create post table"
3. alembic upgrade df0bc9d6a4a5


alembic current < - to check current revision
alembic heads   < - to check lattest revision
alembic upgrade 749609cec5e9   OR  alembic upgrade head <- to upgrade

to roll back, or undo some changes:
alembic downgrade df0bc9d6a4a5 or alembic downgrade -1 


alembic upgdare +2 <- to go 2 revision +


to autogenerate 
alembic revision --autogenerate -m "add votes"



git section
------------------------------------------
Before uplaoding to git you should
1. pip freeze > requirements.txt     
-> after that anyone can download libraries using pip install -r requirements.txt     
2. create .gitignore



heroku section
----------------------------------------------------
docs-tutorial:
https://devcenter.heroku.com/articles/getting-started-with-python#set-up  
https://dashboard.heroku.com/apps   <-- dashboard

heroku --version
git remote <--- to check remotes
heroku logs -t <--- to view logs
heroku ps --help
heroku apps:info nameoftheapp <-- to see information


steps:
1. heroku login
2. heroku create appname
3. git push heroku main 
4. create Procfile in main directory
5. web: uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-5000} <-- add to Procfile
6. 1. git add . 2. git commit -m "zdaw" 3. git push origin main 4. git push heroku main 
7. heroku addons:create heroku-postgresql:mini
8. check in dashboard -> app that we created -> Settings -> Config vars -> add config vars -> and add config vars
you can find heroku database information inside click addons-name in website -> Settings
9. heroku ps:restart
10. heroku run "alembic upgrade head"  <-- to upgrade almebic in our prod postgresql server
11. heroku ps:restart

push out changes
steps:
1. make changes in a code
2. -git add  -git commit  -git push origin main  -git push heroku main

if we made changes in alembic revision
steps:
1. -git add  -git commit  -git push origin main  -git push heroku main
2. heroku run "alembic commands"

if you want to deploy one porject to two different heroku accounts:
1. heroku login
2. heroku git:remote -a your-second-heroku-app-name
3. git push heroku main


if you use selenium and want to work with heroku:
1. heroku buildpacks:add --index 1 https://github.com/heroku/heroku-buildpack-google-chrome.git
2. in code:
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
options = Options()
options.binary_location = '/app/.apt/usr/bin/google-chrome-stable'
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
3. git add commit push, git push heroku main
4. heroku restart

CI/CD section
-----------------------------------------------------------------------
link:
https://docs.github.com/en/actions/quickstart
https://github.com/marketplace
https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python
https://docs.github.com/en/actions/using-containerized-services/creating-postgresql-service-containers

steps:
1. create .github folder inside .github create workflows folder
2. create filename.yml file
3. write script
4. -git add  -git commit  -git push origin main
5. go to github -> repository -> Actions


1. go to github -> repo -> Settings -> Environments -> create environment
2. create secrets inside environment


HEROKU_API_KEY  -> heroku account settings -> api-key
HEROKU_APP_NAME -> library-alish
HEROKU_EMAIL -> heroku account email



Docker section
----------------------------------------------
to use Docker
1. create Dockerfile and add some code
2. docker build -t fastapi <-- run on terminal
3. docker image ls <-- to check images
4. create docker-compose.yml and add some code
5. docker-compose up -d <-- run command
6. docker ps -a 

also 
1. docker-compose down

2. docker logs fastapi-api-1 <--- to check logs

3. go into file: cat docker-compose.yml

docker-compose -f docker-compose-dev.yml up -d




test section
---------------------------------------
pip install pytest <--- to install pytest

pytest -v 

pytest -v -s tests\test_users.py

pytest --disable-warnings

pytest -v -x -s           

pytest tests\test_posts.py -v -s



-s <-- to see print() statement
-v <-- to see Passed instead .
-x <-- stop test if not passed



