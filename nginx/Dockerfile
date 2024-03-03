FROM nginx:1.25.2-bookworm

WORKDIR /helping_hands
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
RUN apt update -y && apt upgrade -y
RUN apt install software-properties-common -y
RUN add-apt-repository 'deb http://ftp.us.debian.org/debian/pool/main/p/python-certbot/certbot_2.1.0-4_all.deb bookworm main' -y
RUN apt install certbot -y && apt install python3-certbot-nginx -y
RUN mkdir -p  /var/www/html
RUN certbot certonly --nginx --force-renewal -d helping-hands.duckdns.org