# MiMo Skills

MiMo Code 的全局 skill 集合，遵循 [Anthropic Skills](https://github.com/anthropics/skills) 的 SKILL.md 格式。

## 结构

```
skills/
  <skill-name>/
    SKILL.md     ← 必需：YAML 前言 + Markdown 指令
    <scripts>/   ← 可选：辅助脚本
```

---

## 工具

| Skill | 说明 |
|-------|------|
| `vision` | 视觉分析（豆包/Qwen/OpenAI），截图、UI检查、OCR |
| `dev-sandbox` | 开发环境沙箱，快速搭建隔离的测试环境 |

## 办公文档

| Skill | 说明 |
|-------|------|
| `docx` | Word 文档创建、编辑、提取、格式转换 |
| `pdf` | PDF 读取、合并、拆分、OCR、表单填充 |
| `pptx` | PPT 创建、编辑、提取内容 |
| `xlsx` | Excel 表格读写、公式、图表、数据清洗 |
| `doc-coauthoring` | 结构化文档协同撰写工作流 |

## 思维视角

| Skill | 人物 |
|-------|------|
| `andrej-karpathy-perspective` | Andrej Karpathy — AI工程现实主义 |
| `elon-musk-perspective` | 马斯克 — 第一性原理、白痴指数 |
| `feynman-perspective` | 费曼 — 反自欺、货物崇拜检测 |
| `ilya-sutskever-perspective` | Ilya Sutskever — AI安全、研究品味 |
| `mrbeast-perspective` | MrBeast — 内容创作、病毒传播 |
| `munger-perspective` | 芒格 — 逆向思考、认知偏误 |
| `naval-perspective` | Naval — 杠杆、特定知识、财富 |
| `paul-graham-perspective` | Paul Graham — 创业、写作、产品 |
| `steve-jobs-perspective` | 乔布斯 — 产品直觉、极简 |
| `sun-yuchen-perspective` | 孙宇晨 — 注意力经济、叙事操控 |
| `taleb-perspective` | 塔勒布 — 黑天鹅、反脆弱 |
| `trump-perspective` | 特朗普 — 谈判、权力、传播 |
| `x-mastery-mentor` | X/Twitter 运营导师 |
| `zhang-yiming-perspective` | 张一鸣 — 产品、组织、全球化 |
| `zhangxuefeng-perspective` | 张雪峰 — 教育选择、职业规划 |
