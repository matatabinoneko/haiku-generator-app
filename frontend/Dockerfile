FROM node:14.15.0

RUN mkdir /app
WORKDIR /app

COPY ./app/package.json /app/package.json
# ENV API_URL http://localhost:5000
RUN yarn install