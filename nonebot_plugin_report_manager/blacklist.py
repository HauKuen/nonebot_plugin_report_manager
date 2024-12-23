from pathlib import Path
from typing import Literal
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot import get_driver
from nonebot import require
from dataclasses import dataclass, field
from typing import List
import json

require("nonebot_plugin_localstore")

import nonebot_plugin_localstore as store


superusers = get_driver().config.superusers
plugin_data_dir: Path = store.get_plugin_data_dir()
file_path = plugin_data_dir / "blacklist.json"


@dataclass
class Blacklist:
    users: List[str] = field(default_factory=list)


blacklist = Blacklist()


def load_blacklist() -> None:
    if file_path.is_file():
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            blacklist.users = data.get("blacklist", [])
    else:
        blacklist.users = []


def save_blacklist() -> None:
    with open(file_path, "w", encoding="utf-8") as f:
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
        if uid not in blacklist.users:
            blacklist.users.append(uid)
    save_blacklist()


def remove_from_blacklist(uids: set) -> None:
    global blacklist
    blacklist.users = [uid for uid in blacklist.users if uid not in uids]
    save_blacklist()


def handle_blacklist(event: MessageEvent, mode: Literal["add", "del"]) -> str:
    msg = str(event.get_message()).strip().split(" ")
    uids = {uid.strip() for uid in msg if is_number(uid.strip())}  # 使用集合推导式去重

    valid_uids = {uid for uid in uids if uid not in superusers}
    skipped_uids = uids - valid_uids

    # 其实该加上 feedback_users 无法被拉黑，但是感觉没人会这么做，懒得写了

    if mode == "add":
        already_blacklisted = {uid for uid in valid_uids if uid in blacklist.users}
        valid_uids = valid_uids - already_blacklisted
        add_to_blacklist(valid_uids)
        _mode = "添加"
    elif mode == "del":
        remove_from_blacklist(valid_uids)
        _mode = "删除"

    if len(valid_uids) == 0:
        if len(skipped_uids) > 0 and len(already_blacklisted) > 0:
            return f"操作失败：{'、'.join(skipped_uids)} 是超级用户，{'、'.join(already_blacklisted)} 已在黑名单中"
        elif len(skipped_uids) > 0:
            return f"操作失败：{'、'.join(skipped_uids)} 是超级用户，无法拉黑"
        elif len(already_blacklisted) > 0:
            return f"操作失败：{'、'.join(already_blacklisted)} 已在黑名单中"
        return "没有可操作的用户，请检查输入格式或者用户是否已在黑名单中"
    else:
        result = f"已{_mode} {len(valid_uids)} 个黑名单用户: {', '.join(valid_uids)}"
        if skipped_uids:
            result += f"\n注意：{'、'.join(skipped_uids)} 是超级用户，已自动跳过"
        if mode == "add" and already_blacklisted:
            result += (
                f"\n注意：{'、'.join(already_blacklisted)} 已在黑名单中，已自动跳过"
            )
        return result
