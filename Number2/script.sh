#install the needed packages
sudo apt update && sudo apt-get install python3 python3-pip nginx

echo "create a working directory"
mkdir -p www/flaskapp
cd www/flaskapp

echo "create a virtual environment"
pip3 install virtualenv	
python3 -m virtualenv flaskenv 	
chmod 755 flaskenv/

echo "activate the virtual environment"
source flaskenv/bin/activate

echo "check the version"
python -V

echo "install flask & numpy"
pip3 install flask
pip3 install numpy
pip3 install gunicorn

export FLASK_APP=app.py

# outbound connection
# flask run

# inbound connection
# flask run --host 0.0.0.0

sudo iptables -I INPUT -p tcp --dport 5000 -j ACCEPT

# remove the default
sudo rm /etc/nginx/sites-available/default
sudo rm /etc/nginx/sites-enabled/default

# add the new configuration 
sudo mv flaskapp /etc/nginx/sites-available/flaskapp
sudo ln /etc/nginx/sites-available/flaskapp /etc//nginx/sites-enabled/flaskapp

sudo /etc/init.d/nginx restart

# to activate the server
# gunicorn --bind 0.0.0.0:5000 app:app --reload & >> /dev/null
