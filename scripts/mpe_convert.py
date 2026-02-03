import re
import os

def convert_to_mpe(file_path):
    print(f"Reading {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    in_block = False

    for line in lines:
        # Check for callout header: > [!question] Title
        # Note: Obsidian sometimes puts the title on the same line
        header_match = re.match(r'^>\s*\[!question\]\s*(.*)', line)
        
        if header_match:
            title = header_match.group(1).strip()
            # Construct MPE admonition header
            if title:
                new_lines.append(f'!!! question "{title}"\n')
            else:
                new_lines.append('!!! question\n')
            in_block = True
            continue
        
        if in_block:
            # Check for blockquote lines
            # Case 1: "> " followed by text
            if line.startswith('> '):
                content = line[2:] 
                new_lines.append(f'    {content}')
            # Case 2: ">" only (empty blockquote line)
            elif line.strip() == '>':
                new_lines.append('    \n')
            else:
                # Line does not start with quote, block ends
                in_block = False
                new_lines.append(line)
        else:
            new_lines.append(line)

    print("Writing converted content...")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Done.")

if __name__ == '__main__':
    file_path = r'c:\Users\calculus\Desktop\MathNotes\Understanding Analysis 习题草稿.md'
    if os.path.exists(file_path):
        convert_to_mpe(file_path)
    else:
        print(f"File not found: {file_path}")
