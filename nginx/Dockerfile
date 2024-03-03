FROM nginx:1.25.2-bookworm

WORKDIR /helping_hands
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY renew-certificate.sh /helping_hands/