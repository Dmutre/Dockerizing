FROM node:20-alpine3.18

WORKDIR /app

RUN npm install -g pnpm

COPY package*.json ./

COPY pnpm-lock.yaml ./

RUN pnpm install

COPY . .

COPY .env ./

RUN pnpm run build

EXPOSE 5000

CMD ["pnpm", "run", "start:prod"]