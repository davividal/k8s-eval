from kubernetes import client, config

import json


def get_all_pods():
    config.load_kube_config()

    v1 = client.CoreV1Api()

    return v1.list_pod_for_all_namespaces(watch=False).items

def check(rules, pods):
    results = []

    for pod in pods:
        results.append({
            'pod': pod.metadata.name,
            'rule_evaluation': [rule.evaluate(pod) for rule in rules]
        })

    return results

def check_all(rules):
    return check(rules, get_all_pods())
