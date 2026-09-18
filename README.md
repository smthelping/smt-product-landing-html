# smt-product-landing-html

用单 html 创建 smthelp 产品 landing page。

每个页面都是**单文件、零构建**的独立 HTML —— 内联 CSS/JS，直接用浏览器打开即可，可直接作为附件发给客户。

## 页面索引

| 文件 | 主题 | 说明 |
|---|---|---|
| `tht-im-pcb-design-guideline-auto-insertion-dfm.html` | THT / IM PCB Design Guideline | 自动插件 DFM 设计指南。基于 Universal Instruments GS-354-02 Rev. D 与 GS-354-01，含板件包络、基准孔、孔径公式、孔跨距表、公差链、设备类别、故障推理、6 篇 Blog、10 支实测视频、下载区。支持 7 语言切换（EN / ES / PT / FR / AR / RU / ZH）+ 明暗主题，偏好本地持久化。内嵌 JSON-LD（Organization / TechArticle / FAQPage / ItemList / BreadcrumbList）与 hreflang。 |
| `s380a-vision-pcb-separator-machine-v-cut-curve-depaneling.html` | S380A Vision Curved & V-cut PCB Separator | 全视觉曲线 / V-CUT 分板机。基于 **S380A 规格书 + 2023 版操作手册**（两份原始 PDF），含 18 项规格表、手册补充参数表、**两份文件矛盾清单**（长度 1180 vs 1230 mm、工作面积 350×550 vs L350×W330、自动换刀归属 Q380A 等待确认项）、6 类轮廓切割能力、6 步视觉编程流程、进给式回本计算器（唯一硬编码值为已公布 5–100 mm/s 进给范围）、保养周期表、10 条故障→首查序列、8 支 YouTube 视频、**8 篇 Dan Koe 六步法长文**（标题不含 hook/diagnosis/framework/vehicle/loop/CTA）、Chatwoot 智能客服。支持 7 语言 + 明暗主题，偏好本地持久化。内嵌 JSON-LD（Organization / Product / FAQPage / BreadcrumbList，FAQ 与可见内容同源）与 hreflang。SEO 标题与描述按 SERP 显示宽度预算收敛（标题 ≤60、描述 ≤160 宽度单位），7 种语言各自独立。 |
| `s7020t-terminal-insertion-machine-tht-odd-form-auto-insertion.html` | S7020T Terminal Insertion Machine | THT 异形端子插入机（轻触开关 / 条形连接器 / 铜嵌件 / 轴向编织元件）。基于 **S7020T 使用说明书（手册原文，13.6 MB，取自产品目录看板）** + S-7000T 解决方案说明 + S-7000 演示资料三份源文件，含 20 项手册规格表、**7 项三文件矛盾披露表**（外形尺寸 2160×1330×1530 vs 1700×1300×1600、重量 1500 vs 1200 kg、产能 6000 vs 8000 CPH、功率 1.6 vs 2.0 kVA、气压在一本手册内即有三种写法、型号 S7020T vs S-7000T）、6 步工艺、6 项配置决策、安装条件、日/月/年保养表（保留手册原文措辞）、8 条故障→首查序列、10 张实拍图、6 支看板校验视频、6 份可下载 PDF、**8 篇 Dan Koe 六步法长文**（标题不含 hook/diagnosis/framework/vehicle/loop/CTA）、6 条 FAQ、插入回本计算器（唯一硬编码机器值为已公布 0.6 s/点）、Chatwoot 智能客服。支持 7 语言 + 明暗主题，偏好本地持久化，阿拉伯语 RTL。内嵌 JSON-LD（Organization / Product / FAQPage / BreadcrumbList，FAQ 由可见标记生成，不会漂移）与 hreflang。SEO 标题与描述按 SERP 显示宽度预算收敛（标题 ≤60、描述 ≤160 宽度单位），7 种语言各自独立；已通过 129 项无头语义断言。 |
| `sme-6300-pcba-inline-cleaning-machine.html` | SME-6300 In-line PCBA Cleaning Machine | 在线 PCBA 清洗机。支持 7 语言 + 明暗主题、8 篇长文、Chatwoot 客服。（由另一会话提交，索引行待补充完整描述） |
| `ems-pcb-assembly-automation-tht-insertion-machines-feeders-turnkey-solutions.html` | EMS PCB Assembly Automation | THT 插件机、智能供料器、整线 turnkey 方案。 |
| `sf320at-inline-auto-selective-lead-cutter-measured-result.html` | SF320AT Inline Auto Selective Lead Cutter | 在线自动选择性剪脚机实测结果页。基于客户 demo 报告（**已匿名化**）的三组卡尺读数，含剪脚长度计算器（读者可就地复算减少率）、公差链、14 项规格表、刀头 CAD 剖视图、5 项售后支持、6 组 FAQ、10 支实测视频、下载区。支持 7 语言（EN / ES / PT / FR / AR / RU / ZH）+ 明暗主题。数据分三级标注：`已验证数据` / `概念示意` / `待确认`；机型归属按 SF320AT **标注**，下单前需复核。 |
| `s430ac-auto-lead-cutter-machine-tht-pcba-lead-trimming.html` | S-430AC Auto Lead Cutter | THT 自动剪脚机（台式 / 离线，与在线式 SF320AT 互补）。基于 **S-430AC 使用说明书 + 自动剪脚机 PPT + 剪脚机关键零件清单** 三份源文件，含 12 项规格表、I/O 映射表（4 剪 / 8 入 / 4 出）、X/Y/Z/R 四轴说明、9 行核心零部件品牌表（上银 HIWIN / 亚德客 AirTAC / 基恩士 KEYENCE / SICK / 雷赛 Leadshine / 三菱 Mitsubishi / 信捷 Xinje / 铭纬 MEAN WELL / 欧姆龙 OMRON / NSK / 日本利莱）、**7 行三文件矛盾与沉默披露表**、剪刀错边剪切 vs 挤压原理图、1 ms 剪切时序、4 项耗材与 4 项日常保养、产能回本计算器、8 篇 Dan Koe 六步法长文（标题不含 hook/diagnosis/framework/vehicle/loop/CTA）、10 条 FAQ、9 支看板校验视频、3 组共 15 份可下载 PDF、Chatwoot 智能客服。数据分三级标注：`已验证资料` / `概念示意` / `待确认`。支持 7 语言 + 明暗主题，偏好本地持久化，阿拉伯语 RTL；已通过 103 项无头语义断言。 |
| `s7000-odd-form-insertion-machine-tht-auto-pcb-assembly.html` | S7000 Odd Form Series Insertion Machine | THT 异形元件插件机系列（PIN / 铜嵌件 eyelet / 端子 / 轻触开关 / 异形元件）。基于 **九份具名文档**：用户提供的 6 份产品 PDF（S7020 系列 PIN & Eyelet 端子插件机、S7020 THT 异形元件说明、S7000 PIN 端子应力测试方案、S-7000P 演示资料、S-7000E 铜嵌件方案、S-7000D 轻触开关机）＋从产品目录看板补充的 3 份（**2024 版 S7000 平台手册**为权威源、S7900 送料器目录、OIM-2FS-W 四头压脚方案）。含 22 项平台规格表、**9 型号变体矩阵**（S7000 / S7020T·E·P·S·F / S-7000T·P·E·D / OIM-2FS-W）、**10 行四文件矛盾披露表**（外形尺寸 1995×1250×1530 vs 1700×1300×1600 vs 2160×1330×1530 vs 1450×1300×1600 mm、重量 1500 vs 1200 vs 1000 kg、产能 12000 vs 8000 vs 4000 CPH **跨 3 倍**、功率 1.6 vs 2.0 kVA、PCB 尺寸 5 个不同窗口、头数 2 / 1–3 / 1–4 / 4、气压 5–6 kgf/cm² 换算 ≈0.49–0.59 MPa 与 0.6–0.8 MPa **不重叠**、月维护成本 USD 500 vs RMB 2000 **币种不同不等价**、插入角度 360° vs 0–90°、型号四套命名家族）、6 步工艺流程、安装条件、调整点清单、**8 条故障→首查序列**（保留手册原文措辞）、12 张实拍图、12 支看板校验视频、12 份可下载 PDF、**8 篇 Dan Koe 六步法长文**（标题不含 hook/diagnosis/framework/vehicle/loop/CTA）、8 条 FAQ、插入回本计算器（唯一硬编码机器值为已公布秒/点，按元件类别 0.6 / 0.55 / 1 s，公式全由访客输入驱动）、Chatwoot 智能客服。支持 7 语言 + 明暗主题，偏好本地持久化，阿拉伯语 RTL。内嵌 JSON-LD（Organization / Product / FAQPage / BreadcrumbList，FAQ 由可见标记生成，不会漂移）与 hreflang。SEO 标题与描述按 SERP 显示宽度预算收敛（标题 ≤60、描述 ≤160 宽度单位），7 种语言各自独立（EN 50.3 / ES 40.5 / PT 53.5 / FR 45.2 / AR 50.0 / RU 56.7 / ZH 45.0）；已通过 135 项无头语义断言，0 失败 0 跳过。 |
| `bulk-capacitor-lead-cut-forming-machine-tht-assembly.html` | S-EPCOS Bulk Capacitor Lead Cut & Forming Machine | 散装电容切脚成型机（THT 自动插件前道成型）。基于 **S-EPCOS 技术协议**（.doc，按 UTF-16LE 解码提取规格表）+ **客户电容零件图纸**（成型要求标注为 STATE AS-ASSEMBLED TO PCB；**图纸号、第三方零件号与变更单已脱敏**，页面只保留「客户电容图纸」这一来源类别）+ 随询价提供的实测照片 + 营销素材索引 CSV + 客户 demo 视频。含 8 工位分度盘与 4 大部件（主机 / 振动料道 / 电箱 / 控制系统）结构说明、11 步已记录工艺流程、**3 行规格冲突披露表**（其中气压 5–7 MPa 与行业常识量级不符，标注为 `待确认`，不取平均、不二选一、不沉默）、零件成型尺寸（R1.3 弯曲半径 / R0.5 最大外圆角 / Ø18.5 mm 最大包络）、含降额的产能换算表、4 项可选项、安装条件、回本计算器（机器 1000 pcs/h vs 人工台 2 人 × 250 pcs/h，算术全部由访客输入驱动）、8 张实拍图、6 支看板校验视频、4 份可下载 PDF、**8 篇 Dan Koe 六步法长文**（标题不含 hook/diagnosis/framework/vehicle/loop/CTA）、8 条 FAQ、Chatwoot 智能客服。数据分三级标注：`已验证资料` / `概念示意` / `待确认`。支持 7 语言（EN / ES / PT / FR / AR / RU / ZH）+ 明暗主题，偏好本地持久化，阿拉伯语 RTL。内嵌 JSON-LD（Organization / Product / FAQPage / BreadcrumbList，FAQ 由可见标记生成，不会漂移）与 hreflang（含 x-default）。SEO 标题与描述按 SERP 显示宽度预算收敛（标题 ≤60、描述 ≤160 宽度单位），7 种语言各自独立（EN 48.0 / ES 45.0 / PT 44.5 / FR 42.5 / AR 38.4 / RU 41.1 / ZH 35.4）；已通过 122 项无头语义断言，0 失败 0 跳过。 |

## 页面约定

- **单文件交付**：一个页面 = 一个 `.html`，无外部本地依赖；品牌资源走 `ph.smthelp.com` / `file.autoinsertion.com` 稳定 URL。
- **证据约束**：所有技术数值必须可追溯到公开源文件（机器手册 / 设计指南），页面内标注来源；查不到的标为「待确认」，不猜测。
- **客户资料转公开页必须匿名化**：客户名、联系人、地址、单号、金额、报价条款一律不得出现；页面需自行说明引用出处与不确定性（未点名客户 / 规格需复核）。
- **多语言**：静态段用 `data-i18n` 属性，动态段由 JS 数组渲染；`localStorage` 保存语言与主题；阿拉伯语 `dir="rtl"`。
- **GEO/SEO**：英文正文预渲染进静态 HTML（不依赖 JS 执行即可被爬虫读取），配合 JSON-LD、canonical、OG/Twitter Card、hreflang。

## 联系

- 官网 www.smthelp.com · 邮箱 info@smthelp.com · WhatsApp +86 136 0256 2576
- 机器目录 https://file.autoinsertion.com · 机器图片 https://ph.smthelp.com
