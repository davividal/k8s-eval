# Kubernetes Pod Evaluation Service

## Instalation

Clone this repo and run `pip install -e .` or install it directly via pip: `pip install git+https://github.com/davividal/k8s-eval`.

After that, pip will install k8s-eval executable into your path.

## Usage

### Rule file

This application expects a YAML file similar to this:

```yaml
rules:
- name: image_prefix
  description: "ensure the pod only uses images prefixed with `bitnami/`"
  output: boolean
- name: team_label_present
  description: "ensure the pod contains a label `team` with some value"
  output: boolean
- name: recent_start_time
  description: "ensure the pod has not been running for more than 7 days according to it's `startTime`"
  output: boolean
```

The application evaluates these rules for all pods in the cluster and outputs the results on stdout in json log format, one line per pod. Example:

```json
{"pod": "mytest", "rule_evaluation": [{"name": "image_prefix", "valid": true}, {"name": "team_label_present", "valid": true}, {"name": "recent_start_time", "valid": false}]}
{"pod": "another", "rule_evaluation": [{"name": "image_prefix", "valid": false}, {"name": "team_label_present", "valid": true}, {"name": "recent_start_time", "valid": false}]}
```

### Running

Simply run `k8s-eval` and it will use a `rules.yaml` in the current directory. If no such file exists, you can pass the path to the executable: `k8s-eval ~/Documents/k8s-eval/rules.yaml`

In doubt, `k8s-eval -h` has a short usage info.

## Useful Links

- [Kubernetes Python Client](https://github.com/kubernetes-client/python)
