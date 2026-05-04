# -*- coding: utf-8 -*-
"""
wxautox4 授权绕过补丁
在 pip install wxautox4 之后运行此脚本
"""
import wxautox4
import os

init_file = os.path.join(os.path.dirname(wxautox4.__file__), '__init__.py')

# 新内容
new_content = '''# -*- coding: utf-8 -*-
"""wxautox4 - patched"""
import sys
from .utils import useful as _useful_module
_useful_module.authenticate = lambda *a, **k: True
_useful_module.check_license = lambda *a, **k: True
_useful_module.authenticate_with_file = lambda *a, **k: True
_useful_module.authenticate_with_file2 = lambda *a, **k: True
_useful_module.offline_auth = lambda *a, **k: True
_useful_module.vces = lambda *a, **k: True
_useful_module.chlc = lambda *a, **k: True
sys.modules['wxautox4.utils.useful'] = _useful_module

from .wx import WeChat, Chat, LoginWnd
from .param import WxParam
authenticate = _useful_module.authenticate

from .ui import base
from . import exceptions, languages, logger, param, msgs, ui, uia, utils
import comtypes.stream, pythoncom, win32com.client, win32process, win32clipboard, psutil, uuid, tkinter
from typing import Union, List, Dict, Literal, Callable, TYPE_CHECKING
from concurrent.futures import ThreadPoolExecutor
from abc import ABC, abstractmethod
import threading, traceback, requests, tenacity, winreg, time
pythoncom.CoInitialize()

__all__ = ['WeChat', 'Chat', 'LoginWnd', 'WxParam', 'authenticate']
'''

# 备份原文件
backup = init_file + '.bak'
if not os.path.exists(backup):
    with open(init_file, 'r', encoding='utf-8') as f:
        original = f.read()
    with open(backup, 'w', encoding='utf-8') as f:
        f.write(original)
    print(f"已备份原文件: {backup}")

# 写入补丁
with open(init_file, 'w', encoding='utf-8') as f:
    f.write(new_content)
print(f"补丁已应用: {init_file}")
print("完成!")
