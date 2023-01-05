
class CNC:
    def __init__(self):
        self.axis_maxspeed_rapid_positioning=20000
        self.current_feed=50
        self.spindle_rpm=500
        self.spindle_on_time=0.1
        self.tool_change_time=1
        self.rapid_positioning_mode=0   #0 for max feed rate positioning 
