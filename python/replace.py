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
        placeholder = f"{{{{{key}}}}}"  # e.g., {{name}}
        content = content.replace(placeholder, value)

    with open(output_path, 'w') as f:
        f.write(content)

    print(f"Replaced values written to: {output_path}")

if __name__ == "__main__":
    mapping = load_mapping("values.txt")
    replace_placeholders("template.yaml", mapping, "infrastructureDefinition.yaml")


