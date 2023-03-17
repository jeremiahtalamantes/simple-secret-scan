import os
import re
from pathlib import Path

def search_secrets(directory):
    secret_patterns = [
        re.compile(r'((?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?)'),
        re.compile(r'([A-Za-z0-9]{32})'),
        re.compile(r'([A-Za-z0-9]{40})'),
        re.compile(r'([A-Za-z0-9-_]{64})'),
    ]

    def is_potential_secret(string):
        for pattern in secret_patterns:
            if pattern.match(string):
                return True
        return False

    for root, _, files in os.walk(directory):
        for file in files:
            #
            # Modify file extensions for any other files you want to include
            #
            if file.endswith((".py", ".js", ".json", ".yml", ".yaml", ".xml", ".ini", ".properties", ".txt")):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    try:
                        lines = f.readlines()
                        for line_number, line in enumerate(lines, 1):
                            for word in line.split():
                                if is_potential_secret(word):
                                    print(f"Potential secret found in {file_path} at line {line_number}: {word}")
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python search_secrets.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        sys.exit(1)

    search_secrets(directory)