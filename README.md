# smt-product-landing-html

用单 html 创建 smthelp 产品 landing page。

每个页面都是**单文件、零构建**的独立 HTML —— 内联 CSS/JS，直接用浏览器打开即可，可直接作为附件发给客户。

## 页面索引

| 文件 | 主题 | 说明 |
|---|---|---|
| `tht-im-pcb-design-guideline-auto-insertion-dfm.html` | THT / IM PCB Design Guideline | 自动插件 DFM 设计指南。基于 Universal Instruments GS-354-02 Rev. D 与 GS-354-01，含板件包络、基准孔、孔径公式、孔跨距表、公差链、设备类别、故障推理、6 篇 Blog、10 支实测视频、下载区。支持 7 语言切换（EN / ES / PT / FR / AR / RU / ZH）+ 明暗主题，偏好本地持久化。内嵌 JSON-LD（Organization / TechArticle / FAQPage / ItemList / BreadcrumbList）与 hreflang。 |
| `ems-pcb-assembly-automation-tht-insertion-machines-feeders-turnkey-solutions.html` | EMS PCB Assembly Automation | THT 插件机、智能供料器、整线 turnkey 方案。 |

## 页面约定

- **单文件交付**：一个页面 = 一个 `.html`，无外部本地依赖；品牌资源走 `ph.smthelp.com` / `file.autoinsertion.com` 稳定 URL。
- **证据约束**：所有技术数值必须可追溯到公开源文件（机器手册 / 设计指南），页面内标注来源；查不到的标为「待确认」，不猜测。
- **多语言**：静态段用 `data-i18n` 属性，动态段由 JS 数组渲染；`localStorage` 保存语言与主题；阿拉伯语 `dir="rtl"`。
- **GEO/SEO**：英文正文预渲染进静态 HTML（不依赖 JS 执行即可被爬虫读取），配合 JSON-LD、canonical、OG/Twitter Card、hreflang。

## 联系

- 官网 www.smthelp.com · 邮箱 info@smthelp.com · WhatsApp +86 136 0256 2576
- 机器目录 https://file.autoinsertion.com · 机器图片 https://ph.smthelp.com
