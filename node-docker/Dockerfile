FROM node:20-alpine3.18 as builder

WORKDIR /app

RUN npm install -g pnpm

COPY package*.json ./

COPY pnpm-lock.yaml ./

RUN pnpm install

COPY . .

RUN pnpm run build

FROM node:20-alpine3.18

WORKDIR /app

COPY --from=builder /app/dist /app/dist

COPY --from=builder /app/node_modules /app/node_modules

COPY .env /app

EXPOSE 5000

CMD ["dist/main"]