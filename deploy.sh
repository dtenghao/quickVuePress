#!/bin/bash

set -e

# 生成首页目录
python readHeader.py

# 为笔记开头加上title，使得博客更好的展示
python addTitle.py

# 生成静态文件
npm run-script docs:build

# 删除笔记的title，方便本地查看
python deleteTitle.py

# 进入生成的文件夹
cd docs/.vuepress/dist

git init
git add -A
git commit -m 'deploy'

### imporant 注意替换 如果发布到 https://<USERNAME>.github.io/<REPO>
git push -f git@github.com:0Eumenides/notebook.git master:gh-pages

cd -

