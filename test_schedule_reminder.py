from schedule_reminder import Plugin
from datetime import datetime, timedelta

def test_parse_minutes_later():
    plugin = Plugin()
    time_str, content = plugin.parse_query("10分钟后提醒我喝水")
    assert '分钟后' in time_str
    assert content == "喝水"

def test_parse_afternoon_time():
    plugin = Plugin()
    time_str, content = plugin.parse_query("下午3点提醒我开会")
    remind_time = plugin.parse_time(time_str)
    assert remind_time.hour == 15
    assert content == "开会"
