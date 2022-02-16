# **Router_Detial API's Project on Django framework of Python**
The project provides 2 API's. One is just to view all the router_details and the other is to retrive, update and delete the router details from the database table. The project uses the default sqlite database provided by Django framework of python.

# Local setup of the application
1. Run ```pip install -r requirements.txt``` on the terminal of the VS code.
2. Create a virtual env using commang '''virtualenv venv'''. After that activate the same using command ```.\venv\Script\activate```.
3. Run ```python manage.py runserver```.
4. Hit http://127.0.0.1:8000/router_detail URL to see all the router details that are been inserted into router_detail table, through http://127.0.0.1:8000/admin panel.
5. Hit http://127.0.0.1:8000/router_detail/ url To retrive, update and destroy any router detail in the router_detail table.
6. Deployment is not done, as dont have access to any server. By default Django provides its in-built webserver, on which I had tested my API's.

# Server instructions of the application to deploy the changes on the test server
1. Log onto the server using "ssh sifarstest@45.79.120.109".
1. First we need to get into our proj directory '/travelidu-bots' and open the Git Bash here.
2. Pull all the changes from the develop branch to the local m/c using ```git pull origin develop```.
3. Activate the virtual env using command ```source ../venvs/travelidu/bin/activate``` on server and then run migrations using ```python manage.py migrate```.
4. Run ```sudo systemctl daemon-reload``` to notifies the system about the changes in the configurations.
5. restart (or reload) the service using ```sudo systemctl restart gunicorn```.