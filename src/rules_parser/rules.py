import datetime
import pytz
import yaml


def parse_rules_file(rules_path):
    rule_list = []
    with open(rules_path) as f:
        doc = ''.join(f.readlines())
    yaml_rules = yaml.full_load(doc)['rules']
    for r in yaml_rules:
        rule_list.append(factory(r))
    return rule_list

def factory(r):
    import importlib
    cls_name = ''.join([t.title() for t in r['name'].split('_')]) + 'Rule'
    module = importlib.import_module('src.rules_parser.rules')
    return getattr(module, cls_name)(r)


class Rule(object):
    name = None
    description = None
    output = None
    valid = None

    def __init__(self, rule: dict):
        self.name = rule['name']
        self.description = rule['description']
        self.output = rule['output']
        self.valid = None

    def evaluate(self, pod):
        return {
            'name': self.name,
            'valid': self._evaluate(pod)
        }

    def _evaluate(self, pod):
        raise NotImplementedError


class ImagePrefixRule(Rule):
    image_prefix = None

    def __init__(self, rule: dict):
        super().__init__(rule)
        self.image_prefix = self.description.split('`')[1]

    def _evaluate(self, pod):
        return all([c.image.find(self.image_prefix) >= 0 for c in pod.status.container_statuses])


# TODO: Make this rule generic
class TeamLabelPresentRule(Rule):
    def _evaluate(self, pod):
        return 'team' in pod.metadata.labels


class RecentStartTimeRule(Rule):
    def _evaluate(self, pod):
        week_ago = datetime.datetime.now() - datetime.timedelta(days=7)

        return pod.status.start_time > pytz.UTC.localize(week_ago)
