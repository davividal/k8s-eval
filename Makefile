.PHONY: docker

docker:
	docker build . -t k8s-eval -t localhost:5000/k8s-eval
