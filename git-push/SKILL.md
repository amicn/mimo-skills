---
name: git-push
description: 将 D:\AI\skills 仓库变更推送到 GitHub (amicn/mimo-skills)。当用户提到"推送skill""上传skill""git push""提交skill""push skills"时使用。
location: file:///D:/AI/skills/git-push/SKILL.md
---

# Git Push Skill

将 `D:\AI\skills\` 仓库的变更提交并推送到 GitHub [amicn/mimo-skills](https://github.com/amicn/mimo-skills)。

## 环境配置

执行推送前确保以下环境变量已设置：

```powershell
$env:HTTPS_PROXY = "http://127.0.0.1:7890"
$env:GH_TOKEN = "<token>"      # GitHub PAT，权限: repo
```

Git 用户配置：
```powershell
git config user.name "AMICN"
git config user.email "2076624083@qq.com"
```

## 推送流程

### 1. 检查状态

```powershell
git -C D:\AI\skills status
git -C D:\AI\skills diff --stat
```

向用户列出变更，等待确认。

### 2. 暂存并提交

```powershell
git -C D:\AI\skills add -A
git -C D:\AI\skills commit -m "<变更说明>"
```

### 3. 推送到 GitHub

```powershell
$env:HTTPS_PROXY = "http://127.0.0.1:7890"
git -C D:\AI\skills push origin main
```

## GH_TOKEN 管理

Token 存储在 `D:\AI\skills\.token`（gitignore 已排除），需要时读取：

```powershell
$env:GH_TOKEN = Get-Content D:\AI\skills\.token -Raw
```

如果 `.token` 不存在或 token 过期，提示用户：
1. 访问 https://github.com/settings/tokens
2. 生成新 token，勾选 `repo` 权限
3. 将 token 写入 `D:\AI\skills\.token`

## 故障处理

| 问题 | 解决 |
|------|------|
| 连接超时 | 确保 Clash 代理运行: `127.0.0.1:7890` |
| 认证失败 | 检查 `.token` 是否有效，重新生成 PAT |
| 合并冲突 | 先 `git pull` 再重新提交 |
