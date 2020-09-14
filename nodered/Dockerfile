FROM keymetrics/pm2:latest-alpine
LABEL maintainer="Simplon"

WORKDIR /usr/src/app 

COPY . .

ENV NPM_CONFIG_LOGLEVEL warn
RUN npm install --save-dev

EXPOSE 1880

CMD [ "pm2-runtime", "start", "pm2.json" ]
