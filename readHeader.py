import os

def is_hidden(item):
    return item.startswith('.')

def url_encode(string):
    return string.replace(' ', '%20')

def traverse_directory(path, base_url, depth=0):
    markdown_text = ''
    md_files = []
    has_directory = False
    for item in os.listdir(path):
        if is_hidden(item) or item.lower() == 'readme.md':
            continue

        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):
            has_directory = True
            markdown_text += '#' * (depth + 1) + ' ' + item + '\n'
            markdown_text += traverse_directory(item_path, base_url, depth + 1)
        else:
            filename, ext = os.path.splitext(item)
            if ext.lower() == '.md':
                relative_url = os.path.relpath(item_path, '.' + os.sep + 'docs')
                encoded_url = url_encode(relative_url.replace('\\', '/'))
                md_files.append((filename, base_url + encoded_url))

    for filename, url in md_files:
        if has_directory:
            markdown_text += '#' * (depth + 1) + ' [' + filename + '](' + url + ')\n'
        else:
            markdown_text += '- [' + filename + '](' + url + ')\n'

    return markdown_text

def main():
    markdown_filename = 'README.md'
    path = './docs'
    
    # 将你的github账户的用户名和仓库名填入
    base_url = 'https://用户名.github.io/仓库名/'

    markdown_text = traverse_directory(path, base_url)

    with open(os.path.join(path, markdown_filename), 'w') as md_file:
        md_file.write(markdown_text)

    print(f"Markdown file '{markdown_filename}' has been generated with the directory structure.")

if __name__ == '__main__':
    main()
