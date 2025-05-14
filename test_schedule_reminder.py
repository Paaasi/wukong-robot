from schedule_reminder import Plugin
from datetime import datetime, timedelta

def test_parse_minutes_later():
    plugin = Plugin()
    time_str, content = plugin.parse_query("Remind me to drink water in 10 minutes")
    assert 'minutes' in time_str
    assert content == "drink water"

def test_parse_afternoon_time():
    plugin = Plugin()
    time_str, content = plugin.parse_query("Remind me to have a meeting at 3pm")
    remind_time = plugin.parse_time(time_str)
    assert remind_time.hour == 15
    assert content == "have a meeting"
