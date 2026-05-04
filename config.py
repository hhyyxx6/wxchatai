# -*- coding: utf-8 -*-

# ***********************************************************************
# Modified based on the KouriChat project
# Copyright of the original project: Copyright (C) 2025, umaru
# Copyright of this modification: Copyright (C) 2025, iwyxdxl
# Licensed under GNU GPL-3.0 or higher, see the LICENSE file for details.
# ***********************************************************************

# 用户列表(请配置要和bot说话的账号的微信昵称，不要写备注！)
# 例如：LISTEN_LIST = ['微信昵称1','用户2']
LISTEN_LIST = [['L.', '提示词1']]

# DeepSeek API 配置
DEEPSEEK_API_KEY = 'sk-your-deepseek-api-key'
# 硅基流动API注册地址，免费15元额度 https://cloud.siliconflow.cn/
DEEPSEEK_BASE_URL = 'https://api.deepseek.com'
# 硅基流动API的模型
MODEL = 'deepseek-chat'

# 如果要使用官方的API
# DEEPSEEK_BASE_URL = 'https://api.deepseek.com'
# 官方API的V3模型
# MODEL = 'deepseek-chat'

# 回复最大token
MAX_TOKEN = 200
# DeepSeek温度 (0.0-1.0, 越低越稳定)
TEMPERATURE = 0.7

# Moonshot AI配置（用于图片和表情包识别）
# API申请https://platform.moonshot.cn/
MOONSHOT_API_KEY = 'sk-your-moonshot-api-key'
MOONSHOT_BASE_URL = 'https://api.moonshot.cn/v1'
MOONSHOT_MODEL = 'moonshot-v1-128k-vision-preview'
MOONSHOT_TEMPERATURE = 0.9
ENABLE_IMAGE_RECOGNITION = True
ENABLE_EMOJI_RECOGNITION = True

# 消息队列等待时间（秒），等待这么久后才处理消息，防止用户连续发多条消息
QUEUE_WAITING_TIME = 5

# 表情包存放目录
EMOJI_DIR = 'emojis'
ENABLE_EMOJI_SENDING = True

# 自动消息配置
AUTO_MESSAGE = '请你模拟系统设置的角色，在微信上找对方发消息想知道对方在做什么'
ENABLE_AUTO_MESSAGE = True
# 等待时间
MIN_COUNTDOWN_HOURS = 1.0
MAX_COUNTDOWN_HOURS = 2.0
# 消息发送时间限制
QUIET_TIME_START = '22:00'
QUIET_TIME_END = '8:00'

# 消息回复时间间隔
# 间隔时间 = 字数 * (平均时间 + 随机时间)
AVERAGE_TYPING_SPEED = 0.3
RANDOM_TYPING_SPEED_MIN = 0.1
RANDOM_TYPING_SPEED_MAX = 0.6

# 记忆功能
# 采用综合评分公式：0.6*重要度 - 0.4*(存在时间小时数)
# 示例：
# 重要度5的旧记忆（存在12小时）得分：0.65 - 0.412 = 3 - 4.8 = -1.8
# 重要度4的新记忆（存在1小时）得分：0.64 - 0.41 = 2.4 - 0.4 = 2.0 → 保留新记忆
ENABLE_MEMORY = True
MEMORY_TEMP_DIR = 'Memory_Temp'
MAX_MESSAGE_LOG_ENTRIES = 15
MAX_MEMORY_NUMBER = 5000

# 是否接收全部群聊消息
Accept_All_Group_Chat_Messages = False
