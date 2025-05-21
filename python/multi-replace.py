values1.txt + template1.yaml → outputs/values1_template1.yaml

values2.txt + template2.yaml → outputs/values2_template2.yaml


import re
import os

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
        # Match {{ key }} or {{key}}
        pattern = r"\{\{\s*" + re.escape(key) + r"\s*\}\}"
        content, count = re.subn(pattern, value, content)
        print(f"[{os.path.basename(template_path)}] Replaced {count} occurrence(s) of '{{{{{key}}}}}' with '{value}'")

    with open(output_path, 'w') as f:
        f.write(content)
    print(f"✅ Output written to: {output_path}\n")

def process_multiple_files(value_files, template_files, output_dir="outputs"):
    os.makedirs(output_dir, exist_ok=True)

    for val_file in value_files:
        mapping = load_mapping(val_file)
        base_name = os.path.splitext(os.path.basename(val_file))[0]

        for template_file in template_files:
            template_base = os.path.splitext(os.path.basename(template_file))[0]
            output_name = f"{base_name}_{template_base}.yaml"
            output_path = os.path.join(output_dir, output_name)

            replace_placeholders(template_file, mapping, output_path)

if __name__ == "__main__":
    # List your input files here
    value_files = ["values1.txt", "values2.txt"]
    template_files = ["template1.yaml", "template2.yaml"]

    process_multiple_files(value_files, template_files)
