#!/bin/bash

set -e

# 生成首页目录
python readHeader.py

# 为笔记开头加上title
python addTitle.py

# 生成静态文件
npm run-script docs:build

# 进入生成的文件夹
cd docs/.vuepress/dist

git init
git add -A
git commit -m 'deploy'

# 注意替换为自己的仓库地址
git push -f git@github.com:/<用户名>//<仓库名>.git master:gh-pages

cd -

