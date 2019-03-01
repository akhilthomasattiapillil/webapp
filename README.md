# cloud_assignment1
## Assignment check points
1 Make the web app using 2 tier functionality-done
2 Responsive web app-done
3 use flask-done
4 use UWSGI-done
5 serve Nginix-done
6 Deployed on AWS EC2- done
## Prerequesites
### 1 install requirements.txt
it has: 
asn1crypto==0.24.0
awscli==1.16.95
botocore==1.12.85
Click==7.0
colorama==0.3.9
cryptography==2.1.4
docutils==0.14
enum34==1.1.6
Flask==1.0.2
futures==3.2.0
idna==2.6
ipaddress==1.0.17
itsdangerous==1.1.0
Jinja2==2.10
jmespath==0.9.3
keyring==10.6.0
keyrings.alt==3.0
MarkupSafe==1.1.0
pyasn1==0.4.5
pycrypto==2.6.1
pygobject==3.26.1
python-dateutil==2.7.5
pyxdg==0.25
PyYAML==3.13
rsa==3.4.2
s3transfer==0.1.13
SecretStorage==2.3.1
six==1.12.0
urllib3==1.24.1
uWSGI==2.0.17.1
virtualenv==16.3.0
Werkzeug==0.14.1

### Flask commands:
pip install virtualenv
pyvenv-3.6 env
source env/bin/activate
touch app.py .gitignore README.md requirements.txt
pip install Flask
pip freeze > requirements.txt
pip install --upgrade pip

## how to run
Go to  http://ec2-18-191-197-159.us-east-2.compute.amazonaws.com:5000/ to see the webapp

### To run locally do the steps below
go inside the folder fibgen
open a virtual environment using the command : source fibgen/bin/activate
Install Flask and uwsgi using the command :pip install uwsgi flask
now you can run the app using command : sudo python fibgen.py
it will run on the amazon instance, public DNS = http://ec2-18-191-197-159.us-east-2.compute.amazonaws.com:5000/
If running on local host , it will run on 0.0.0.0 copy and paste the link from terminal to browser.

Now UWSGI . the uwsgi python file is already in it , when you access it with code : uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi

Use the public DNS : http://ec2-18-191-197-159.us-east-2.compute.amazonaws.com:5000/
to see Uwsgi effect.
you can start the uwsgi using :sudo service uwsgi restart
you can start the nginx using   sudo service nginx restart

check the status of both service using:systemctl status uwsgi.service
                                      :systemctl status nginx.service
                                      
you can see the both service running but it gives some internal server error when i reach to Nginx .

My ref for installing flask and serving uwsgi and nginx is : https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-14-04

## In progress:
SSL certificate 

## Bugs:
Procfile path not found while serving nginx.

## License

MIT License

Copyright (c) [2019] [Akhil Thomas]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

