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


## ☀ ️指令
自定义指令前缀在``.env.*``中写入``COMMAND_START=["前缀"]``

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
- [ ] 限制反馈次数(~~感觉没啥必要~~)
- [x] 黑名单


## 🙏鸣谢

黑名单功能修改于[nonebot-plugin-namelist](https://github.com/A-kirami/nonebot-plugin-namelist)
