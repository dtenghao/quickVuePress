import os

def is_hidden(item):
    return item.startswith('.')

def remove_front_matter(path, front_matter):
    for item in os.listdir(path):
        if is_hidden(item):
            continue

        item_path = os.path.join(path, item)
    
        if os.path.isdir(item_path):
            remove_front_matter(item_path, front_matter)
        else:
            filename, ext = os.path.splitext(item)
            if ext.lower() == '.md':
                with open(item_path, 'r', encoding='utf-8') as md_file:
                    content = md_file.read()
                
                if content.startswith(front_matter):
                    content = content.replace(front_matter, '', 1).lstrip()
                    with open(item_path, 'w', encoding='utf-8') as md_file:
                        md_file.write(content)
                    print(f"Front matter has been removed from '{item_path}'")

def main():
    path = './docs'
    front_matter = '---\ntitle: 目录\n---'

    remove_front_matter(path, front_matter)
    
    print("Front matter has been removed from all Markdown files with it.")

if __name__ == '__main__':
    main()
