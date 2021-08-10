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
        if (self.alarm_on == False):
            print('Your alarm has not gone off yet')
        elif (self.current_time == self.time_alarm_set):
            self.alarm_on == True
            print("You're alarm is going off!")





