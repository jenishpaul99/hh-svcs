docker exec -it hh-svcs-nginx-1 bash

apt update -y && apt upgrade -y
install software-properties-common -y
add-apt-repository 'deb http://ftp.us.debian.org/debian/pool/main/p/python-certbot/certbot_2.1.0-4_all.deb bookworm main' -y
apt install certbot -y
mkdir -p  /var/www/html
certbot certonly --webroot --webroot-path=/var/www/html --email jenis1303@gmail.com --agree-tos --no-eff-email --staging -d helping-hands.duckdns.org

certbot certonly --webroot --webroot-path=/var/www/html --email jenis1303@gmail.com --agree-tos --no-eff-email --force-renewal -d helping-hands.duckdns.org
