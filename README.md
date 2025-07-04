# 🍅 番茄小说下载器 v1.7.0

<div align="center">

[![Release](https://img.shields.io/github/v/release/POf-L/Fanqie-novel-Downloader?style=for-the-badge&logo=github)](https://github.com/POf-L/Fanqie-novel-Downloader/releases)
![Python 3.8+](https://img.shields.io/badge/Python-3.8+-3776ab?style=for-the-badge&logo=python&logoColor=white)
![License MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Platform Windows|macOS|Linux](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=for-the-badge)
![Status Active](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

</div>

> **番茄小说下载器** 是一款简单易用的小说下载工具，提供现代化GUI界面和命令行模式，支持批量下载、Tor代理、Cloudflare反代、多线程及多种输出格式，让你轻松下载并阅读网络小说。

---

## 📑 目录

- [🌟 功能特点](#功能特点)
- [🚀 快速开始](#快速开始)
- [📖 使用指南](#使用指南)
- [⚙️ 配置说明](#配置说明)
- [🤝 贡献指南](#贡献指南)
- [📄 License](#license)

---

## 🌟 功能特点

### 🎯 核心功能
- 🖥️ **现代化GUI界面** - 基于CustomTkinter的美观界面，支持响应式布局
- 🌐 **智能API管理** - 自动从服务器获取最新API列表，确保下载稳定性
- ⚡ **批量下载模式** - 大量章节时自动启用批量下载，显著提升效率
- 📖 **多种输出格式** - 支持 TXT 和 EPUB 格式输出
- 📊 **实时进度显示** - 详细的下载状态、进度条和章节计数

### 🚀 高级功能
- 🔒 **Tor网络支持** - 内置Tor代理，保护隐私和绕过网络限制
- 🌍 **Cloudflare Workers反代** - 支持自定义反向代理，解决API访问问题
- ⚡ **多线程下载** - 智能并发控制，最大化下载速度
- 🔄 **断点续传** - 支持暂停和恢复下载，避免重复下载
- 🎨 **响应式界面** - 自适应不同屏幕尺寸，完美适配各种设备

### 🛠️ 技术特性
- 🔄 **智能重试机制** - 多API轮询，自动错误处理和重试
- 📝 **详细日志系统** - 完整的操作记录和错误信息
- 🔧 **模块化架构** - 清晰的代码结构，易于扩展和维护
- 🔐 **加密支持** - 内置AES加密功能，保护数据安全

---

## 🚀 快速开始

### 📋 系统要求

| 项目 | 要求 |
|------|------|
| **Python版本** | 3.8+ |
| **操作系统** | Windows 10+, macOS 10.14+, Linux |
| **内存** | 至少 512MB 可用内存 |
| **网络** | 稳定的互联网连接 |
| **存储空间** | 根据下载内容而定 |

### ⚙️ 安装步骤

#### 1️⃣ 获取源码
```bash
git clone https://github.com/POf-L/Fanqie-novel-Downloader.git
cd Fanqie-novel-Downloader
```

#### 2️⃣ 安装依赖
```bash
# 安装所有依赖包
pip install -r requirements.txt

# 或者使用国内镜像加速
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

> 💡 **提示**: tkinter是Python标准库，无需单独安装。如遇到问题，请确保Python安装时包含了tkinter组件。

#### 3️⃣ 启动程序

**🖥️ GUI版本 (推荐)**
```bash
python main.py
```

**⌨️ 命令行版本**
```bash
python cli.py
```

---

## 📖 使用指南

### 🖥️ GUI界面使用

1. **🚀 启动程序**
   ```bash
   python main.py
   ```

2. **📝 输入小说信息**
   - 在输入框中输入番茄小说的ID或书名
   - 支持直接粘贴小说链接

3. **📁 选择保存路径**
   - 点击"浏览"按钮选择保存位置
   - 程序会记住上次选择的路径

4. **📄 选择输出格式**
   - **TXT格式**: 纯文本文件，兼容性好
   - **EPUB格式**: 电子书格式，支持阅读器

5. **⚡ 开始下载**
   - 点击"开始下载"按钮
   - 程序自动获取API列表并开始下载
   - 实时显示下载进度和状态

### ⌨️ 命令行使用

```bash
python cli.py
```

按照提示操作：
- 选择是否启用Tor代理
- 输入小说ID
- 指定保存路径
- 自动开始下载

---

## ⚙️ 配置说明

### 📁 配置文件位置

程序会自动在标准用户数据目录中创建 `user_config.json` 配置文件：

| 操作系统 | 配置文件路径 |
|----------|-------------|
| **Windows** | `%LOCALAPPDATA%\User\TomatoNovelDownloader\user_config.json` |
| **macOS** | `~/Library/Application Support/TomatoNovelDownloader/user_config.json` |
| **Linux** | `~/.config/TomatoNovelDownloader/user_config.json` |

### 🔧 配置参数详解

#### 网络请求配置
```json
{
    "request": {
        "max_workers": 50,          // 最大并发线程数
        "max_retries": 3,           // 最大重试次数
        "timeout": 10,              // 请求超时时间(秒)
        "request_rate_limit": 0.05  // 请求间隔(秒)
    }
}
```

#### 文件输出配置
```json
{
    "file": {
        "default_save_path": "downloads",  // 默认保存路径
        "last_save_path": ""              // 上次使用的路径
    }
}
```

#### Tor网络配置
```json
{
    "tor": {
        "enabled": false,        // 是否启用Tor
        "proxy_port": 9050,      // Tor代理端口
        "change_ip_after": 980,  // 多少次请求后更换IP
        "request_timeout": 35    // Tor请求超时时间
    }
}
```

#### Cloudflare Workers反代配置
```json
{
    "cloudflare_proxy": {
        "enabled": false,              // 是否启用反代
        "proxy_domain": "",            // 反代域名
        "fallback_to_original": true,  // 失败时回退到原始API
        "test_endpoint": "/test"       // 测试端点
    }
}
```

#### 界面外观配置
```json
{
    "appearance": {
        "appearance_mode": "dark",  // 界面主题: dark/light
        "color_theme": "blue"       // 颜色主题
    },
    "window": {
        "default_geometry": "1300x850",  // 默认窗口大小
        "position": null                 // 窗口位置
    }
}
```

---

## 🔧 高级功能

### 🌍 Cloudflare Workers反代部署

项目包含完整的Cloudflare Workers反代脚本，用于解决API访问问题：

1. **部署步骤**：
   - 登录 [Cloudflare Dashboard](https://dash.cloudflare.com/)
   - 进入 Workers & Pages
   - 创建新的 Worker
   - 复制 `scripts/cloudflare-worker-proxy.js` 内容到编辑器
   - 部署并获取 Worker 域名

2. **配置使用**：
   - 在下载器中启用反代功能
   - 输入 Worker 域名
   - 程序会自动使用反代进行请求

### 🔒 Tor网络支持

内置Tor网络支持，提供额外的隐私保护：

1. **安装Tor**：
   - Windows: 下载 [Tor Browser](https://www.torproject.org/)
   - Linux: `sudo apt install tor`
   - macOS: `brew install tor`

2. **启用Tor**：
   - 在GUI中勾选"启用Tor代理"
   - 或在命令行版本中选择启用
   - 程序会自动检测Tor连接状态

### 📦 打包发布

项目包含完整的PyInstaller配置文件：

```bash
# 打包GUI版本（无控制台）
pyinstaller build_gui.spec

# 打包控制台版本（带调试信息）
pyinstaller build_console.spec
```

---

## 🤝 贡献指南

我们欢迎所有形式的贡献！

### 🐛 报告问题
- 使用 [Issues](https://github.com/POf-L/Fanqie-novel-Downloader/issues) 报告bug
- 提供详细的错误信息和复现步骤
- 包含系统环境和Python版本信息

### 💡 功能建议
- 在Issues中提出新功能建议
- 详细描述功能需求和使用场景
- 欢迎提供设计思路和实现方案

### 🔧 代码贡献
1. Fork 本项目
2. 创建功能分支: `git checkout -b feature/AmazingFeature`
3. 提交更改: `git commit -m 'Add some AmazingFeature'`
4. 推送分支: `git push origin feature/AmazingFeature`
5. 创建 Pull Request

### 📝 文档改进
- 改进README文档
- 添加代码注释
- 完善使用说明

---

## 📄 许可证

本项目采用 **MIT** 许可证。详见 `LICENSE` 文件。

---

## ⚠️ 免责声明

本工具仅用于技术学习和研究目的。使用者应承担使用本工具的所有风险和责任，作者不承担任何法律责任。

---

## 🙏 致谢

- 感谢 [Dlmily/Tomato-Novel-Downloader-Lite](https://github.com/Dlmily/Tomato-Novel-Downloader-Lite) 提供的参考代码
- 感谢所有贡献者的支持和建议
- 感谢开源社区提供的优秀库和工具

---

<div align="center">

**⭐ 如果这个项目对您有帮助，请给个Star支持一下！ ⭐**

[![Star History Chart](https://api.star-history.com/svg?repos=POf-L/Fanqie-novel-Downloader&type=Date)](https://star-history.com/#POf-L/Fanqie-novel-Downloader&Date)

</div>
