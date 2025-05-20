pipeline.name: Build_and_Deploy
pipeline.identifier: build_and_deploy
stages.0.name: Build Stage
stages.0.type: CI
stages.0.spec.steps.0.name: Build App
stages.0.spec.steps.0.type: Run
stages.0.spec.steps.0.spec.command: make build
stages.1.name: Deploy Stage
stages.1.type: CD
stages.1.spec.steps.0.name: Deploy to Prod
stages.1.spec.steps.0.type: K8sDeploy
stages.1.spec.steps.0.spec.manifest: prod.yaml


import yaml
from collections import defaultdict

def nested_set(dic, keys, value):
    for key in keys[:-1]:
        # If it's a digit, it's a list index
        if key.isdigit():
            key = int(key)
            if not isinstance(dic, list):
                dic_list = []
                dic.update(dic_list)
                dic = dic_list
            while len(dic) <= key:
                dic.append({})
            dic = dic[key]
        else:
            dic = dic.setdefault(key, {})
    last_key = keys[-1]
    if last_key.isdigit():
        last_key = int(last_key)
    dic[last_key] = value

def parse_input_file(file_path):
    data = {}
    with open(file_path, 'r') as file:
        for line in file:
            if not line.strip(): continue
            key, value = line.strip().split(":", 1)
            key_parts = [k.strip() for k in key.strip().split(".")]
            nested_set(data, key_parts, value.strip())
    return data

def write_yaml(data, output_file):
    with open(output_file, 'w') as file:
        yaml.dump(data, file, sort_keys=False, default_flow_style=False)

if __name__ == "__main__":
    input_path = "input.txt"
    output_path = "harness_pipeline.yaml"

    parsed_data = parse_input_file(input_path)
    write_yaml(parsed_data, output_path)
    print(f"Harness pipeline YAML written to: {output_path}")



Output
pipeline:
  name: Build_and_Deploy
  identifier: build_and_deploy
  stages:
    - name: Build Stage
      type: CI
      spec:
        steps:
          - name: Build App
            type: Run
            spec:
              command: make build
    - name: Deploy Stage
      type: CD
      spec:
        steps:
          - name: Deploy to Prod
            type: K8sDeploy
            spec:
              manifest: prod.yaml

