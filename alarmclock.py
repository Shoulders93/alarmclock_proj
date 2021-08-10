class Alarmclock:
    def __init__(self, current_time, set_alarm):
        self.current_time = current_time
        self.alarm_on = False
        self.alarm_off = True
        self.time_alarm_set = set_alarm


    def trigger_alarm(self):
        if (self.alarm_on == False):
            self.current_time += 1
            print('Your alarm has not gone off yet')
        elif (self.current_time == self.time_alarm_set):
            self.alarm_on == True
            print("You're alarm is going off!")
