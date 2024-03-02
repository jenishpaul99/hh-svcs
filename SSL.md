docker exec -it hh-svcs-nginx-1 bash

sudo apt update -y
sudo apt upgrade -y
41  add-apt-repository 'deb http://ftp.us.debian.org/debian/pool/main/p/python-certbot/certbot_2.1.0-4_all.deb bookworm main'
42  apt install --classic certbot
43  apt install certbot

certbot certonly --webroot --webroot-path=/var/www/html --email jenis1303@gmail.com --agree-tos --no-eff-email --staging -d helping-hands.duckdns.org
