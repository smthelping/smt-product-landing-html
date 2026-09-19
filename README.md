# smt-product-landing-html

用单 HTML 创建 smthelp 产品 landing page 的仓库。

每个页面都是**单文件、零构建**的独立 HTML —— 内联 CSS/JS，直接用浏览器打开即可，也可直接作为附件发给客户。

公开访问入口（GitHub Pages）：**https://smthelping.github.io/smt-product-landing-html/**

---

## 目录结构

页面按**实际内容**归类到产品线目录，不再是根目录平铺：

| 目录 | 主题 | 页面数 |
|---|---|---|
| `tht-auto-insertion/` | THT 自动插件（轴向 / 径向 / 异形 / 端子，单机到整线） | 30 |
| `feeders-nozzles/` | 供料器与吸嘴（编带 / 管装 / 托盘 / 皮带 / 振动盘 / 端子飞达 / 定制吸嘴夹爪） | 42 |
| `smt-line-placement/` | SMT 产线与贴装（印刷机、回流焊、激光打标、点胶、编带飞达变体） | 6 |
| `board-handling/` | 上下板、输送与分板（分板机、铣刀机、周转车） | 12 |
| `wave-selective-soldering/` | 波峰焊与选择焊（选择焊机、桌面焊锡机器人、焊接自动化） | 7 |
| `cleaning-coating/` | 清洗、涂覆与工艺（钢网 / PCBA / 吸嘴 / 治具清洗，等离子、灌胶、UV 固化） | 13 |
| `inspection-rework/` | 检测与返修（AOI、X-Ray、点料机、BGA 返修台） | 6 |
| `storage-esd/` | 智能仓储与防静电（智能料架、钢网柜、ESD 闸机） | 16 |
| `materials-consumables/` | 物料与耗材（接料带、载带、擦拭纸、剪脚成型、编带机） | 11 |
| `fixtures-carriers/` | 治具与载具（波峰焊托盘、钛爪、印刷与回流治具） | 4 |
| `case-studies/` | 案例研究（含实测节拍、元件数与产线布局） | 7 |
| `marketing/` | 营销素材（冷邮件模板、表单触发器、买方一页纸） | 24 |

- `index.html` —— 全站导航首页，按上述分类列出全部 178 个页面。
- `*-assets/images/` —— 被页面直接引用的本地实拍图（仅同步被引用的文件，其余素材留在原工作区）。

---

## 外部资源接入

三类外部资源已逐条校验并**按机型匹配**嵌入对应页面：

### 1. 图片 —— `ph.smthelp.com`

- 统一使用真实存在的路径格式 `https://ph.smthelp.com/images/YYYY/MM/DD/<file>`。
- 历史遗留的 `images/YYYY-MM-DD/`（连字符日期）写法**全部修正为斜杠日期**，共修正 182 处。
- 页内引用的全部图床图片（约 300 个唯一 URL）逐条 HTTP 校验，失效项按文件名关键词在图床资源中匹配替换，共替换 76 处，替换目标全部为 `200`。

### 2. 视频 —— YouTube 视频看板

看板：<https://file.autoinsertion.com/public/Southern-Machinery-YouTube-Video-Board.html>

- 按页面机型/主题在看板条目中匹配，注入统一结构的「Watch it running」区块（响应式 16:9 嵌入，`youtube-nocookie`，`loading="lazy"`）。
- 本次共为 37 个原本没有视频的页面补入视频；嵌入的 53 个视频 ID 全部通过 YouTube oEmbed 校验（0 个失效）。

### 3. 产品资料 —— 产品 Catalog 看板

看板：<https://file.autoinsertion.com/public/Southern-Machinery-Product-Catalog-Board.html>

- 按机型匹配 catalog / 手册 / ROI 表，注入「Product documentation」下载区。
- 使用的 48 个下载链接逐条 `HTTP 200` 校验通过。

> 统一区块带 `id="smth-matched-resources"`，便于后续重新生成或移除。

---

## 页面约定

- **单文件交付**：一个页面 = 一个 `.html`，无外部本地依赖（仅被引用的实拍图放在 `*-assets/`）；品牌资源走 `ph.smthelp.com` / `file.autoinsertion.com` 稳定 URL。
- **证据约束**：所有技术数值必须可追溯到公开源文件（机器手册 / 设计指南），页面内标注来源；查不到的标为「待确认」，不猜测。
- **客户资料转公开页必须匿名化**：客户名、联系人、地址、单号、金额、报价条款一律不得出现。
- **多语言**：静态段用 `data-i18n` 属性，动态段由 JS 数组渲染；`localStorage` 保存语言与主题；阿拉伯语 `dir="rtl"`。
- **GEO/SEO**：英文正文预渲染进静态 HTML（不依赖 JS 执行即可被爬虫读取），配合 JSON-LD、canonical、OG/Twitter Card、hreflang。

## 本次整理说明

- 文件名统一 slug 化（小写 + 连字符），去掉原始命名中的空格、全角符号与不可见字符。
- 页面内相对链接（原有 61 处）已按新目录结构重写为正确的相对路径；全部 570 余处本地相对引用已逐条校验存在。
- 仓库中**已有且已清理过**的页面以仓库版本为准（工作区副本含编辑器注入的 `data-page-node-id` 属性，仓库版本已剥离），避免回退。
- 工作区中 74 GB 的构建中间产物（`*-build/`、`venv/`、`node_modules/`、嵌套 `.git`、导出图源）不进入本仓库：它们不是交付物，且页面不引用。
- `smt-customized-feeder-nozzle-solution.html` 原文件混入了生成过程的提示词与推理文本、并在一处 `<div class="w-14 h-1` 处被截断。本次已切除泄出文本、补全截断结构、补齐页脚与客服脚本。

## 联系

- 官网 www.smthelp.com · 邮箱 info@smthelp.com · WhatsApp +86 136 0256 2576
- 机器目录 https://file.autoinsertion.com · 机器图片 https://ph.smthelp.com
