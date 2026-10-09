FROM python:3.14-alpine

WORKDIR /code

COPY rules.yaml .

RUN pip install k8s-eval

CMD ["k8s-eval", "/code/rules.yaml"]
