
import sys
import codecs

def apply_rot13_to_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    rot13_content = codecs.encode(content, 'rot_13')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(rot13_content)

if len(sys.argv) != 2:
    print("Usage: python rot13_file.py <filename>")
else:
    apply_rot13_to_file(sys.argv[1])
