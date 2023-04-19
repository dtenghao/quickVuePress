import { defineUserConfig, defaultTheme } from 'vuepress'


export default defineUserConfig({
  // 仓库名称
  base: '/notebook/',
  // markdown显示几级标题
  markdown: {
    headers: {
      level: [1, 2, 3, 4],
    }
  },
  lang: 'zh-CN',
  title: '记录',
  description: '个人博客',

  theme: defaultTheme({


    sidebarDepth: 4
  }),
})


