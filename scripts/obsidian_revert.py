import re
import os

def revert_to_obsidian(file_path):
    print(f"Reading {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    in_block = False
    in_style = False

    for line in lines:
        # 1. Remove style block (start)
        if line.strip() == '<style>':
            in_style = True
            continue
        
        # 1. Remove style block (end)
        if line.strip() == '</style>':
            in_style = False
            continue
            
        if in_style:
            # Skip lines inside style block
            continue
            
        # 2. Detect start of Admonition block
        # Pattern: !!! type "Title" or !!! type
        header_match = re.match(r'^!!!\s+(\w+)(?:\s+"(.*?)")?\s*$', line.strip())
        
        if header_match:
            admonition_type = header_match.group(1)
            title = header_match.group(2)
            
            # Obsidian uses > [!type] Title
            if title:
                new_lines.append(f'> [!{admonition_type}] {title}\n')
            else:
                new_lines.append(f'> [!{admonition_type}]\n')
            in_block = True
            continue
        
        # 3. Process content inside block
        if in_block:
            # Check for 4-space indentation which is standard for Admonition blocks
            if line.startswith('    '):
                content = line[4:] # Strip only the first 4 spaces
                new_lines.append(f'> {content}')
            # Check for exactly 4 spaces (empty indented line) or just newline
            elif line == '    \n':
                 new_lines.append('>\n')
            # If line is completely empty (no spaces), it technically ends the block in standard Markdown.
            # However, sometimes users have blank lines inside.
            # Assuming strictly indented blocks:
            elif line.strip() == '':
                 in_block = False
                 new_lines.append(line)
            else:
                # Non-indented text ends the block
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
        revert_to_obsidian(file_path)
    else:
        print(f"File not found: {file_path}")
