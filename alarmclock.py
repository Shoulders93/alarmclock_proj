class Alarmclock:
    def __init__(self, current_time, alarm_time):
        self.current_time = current_time
        self.alarm_on = []
        self.alarm_off = []
        self.time_alarm_set = alarm_time

    def alarm(self):
        self.change_current_time += 1