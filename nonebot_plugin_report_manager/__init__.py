from nonebot.adapters.onebot.v11 import Bot, Event, MessageEvent, GroupMessageEvent
from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.message import event_preprocessor
from nonebot import get_driver, logger
from nonebot.exception import IgnoredException
from typing import Set, List
from .blacklist import blacklist, handle_blacklist, load_blacklist

driver = get_driver()
superusers: Set[str] = driver.config.superusers

# 在插件加载时读取黑名单
load_blacklist()

# 获取自定义指令配置
try:
    feedback_users: List[str] = driver.config.feedback_users
    feedback_users = set(feedback_users)
except AttributeError:
    feedback_users = superusers

# 获取自定义命令配置
config = driver.config
REPORT_COMMAND = getattr(config, "report_command", "反馈开发者")
ADD_BLACKLIST_COMMAND = getattr(config, "add_blacklist_command", "拉黑")
DEL_BLACKLIST_COMMAND = getattr(config, "del_blacklist_command", "解除拉黑")
CHECK_BLACKLIST_COMMAND = getattr(config, "check_blacklist_command", "查看黑名单")

report = on_command(REPORT_COMMAND, priority=50)


@report.handle()
async def report_handle(bot: Bot, event: Event):
    msg = str(event.get_message()).split(REPORT_COMMAND, 1)[1].strip()
    if msg == "":
        await report.finish("反馈内容不能为空！")

    # 构建反馈消息
    feedback_msg = (
        f"来自群【{(await bot.get_group_info(group_id=event.group_id))['group_name']}】的用户 {event.get_user_id()} 反馈：{msg}"
        if isinstance(event, GroupMessageEvent)
        else f"用户 {event.get_user_id()} 反馈：{msg}"
    )

    # 发送给配置的反馈接收者
    for user_id in feedback_users:
        await bot.send_private_msg(user_id=int(user_id), message=feedback_msg)

    await report.finish("已反馈，感谢您的支持！")


add_blacklist = on_command(ADD_BLACKLIST_COMMAND, permission=SUPERUSER)


@add_blacklist.handle()
async def add_black_list(event: MessageEvent):
    msg = handle_blacklist(event, "add")
    await add_blacklist.send(msg)


del_blacklist = on_command(DEL_BLACKLIST_COMMAND, permission=SUPERUSER)


@del_blacklist.handle()
async def del_black_list(event: MessageEvent):
    msg = handle_blacklist(event, "del")
    await del_blacklist.send(msg)


check_blacklist = on_command(CHECK_BLACKLIST_COMMAND, permission=SUPERUSER)


@check_blacklist.handle()
async def check_black_list():
    if len(blacklist.users) == 0:
        await check_blacklist.finish("当前无黑名单用户")
    await check_blacklist.send(f"当前黑名单用户: {', '.join(blacklist.users)}")


@event_preprocessor
def blacklist_processor(event: MessageEvent):
    uid = str(event.user_id)
    if uid in superusers:
        return
    if uid in blacklist.users:
        logger.debug(f"用户 {uid} 在黑名单中, 忽略本次消息")
        raise IgnoredException("黑名单用户")
