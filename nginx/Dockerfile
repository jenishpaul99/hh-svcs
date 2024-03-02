FROM nginx:1.25.2-bookworm

WORKDIR /helping_hands
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY nginx-entrypoint.sh /helping_hands
RUN chmod 755 /helping_hands/nginx-entrypoint.sh
ENTRYPOINT [ "/helping_hands/nginx-entrypoint.sh" ]