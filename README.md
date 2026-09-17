# smt-product-landing-html

用单 html 创建 smthelp 产品 landing page。

每个页面都是**单文件、零构建**的独立 HTML —— 内联 CSS/JS，直接用浏览器打开即可，可直接作为附件发给客户。

## 页面索引

| 文件 | 主题 | 说明 |
|---|---|---|
| `tht-im-pcb-design-guideline-auto-insertion-dfm.html` | THT / IM PCB Design Guideline | 自动插件 DFM 设计指南。基于 Universal Instruments GS-354-02 Rev. D 与 GS-354-01，含板件包络、基准孔、孔径公式、孔跨距表、公差链、设备类别、故障推理、6 篇 Blog、10 支实测视频、下载区。支持 7 语言切换（EN / ES / PT / FR / AR / RU / ZH）+ 明暗主题，偏好本地持久化。内嵌 JSON-LD（Organization / TechArticle / FAQPage / ItemList / BreadcrumbList）与 hreflang。 |
| `s380a-vision-pcb-separator-machine-v-cut-curve-depaneling.html` | S380A Vision Curved & V-cut PCB Separator | 全视觉曲线 / V-CUT 分板机。基于 **S380A 规格书 + 2023 版操作手册**（两份原始 PDF），含 18 项规格表、手册补充参数表、**两份文件矛盾清单**（长度 1180 vs 1230 mm、工作面积 350×550 vs L350×W330、自动换刀归属 Q380A 等待确认项）、6 类轮廓切割能力、6 步视觉编程流程、进给式回本计算器（唯一硬编码值为已公布 5–100 mm/s 进给范围）、保养周期表、10 条故障→首查序列、8 支 YouTube 视频、**8 篇 Dan Koe 六步法长文**（标题不含 hook/diagnosis/framework/vehicle/loop/CTA）、Chatwoot 智能客服。支持 7 语言 + 明暗主题，偏好本地持久化。内嵌 JSON-LD（Organization / Product / FAQPage / BreadcrumbList，FAQ 与可见内容同源）与 hreflang。 |
| `ems-pcb-assembly-automation-tht-insertion-machines-feeders-turnkey-solutions.html` | EMS PCB Assembly Automation | THT 插件机、智能供料器、整线 turnkey 方案。 |
| `sf320at-inline-auto-selective-lead-cutter-measured-result.html` | SF320AT Inline Auto Selective Lead Cutter | 在线自动选择性剪脚机实测结果页。基于客户 demo 报告（**已匿名化**）的三组卡尺读数，含剪脚长度计算器（读者可就地复算减少率）、公差链、14 项规格表、刀头 CAD 剖视图、5 项售后支持、6 组 FAQ、10 支实测视频、下载区。支持 7 语言（EN / ES / PT / FR / AR / RU / ZH）+ 明暗主题。数据分三级标注：`已验证数据` / `概念示意` / `待确认`；机型归属按 SF320AT **标注**，下单前需复核。 |

## 页面约定

- **单文件交付**：一个页面 = 一个 `.html`，无外部本地依赖；品牌资源走 `ph.smthelp.com` / `file.autoinsertion.com` 稳定 URL。
- **证据约束**：所有技术数值必须可追溯到公开源文件（机器手册 / 设计指南），页面内标注来源；查不到的标为「待确认」，不猜测。
- **客户资料转公开页必须匿名化**：客户名、联系人、地址、单号、金额、报价条款一律不得出现；页面需自行说明引用出处与不确定性（未点名客户 / 规格需复核）。
- **多语言**：静态段用 `data-i18n` 属性，动态段由 JS 数组渲染；`localStorage` 保存语言与主题；阿拉伯语 `dir="rtl"`。
- **GEO/SEO**：英文正文预渲染进静态 HTML（不依赖 JS 执行即可被爬虫读取），配合 JSON-LD、canonical、OG/Twitter Card、hreflang。

## 联系

- 官网 www.smthelp.com · 邮箱 info@smthelp.com · WhatsApp +86 136 0256 2576
- 机器目录 https://file.autoinsertion.com · 机器图片 https://ph.smthelp.com
