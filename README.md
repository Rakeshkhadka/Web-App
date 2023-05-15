# weather-data-app-backend
### Clone repository to yout computer
$ git clone https://github.com/Rakeshkhadka/weather-data-app.git

### Go to project directory
<pre> cd weather-data-app </pre>

### Create Virtual Environment and activate it
<pre>
sudo apt-get install virtualenv
virtualenv env
source venv/bin/activate -----> for linux
venv\scripts\activate    -----> for windows terminal
pip install -r requirements.txt
</pre>

### Set up the database by running migrations:
<pre>
python manage.py migrate
</pre>
### Feed weather data to the database
<pre>python manage.py ingestdata</pre>
### Create Summary of the weather data
<pre>python manage.py createsummary</pre>
### After data migration and data ingestion run the server
<pre>python manage.py runserver</pre>
Access the weather application api by visiting $ http://127.0.0.1:8000/api/ in your web browser.

### For API documentation
http://127.0.0.1:8000/docs/
