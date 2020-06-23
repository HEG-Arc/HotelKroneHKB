FROM nginx:1.17-alpine
COPY ./compose/production/nginx/hkb.conf /etc/nginx/conf.d
COPY ./compose/production/nginx/matomo.conf /etc/nginx/conf.d
CMD ["nginx", "-g", "daemon off;"]
