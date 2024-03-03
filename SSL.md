docker exec -it hh-svcs-nginx-1 bash

apt update -y && apt upgrade -y
apt install software-properties-common -y
add-apt-repository 'deb http://ftp.us.debian.org/debian/pool/main/p/python-certbot/certbot_2.1.0-4_all.deb bookworm main' -y
apt install certbot -y && apt install python3-certbot-nginx -y
mkdir -p  /var/www/html
certbot certonly --nginx --force-renewal -d helping-hands.duckdns.org
