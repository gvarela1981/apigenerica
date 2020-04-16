# apigenerica
Django API using Rest Framework

# Installation
git clone https://github.com/gvarela1981/apigenerica.git

# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env-apigenerica

source env-apigenerica/bin/activate  # On Windows use `env-apigenerica\Scripts\activate`


# Install requirements
cd apigenerica

pip install -r requirements.txt

# Now sync your database for the first time:
cd apigenerica

python manage.py migrate

# Create a super user
python manage.py createsuperuser --email admin@apigenerica.com --username admin

# Test the api
python manage.py runserver