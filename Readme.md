# Installtion 
you can make a virtual environment with following command . 
```bash
virtualenv --python python3.7 venv
cd venv/bin
source acivate
```
then install dependencies using pip 
```bash
pip install -r requirements.txt
```

conigure an .env file with SECRET_KEY and DEBUG_MODE Like This.
```bash
touch .env
#in your .env file 
DEBUG_MODE = TRUE # True for Depolyment False for Production
SECRET_KEY = <your secret key> 
```
for deployment server you can run project Like this 
```bash
python manage.py runserver
```
### ROLES
We have Three Roles for this Project . 
Admin , Salesman , Customer .
Admin Role is used by django Default admin .
but SalesMan and Customer Roles are implemented 
using Django Groups and is essetinal for accesing Apis . 

for creating customer and salesman Group you can use this command .

```bash
python manage.py create_customer
python manage.py create_salesman
```
### sign up and authenticatin
after finishing with earlier commands , 
use this apis for sign up and then use token Authentication .
(Session Authentication Can be Used By Admin User)
```bash
#for signing up customer
curl --location --request POST 'http://127.0.0.1:8000/api/v1/signup/customer' \
--header 'Content-Type: application/json' \
--data-raw '{"username":"customer",
  "password" : "yourpass",
  "email" : "your@email.com"
}'
#for signing up salesman
curl --location --request POST 'http://127.0.0.1:8000/api/v1/signup/salesman' \
--header 'Content-Type: application/json' \
--data-raw '{"username":"salesman",
  "password" : "yourpassword",
  "email" : "your@email.com"
}'
```
for token authentication use this curl command

```bash
curl --location --request POST 'http://127.0.0.1:8000/api-token-auth/' \
--header 'Content-Type: application/json' \
--data-raw '{"username":"customer",
  "password" : "pass"
}'
```