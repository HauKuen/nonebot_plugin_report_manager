from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message


report = on_keyword({"反馈开发者"}, priority=50)

@report.handle()
async def report_handle(bot: Bot, event: Event):
    for id in bot.config.superusers:
        await bot.send_private_msg(user_id = int(id), message=Message(f"用户{event.get_user_id()}反馈：{event.get_message()}"))
    await report.finish("已反馈，感谢您的支持！")