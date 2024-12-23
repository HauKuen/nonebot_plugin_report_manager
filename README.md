<div align="center">

# nonebot_plugin_report_manager
_✨ Nonebot2反馈插件 ✨_
</div>

<p align="center">

  <a href="https://github.com/KafCoppelia/nonebot_plugin_roll/blob/beta/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-informational">
  </a>

  <a href="https://github.com/nonebot/nonebot2">
    <img src="https://img.shields.io/badge/nonebot2-2.0.0b3+-green">
  </a>

<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</p>

## 📖 介绍

一个接受群友反馈的Nonebot2反馈插件。


## 💿 安装

<details>
<summary>使用 nb-cli 安装</summary>

    nb plugin install nonebot-plugin-report-manager

</details>

<details>
<summary>使用包管理器安装</summary>

    pip install nonebot-plugin-report-manager
</details>


## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置
注意接收信息的账号必须是机器人的好友

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| feedback_users | 否 | 无 | 指定反馈账号，如不填写则必须配置superusers |

**反馈功能**
```
反馈开发者 + 内容
```
例如，`反馈开发者 在使用xxx功能时...`

**黑名单功能**
```
拉黑/解除拉黑 QQ1 QQ2 QQ3... 
查看黑名单
```


## 😊TODO

- [ ] 合并用户反馈
- [ ] 自定义反馈指令
- [x] 黑名单


## 🙏鸣谢

黑名单功能灵感来源于[nonebot-plugin-namelist](https://github.com/A-kirami/nonebot-plugin-namelist)
