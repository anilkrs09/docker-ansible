Welcome to {{app_name}}, running in {{env}} mode.
The URL is: {{url}}.

  
app_name: HarnessApp
env: production
url: https://prod.example.com



def load_mapping(mapping_file):
    mapping = {}
    with open(mapping_file, 'r') as file:
        for line in file:
            if ':' in line:
                key, value = line.strip().split(':', 1)
                mapping[key.strip()] = value.strip()
    return mapping

def replace_placeholders(source_file, mapping, output_file):
    with open(source_file, 'r') as file:
        content = file.read()

    for key, value in mapping.items():
        placeholder = f"{{{{{key}}}}}"  # Matches {{key}}
        content = content.replace(placeholder, value)

    with open(output_file, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    mapping = load_mapping("mapping.txt")
    replace_placeholders("source.txt", mapping, "output.txt")
    print("Replacements completed. Output written to output.txt.")

