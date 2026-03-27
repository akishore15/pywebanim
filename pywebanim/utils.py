import os

def save_html(content, output_path):
    with open(output_path, "w") as f:
        f.write(content)

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)
