#!/bin/bash

set -e

# 初始化项目
git init
npm init
 
# 安装本地依赖项
npm install

# 将默认的临时目录和缓存目录添加到 .gitignore 文件中
echo 'node_modules' >> .gitignore
echo '.temp' >> .gitignore
echo '.cache' >> .gitignore

