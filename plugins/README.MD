# Wukong-Robot 插件：Schedule Reminder

## 功能
通过语音设定日程提醒，支持以下表达：
- “10分钟后提醒我喝水”
- “下午3点提醒我开会”

## 安装方式
将 `schedule_reminder` 文件夹放入 `plugins/` 中，并重启 Wukong。

## 使用示例
“提醒我10分钟后打电话” → 十分钟后语音提醒。

## 技术点
- 使用 `apscheduler` 实现定时任务调度
- 用正则表达式解析时间表达
