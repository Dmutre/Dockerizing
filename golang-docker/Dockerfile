FROM golang:1.22-alpine AS build

WORKDIR /project

COPY go.mod go.sum ./

RUN go mod download

COPY . .

RUN go build -o build/fizzbuzz

FROM gcr.io/distroless/static-debian11

WORKDIR /project

COPY --from=build /project/templates templates

COPY --from=build /project/build/fizzbuzz fizzbuzz

CMD ["./fizzbuzz", "serve"]