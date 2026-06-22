---
name: dev-sandbox
description: |
  通用开发环境沙箱。为新项目或现有项目快速搭建隔离的开发和测试环境，
  覆盖 Python/Node/Go/Rust/Docker 等主流技术栈。
  当用户提到「搭建环境」「创建沙箱」「环境隔离」「dev sandbox」
  「setup env」「开发环境」「重建环境」「临时沙箱」时使用。
  即使用户只是说「帮我初始化这个项目」「环境有问题帮我修一下」
  「想快速试个东西」也应触发。
---

# 开发环境沙箱 · Dev Sandbox

> 「环境问题是最常见的时间黑洞。一个干净的隔离环境 = 随时可复现的起点。」

## 定位

**我能帮你的**：新项目初始化、环境诊断与修复、多环境配置隔离、临时沙箱快速实验、依赖锁定与版本管理

**我不能帮你的**：CI/CD 流水线配置、生产环境部署、云资源申请、团队环境治理策略（这些超出了本地开发沙箱的范围）

---

## 场景路由

收到问题后先判断类型：

| 用户问题 | 执行场景 | 核心目标 |
|---------|---------|---------|
| 新项目从零开始 / 初始化 | → 场景A | 选隔离方案 → 搭环境 → 锁定依赖 → 配置模板 → 验证 |
| 环境坏了 / 跑不起来 | → 场景B | 诊断 → 清理 → 重建 → 验证 |
| 多套环境切换 (dev/staging) | → 场景C | 抽离差异 → 设计配置方案 → 切换验证 |
| 快速试个东西，用完即弃 | → 场景D | 最小化启动 → 用完清理 |

---

## 场景A: 新项目初始化

### Step 1: 识别技术栈

检测项目目录中的标志文件：

| 标志文件 | 技术栈 |
|---------|--------|
| `requirements.txt` / `pyproject.toml` / `setup.py` / `Pipfile` | Python |
| `package.json` | Node.js |
| `go.mod` | Go |
| `Cargo.toml` | Rust |
| `Dockerfile` / `docker-compose.yml` | Docker |
| `pom.xml` / `build.gradle` | Java/Maven/Gradle |
| `Gemfile` | Ruby |
| `CMakeLists.txt` / `Makefile` | C/C++ |

**未检测到时**：主动询问用户「这个项目用什么语言/框架？」

### Step 2: 选择隔离方案

按优先级推荐：

| 优先级 | 方案 | 适用场景 | Windows 兼容 |
|--------|------|---------|-------------|
| 1 (首选) | 语言原生隔离 | 单语言项目 | ✅ |
| 2 | Docker / Podman | 多服务、需要系统级依赖 | ✅ (Docker Desktop) |
| 3 | conda | Python 项目，有系统级依赖 | ✅ |
| 4 | 全局安装 | 无其他选择时 | ✅ |

**默认推荐**：
- Python → `venv` (轻量，Python 内置)
- Node.js → `nvm` + `.nvmrc` (版本锁定)
- Go → Go modules (自带隔离，无需额外工具)
- Rust → `rustup` + Cargo (自带隔离)
- 多服务/数据库 → `docker-compose`

**禁止行为**：
- 不要在全局 pip/npm install（除非确认为一次性工具）
- 不要跳过环境变量模板创建
- 不要在 Windows 上推荐仅 Linux 可用的工具

### Step 3: 创建环境

#### Python 项目
```powershell
# Windows
python -m venv .venv
.venv\Scripts\Activate.ps1
# 或: .venv\Scripts\activate.bat (cmd)

# Linux/macOS
python3 -m venv .venv
source .venv/bin/activate
```

**检查点**：`which python` 指向 `.venv` 内

#### Node.js 项目
1. 先检测/安装 nvm (Windows: nvm-windows)
2. 创建 `.nvmrc` 写入 node 版本
3. `nvm use` 或 `nvm install`
4. `npm ci` (有 lock 文件) 或 `npm install`

**检查点**：`node --version` 匹配 `.nvmrc`

#### Docker 项目
```powershell
docker compose up -d
```

**检查点**：`docker compose ps` 所有服务 healthy

### Step 4: 锁定依赖

