from robot.sdk.AbstractPlugin import AbstractPlugin
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import re
import threading

scheduler = BackgroundScheduler()
scheduler.start()

class Plugin(AbstractPlugin):
    def __init__(self):
        super().__init__()
        self.lock = threading.Lock()

    def handle(self, query):
        time_info, content = self.parse_query(query)
        if time_info and content:
            remind_time = self.parse_time(time_info)
            if remind_time:
                with self.lock:
                    scheduler.add_job(self.say, 'date', run_date=remind_time, args=[f"提醒：{content}"])
                self.say(f"好的，将在 {remind_time.strftime('%H:%M')} 提醒您：{content}")
            else:
                self.say("抱歉，我没理解提醒时间。")
        else:
            self.say("请告诉我提醒的时间和内容，例如：10分钟后提醒我喝水。")

    def parse_query(self, query):
        match = re.search(r'(上午|下午)?(\d+)点(.*)', query) or re.search(r'(\d+)分钟后(.*)', query)
        if match:
            time_str = match.group(0)
            content = match.group(2 if '分钟后' in time_str else 3).strip()
            return time_str, content
        return None, None

    def parse_time(self, time_str):
        now = datetime.now()
        if '分钟后' in time_str:
            minutes = int(re.search(r'(\d+)', time_str).group(1))
            return now + timedelta(minutes=minutes)
        elif '下午' in time_str or '上午' in time_str:
            hour = int(re.search(r'(\d+)', time_str).group(1))
            if '下午' in time_str:
                hour += 12
            return now.replace(hour=hour, minute=0, second=0, microsecond=0)
        return None
