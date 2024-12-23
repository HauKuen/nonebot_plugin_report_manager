from pathlib import Path
from typing import Literal
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot import get_driver
from nonebot import require
from dataclasses import dataclass, field
from typing import List

require("nonebot_plugin_localstore")

import nonebot_plugin_localstore as store

try:
    import ujson as json
except ModuleNotFoundError:
    import json

superusers = get_driver().config.superusers
plugin_data_dir: Path = store.get_plugin_data_dir()
file_path = plugin_data_dir / 'blacklist.json'

@dataclass
class Blacklist:
    users: List[str] = field(default_factory=list)

blacklist = Blacklist()

def load_blacklist() -> None:
    if file_path.is_file():
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            blacklist.users = data.get("blacklist", []) 
    else:
        blacklist.users = [] 

def save_blacklist() -> None:
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump({"blacklist": blacklist.users}, f, ensure_ascii=False) 

def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

def add_to_blacklist(uids: set) -> None:
    for uid in uids:
        if uid not in superusers and uid not in blacklist.users:
            blacklist.users.append(uid)
    save_blacklist()

def remove_from_blacklist(uids: set) -> None:
    global blacklist
    blacklist.users = [uid for uid in blacklist.users if uid not in uids]
    save_blacklist()

def handle_blacklist(event: MessageEvent, mode: Literal["add", "del"]) -> str:
    msg = str(event.get_message()).strip().split(' ')
    uids = {uid.strip() for uid in msg if is_number(uid.strip())}  # 使用集合推导式去重

    # debug
    # print(f"处理黑名单，模式: {mode}, 用户 ID: {uids}")

    if mode == "add":
        add_to_blacklist(uids)
        _mode = "添加"
    elif mode == "del":
        remove_from_blacklist(uids)
        _mode = "删除"

    if len(uids) == 0:
        return "没有可操作的用户，请检查输入格式或者用户是否已在黑名单中"
    else:
        return f"已{_mode} {len(uids)} 个黑名单用户: {', '.join(uids)}"