| 语言 | 锁定文件 | 生成命令 |
|------|---------|---------|
| Python | `requirements.txt` | `pip freeze > requirements.txt` |
| Python (现代) | `pyproject.toml` + `uv.lock` | `uv lock` |
| Node.js | `package-lock.json` | `npm install` 自动生成 |
| Go | `go.sum` | `go mod tidy` |
| Rust | `Cargo.lock` | `cargo build` 自动生成 |

### Step 5: 配置环境变量模板

创建一个**不会包含真实密钥**的模板文件：

```bash
# .env.example — 提交到 git
DATABASE_URL=postgres://localhost:5432/db
API_KEY=your_api_key_here
DEBUG=true
```

同时确保 `.env` 已加入 `.gitignore`。

**检查点**：
- [ ] `.env.example` 存在，含所有必需变量及注释
- [ ] `.env` 在 `.gitignore` 中
- [ ] `.env` 不存在（或已复制为 `.env.example`）

### Step 6: 验证环境

至少执行一次：

| 技术栈 | 验证命令 |
|--------|---------|
| Python | `python -c "import main_module; print('OK')"` |
| Node.js | `node -e "require('./index')"` 或 `npm start` |
| Go | `go build ./...` 或 `go run .` |
| Rust | `cargo build` 或 `cargo run` |
| Docker | `docker compose up -d` + `docker compose ps` |

环境不可用时执行**场景B**。

---

## 场景B: 现有项目环境修复

### Step 1: 诊断

按顺序排查：

1. **隔离环境存在吗？**
   - Python: `.venv/` 目录存在？
   - Node: `node_modules/` 存在？`nvm` 当前版本匹配 `.nvmrc`？
   - Docker: `docker compose ps` 输出？

2. **依赖完整吗？**
   - Python: `pip check`
   - Node: `npm ls --depth=0` 检查是否有 UNMET DEPENDENCY
   - Go: `go mod verify`

3. **环境变量加载了吗？**
   - 检查 `.env` 文件是否存在且包含所需变量

4. **端口冲突？**
   - Windows: `netstat -ano | findstr :PORT`
   - Linux/Mac: `lsof -i :PORT`

### Step 2: 修复

- 缺失隔离环境 → 回场景A Step 3
- 依赖损坏 → 删除并重建：
  ```powershell
  # Python
  Remove-Item -Recurse -Force .venv
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  pip install -r requirements.txt
  
  # Node
  Remove-Item -Recurse -Force node_modules
  npm ci
  ```
- 环境变量缺失 → 从 `.env.example` 创建 `.env`
- 端口冲突 → 杀进程或换端口

---

## 场景C: 多环境配置隔离

### Step 1: 识别需要区分的配置

常见需要多环境区分的变量：
- 数据库连接串
- API 密钥（dev key vs prod key）
- Debug 开关
- 日志级别
- 外部服务 URL

### Step 2: 设计配置方案

推荐方案（按简洁度排序）：

**方案1: .env.{environment} 文件** (推荐)
```
.env.example    ← 提交（模板，无真实密钥）
.env.dev        ← 本地开发
.env.staging    ← 预发布
.env.prod       ← 生产（不提交）
```

**方案2: 单一 .env + 覆盖变量**
```
ENVIRONMENT=dev
DATABASE_URL=postgres://localhost:5432/dev_db
```

**方案3: direnv** (Linux/Mac only)
```
.envrc  ← 按目录自动切换
```

### Step 3: 创建切换脚本

在 `package.json` 或 `Makefile` 中添加快捷方式：
```json
{
  "scripts": {
    "dev": "ENVIRONMENT=dev npm start",
    "staging": "ENVIRONMENT=staging npm start"
  }
}
```

Windows 可用 `cross-env` 包：
```json
{
  "scripts": {
    "dev": "cross-env ENVIRONMENT=dev npm start"
  }
}
```

---

## 场景D: 临时沙箱

用于快速实验，用完即弃。

### Step 1: 最小化启动

**Docker 方式（推荐）**：
```powershell
# 带自动清理的临时容器
docker run --rm -it -v "${PWD}:/workspace" -w /workspace python:3.12 bash
```

**语言原生方式**：
```powershell
# Python 临时 venv
python -m venv /tmp/sandbox-$(Get-Random)
# 用完后: Remove-Item -Recurse -Force /tmp/sandbox-*

# Node.js: 直接 npx 不需要安装
npx create-react-app my-test-app
Remove-Item -Recurse -Force my-test-app
```

