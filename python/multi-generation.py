import os
import re

def load_mapping(*file_paths):
    mapping = {}
    for file_path in file_paths:
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
        pattern = r"\{\{\s*" + re.escape(key) + r"\s*\}\}"
        content, _ = re.subn(pattern, value, content)

    with open(output_path, 'w') as f:
        f.write(content)
    print(f"✅ Output written: {output_path}")

def generate_configs(template_files, common_file, env_files, output_dir="outputs"):
    os.makedirs(output_dir, exist_ok=True)

    for env_file in env_files:
        env_name = os.path.splitext(os.path.basename(env_file))[0]
        mapping = load_mapping(common_file, env_file)

        for template_file in template_files:
            template_base = os.path.splitext(os.path.basename(template_file))[0]
            output_file = os.path.join(output_dir, f"{env_name}_{template_base}.yaml")
            replace_placeholders(template_file, mapping, output_file)

if __name__ == "__main__":
    # Set paths
    template_files = [
        "templates/infra.yaml",
        "templates/deployment.yaml"
    ]
    common_file = "values/common.txt"
    env_files = [
        "values/dev.txt",
        "values/qa.txt",
        "values/prod.txt"
    ]

    generate_configs(template_files, common_file, env_files)

values/
├── common.txt
├── dev.txt
├── qa.txt

templates/
├── infra.yaml
├── deployment.yaml

outputs/
├── dev_infra.yaml
├── dev_deployment.yaml
├── qa_infra.yaml
├── qa_deployment.yaml

