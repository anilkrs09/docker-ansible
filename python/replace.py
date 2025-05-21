Welcome to {{app_name}}, running in {{env}} mode.
name: k8s-prod
identifier: k8s_prod
orgIdentifier: default
projectIdentifier: my_project
environmentRef: prod
deploymentType: Kubernetes
type: KubernetesDirect
connectorRef: my_k8s_connector
namespace: prod-namespace
releaseName: release-prod

infrastructureDefinition:
  name: {{name}}
  identifier: {{identifier}}
  orgIdentifier: {{orgIdentifier}}
  projectIdentifier: {{projectIdentifier}}
  environmentRef: {{environmentRef}}
  deploymentType: {{deploymentType}}
  type: {{type}}
  spec:
    connectorRef: {{connectorRef}}
    namespace: {{namespace}}
    releaseName: {{releaseName}}


import re

def load_mapping(file_path):
    mapping = {}
    with open(file_path, 'r') as f:
        for line in f:
            if ':' in line:
                key, value = line.strip().split(':', 1)
                mapping[key.strip()] = value.strip()
    return mapping

def replace_placeholders(template_path, mapping, output_path):
    with open(template_path, 'r') as f:
        content = f.read()

    for key, value in mapping.items():
        # Match patterns like {{key}} or {{ key }}
        pattern = r"\{\{\s*" + re.escape(key) + r"\s*\}\}"
        content, count = re.subn(pattern, value, content)
        print(f"Replaced {count} occurrence(s) of '{{{{{key}}}}}' with '{value}'")

    with open(output_path, 'w') as f:
        f.write(content)

    print(f"All replacements written to: {output_path}")

if __name__ == "__main__":
    mapping = load_mapping("values.txt")
    replace_placeholders("template.yaml", mapping, "infrastructureDefinition.yaml")



