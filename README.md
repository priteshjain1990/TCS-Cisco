# TCS-Cisco
1. Run pip install -r requirements.txt on the terminal of the VS code.
2. Create a virtual env using commang "virtualenv venv". After that activate the same using command "source venv/Script/activate".
3. Run python manage.py runserver
4. Open http://127.0.0.1:8000/router_detail = To see all the router details that are been inserted into router_detail table, through http://127.0.0.1:8000/admin panel.
5. Open http://127.0.0.1:8000/router_detail/<id> = To retrive, update and destroy any router detail in the router_detail table.
6. Deployment is not done, as dont have access to any server. By default Django provides its in-built webserver, on which I had tested my API's.
