FROM python:3.12-alpine

WORKDIR /code

COPY rules.yaml .

RUN pip install k8s-eval

CMD ["k8s-eval", "/code/rules.yaml"]
