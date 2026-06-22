# MiMo Skills

MiMo Code 的全局 skill 集合，遵循 [Anthropic Skills](https://github.com/anthropics/skills) 的 SKILL.md 格式。

## 结构

```
skills/
  <skill-name>/
    SKILL.md     ← 必需：YAML 前言 + Markdown 指令
    <scripts>/   ← 可选：辅助脚本
```

## 已有 Skill

| Skill | 说明 |
|-------|------|
| `vision` | 视觉分析（豆包/Qwen/OpenAI），用于截图、UI检查 |
| `dev-sandbox` | 开发环境沙箱，快速搭建隔离环境 |
