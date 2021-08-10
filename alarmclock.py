class Alarmclock:
    def __init__(self):
        self.current_time = 0
        self.time_alarm_set = 0
        self.alarm_on = False
        self.alarm_off = True


    def set_time_and_alarm(self, current_time, time_alarm_set):
        self.current_time = current_time
        self.time_alarm_set = time_alarm_set

    def trigger_alarm(self):
        while (self.alarm_on == False):
            if (self.current_time == self.time_alarm_set):
                self.alarm_on = True
                print(self.current_time)
                print("You're alarm is going off!")
            elif (self.alarm_on == False):
                print(self.current_time)
                self.current_time = self.current_time + 1
                print('Your alarm has not gone off yet')