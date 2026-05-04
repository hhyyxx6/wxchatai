# WeChat AI ChatBot v3.9.1

基于 wxautox4 + DeepSeek 的微信自动回复机器人，支持私聊和群聊。

## 功能特性

- **自动回复**：对接 DeepSeek API，根据预设人设进行智能对话
- **图片识别**：对接 Moonshot AI 识别聊天中的图片和表情包内容
- **多用户支持**：不同聊天对象可配置不同的 Prompt 人设
- **群聊支持**：支持 @机器人回复 或接收全部群消息
- **情绪识别**：根据回复内容自动发送对应的表情包
- **主动消息**：用户长时间未回复时主动发起对话
- **记忆管理**：自动总结对话并保存到 Prompt，实现长期记忆
- **WebUI 配置**：网页端启动/停止 Bot、修改配置、编辑 Prompt

## 环境要求

- Windows 系统
- Python 3.8+
- 电脑微信客户端（登录并保持后台运行）

## 快速开始

1. 申请 API Key：
   - DeepSeek API：https://api.deepseek.com
   - Moonshot API（图片识别）：https://platform.moonshot.cn
2. 登录电脑微信
3. 双击 `Run.bat` 启动，自动安装依赖并打开配置页面
4. 在网页中填入 API Key，配置你要聊天的对象
5. 点击 **Start Bot** 启动

## 用户配置

编辑 `config.py`，主要配置项：

| 配置项 | 说明 |
|--------|------|
| `LISTEN_LIST` | 监听列表，格式：`[['微信昵称', 'Prompt文件名']]` |
| `DEEPSEEK_API_KEY` | DeepSeek API 密钥 |
| `DEEPSEEK_BASE_URL` | API 地址 |
| `MODEL` | 模型名称 |
| `MOONSHOT_API_KEY` | Moonshot API 密钥（图片识别） |
| `TEMPERATURE` | 回复随机性 (0.0-1.0) |
| `MAX_TOKEN` | 回复最大长度 |
| `ENABLE_MEMORY` | 是否启用记忆功能 |
| `ENABLE_AUTO_MESSAGE` | 是否启用主动消息 |

## Prompt 管理

在 `prompts/` 目录下创建 `{昵称}.md` 文件作为人设提示词，格式参考 `提示词1.md`。

## 自定义表情包

将表情包（.gif/.png/.jpg）放入 `emojis/` 对应情绪文件夹：
- `happy/` - 开心
- `sad/` - 难过
- `angry/` - 生气
- `neutral/` - 中性

## 声明

本项目基于 [KouriChat](https://github.com/KouriChat/KouriChat) 修改，遵循 **GNU GPL-3.0** 许可证。原项目版权归属 umaru (2025)。
