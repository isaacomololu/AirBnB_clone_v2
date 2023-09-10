#!/usr/bin/env bash
# Bash script that sets up my web servers for the deployment of web_static.

sudo apt-get -y update
if ! command -v nginx &> /dev/null; then
    echo "Nginx is not installed, installing now..."
    sudo apt-get -y install nginx
    echo "Nginx installed successfully"
else
    echo "Nginx is already installed"
fi

sudo service nginx start

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

# new_string="server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tindex index.html;\n\t}\n"

sed -i "s|server_name _;|server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tindex index.html;\n\t}\n|" /etc/nginx/sites-available/default

sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

sudo service nginx restart
