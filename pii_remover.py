import re
import os
import argparse

def is_pii(text):
    # Add more patterns as needed
    patterns = [
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # Email
        r'\b(?:\+?1[-.]?)?(?:\(?[2-9][0-8][0-9]\)?[-.]?){2}[0-9]{4}\b',  # Phone number
        r'\b\d{3}-\d{2}-\d{4}\b',  # SSN
        r'\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})\b'  # Credit card
    ]
    return any(re.search(pattern, text) for pattern in patterns)

def obfuscate_pii(text):
    # This is a simple obfuscation. You might want to use more sophisticated methods.
    return re.sub(r'\S', '*', text)

def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified = False
    for i, line in enumerate(lines):
        if is_pii(line):
            lines[i] = obfuscate_pii(line)
            modified = True

    if modified:
        with open(file_path, 'w') as file:
            file.writelines(lines)
        print(f"PII removed from {file_path}")

def main():
    parser = argparse.ArgumentParser(description="Remove PII from files")
    parser.add_argument("path", help="Path to file or directory to process")
    args = parser.parse_args()

    if os.path.isfile(args.path):
        process_file(args.path)
    elif os.path.isdir(args.path):
        for root, dirs, files in os.walk(args.path):
            for file in files:
                process_file(os.path.join(root, file))
    else:
        print(f"Invalid path: {args.path}")

if __name__ == "__main__":
    main()