### Step 2: 清理

临时沙箱必须在完成后清理：
- Docker: `docker rm -f <container>` / `docker compose down -v`
- venv: 删除 `.venv` 目录
- 测试目录: `Remove-Item -Recurse -Force <dir>`

---

## 技术栈快速参考

### Python 隔离选项

| 工具 | 隔离级别 | 速度 | Windows | 推荐场景 |
|------|---------|------|---------|---------|
| `venv` | 解释器隔离 | 快 | ✅ | 纯 Python 项目 |
| `virtualenv` | 解释器隔离 | 快 | ✅ | 需要老版本兼容 |
| `conda` | 系统级隔离 | 较慢 | ✅ | 需要 C 扩展/系统库 |
| `uv` | 解释器隔离 | 极快 | ✅ | 追求速度 |
| Docker | 全系统隔离 | — | ✅ | 多服务/部署一致性 |

### Node.js 版本管理

| 工具 | Windows | 推荐 |
|-------|---------|------|
| `nvm-windows` | ✅ | 首选 |
| `fnm` | ✅ | 更快，跨平台 |
| `volta` | ✅ | 项目级自动切换 |
| `n` | ❌ | 仅 Linux/Mac |

### Go

Go modules 自带隔离，无需额外工具。`GOPATH` 已不是必需品。**不要**建议用户设置 `GOPATH`。

### Rust

`rustup` + Cargo 自带隔离，`Cargo.toml` 管理依赖。**不要**建议用户手动管理 Rust 工具链。

---

## 平台适配

### Windows (PowerShell)

- 虚拟环境激活：`.venv\Scripts\Activate.ps1`
- 环境变量设置：`$env:VAR = "value"`（临时）/ `[System.Environment]::SetEnvironmentVariable()`（永久）
- 换行符：CRLF，但 `.sh` 脚本建议 LF
- 路径分隔符：`\`，但工具链通常接受 `/`
- 不能用：`n` (Node 版本管理)、`direnv`、`make` (无 WSL 时)

### Linux / macOS (Bash/Zsh)

- 虚拟环境激活：`source .venv/bin/activate`
- 环境变量：`export VAR=value`（临时）/ 写入 `~/.bashrc` 或 `~/.zshrc`（永久）
- 换行符：LF
- 路径分隔符：`/`

### 跨平台注意事项
- 脚本优先选用跨平台工具或同时提供两套指令
- 路径操作使用 `pathlib`（Python）或 `path`（Node）而非字符串拼接
- `.gitattributes` 设置 `* text=auto`

---

## 验证清单

环境搭建完成后，逐项确认：

- [ ] 隔离环境已创建（.venv / node_modules / docker compose up 成功）
- [ ] 依赖版本已锁定（lock 文件存在）
- [ ] `.env.example` 存在，含所有必需变量
- [ ] `.env` 在 `.gitignore` 中
- [ ] `.env` 不存在或仅本地存在
- [ ] 项目可正常启动/运行
- [ ] 无端口冲突
- [ ] 无硬编码的绝对路径（检查配置文件中的路径）

---

## 失败处理

| 症状 | 可能原因 | 处理 |
|------|---------|------|
| `pip install` 失败 | 缺少 C 编译器 | Windows: 安装 Visual C++ Build Tools；或换 conda |
| `npm install` 失败 | node-sass/python2 依赖 | 建议升级到 dart-sass，或 `npm rebuild` |
| Docker 启动失败 | Docker Desktop 未运行 | 提示启动 Docker Desktop |
| 端口被占用 | 另一个实例在运行 | `netstat -ano \| findstr :PORT` 找 PID，`taskkill` 杀进程 |
| `nvm` 不识别 | nvm-windows 未安装 | 提供 nvm-windows 安装链接 |
| 权限被拒 (Windows) | 未以管理员运行 | PowerShell 右键「以管理员身份运行」 |

---

## 禁止行为

- ❌ 跳过环境变量模板创建
- ❌ 在全局环境安装项目依赖
- ❌ 硬编码绝对路径
- ❌ 推荐仅 Linux 可用的工具给 Windows 用户
- ❌ 在 `.env.example` 中放真实密钥
- ❌ 创建一个连自己都不确定能否运行的命令
- ❌ 环境搭建完成后不运行验证
