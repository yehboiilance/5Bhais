import wx
import time

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title="Focus or Fail")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.timer_label = wx.StaticText(panel, label="00:00")
        my_sizer.Add(self.timer_label, 0, wx.ALL | wx.CENTER, 5)

        my_btn = wx.Button(panel, label="Start focusing")
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)        
        
        panel.SetSizer(my_sizer)
        
        self.study_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_study_timer, self.study_timer)
        
        self.break_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_break_timer, self.break_timer)
        
        self.study_duration = 0
        self.break_duration = 0
        
        self.Show()

    def on_press(self, event):
        self.study_duration = 25 * 60  # Set study duration to 25 minutes (1500 seconds)
        self.break_duration = 5 * 60  # Set break duration to 5 minutes (300 seconds)
        self.start_study_timer()

    def start_study_timer(self):
        self.study_timer.Start(1000)  # Start study timer to tick every 1 second
        print("Study timer started!")

    def on_study_timer(self, event):
        if self.study_duration > 0:
            self.study_duration -= 1
            m, s = divmod(self.study_duration, 60)
            timer = "{:02d}:{:02d}".format(m, s)
            self.timer_label.SetLabel(timer)
        else:
            self.study_timer.Stop()
            self.timer_label.SetLabel("Time for a break!")
            print("Time for a break!")
            self.start_break_timer()

    def start_break_timer(self):
        self.break_timer.Start(1000)  # Start break timer to tick every 1 second
        print("Break timer started!")

    def on_break_timer(self, event):
        if self.break_duration > 0:
            self.break_duration -= 1
            m, s = divmod(self.break_duration, 60)
            timer = "{:02d}:{:02d}".format(m, s)
            self.timer_label.SetLabel(timer)
        else:
            self.break_timer.Stop()
            self.timer_label.SetLabel("Break time is over! Back to focus!")
            print("Break time is over! Back to focus!")

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
