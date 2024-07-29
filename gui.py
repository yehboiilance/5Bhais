import wx
import time


class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent = None, title = "Focus or Fail")
        panel = wx.Panel(self)        
        my_sizer = wx.BoxSizer(wx.VERTICAL)        
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)        
        my_btn = wx.Button(panel, label="Start focusing")
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)        
        panel.SetSizer(my_sizer)
        self.Show()

    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')


    def increment(i):
        i += 1

    def decrement(i):
        i -= 1

    def studyTimer(minutes):
        while (minutes):
            m, s = divmod(minutes, 60)
            timer = "{:02d}:{:02d}".format(m, s)
            print(timer, end = "\r")
            time.sleep(1)
            minutes -= 1
        print("Time for a break!")

    def breakTimer(minutes):
        while (minutes):
            m, s = divmod(minutes, 60)
            timer = "{:02d}:{:02d}".format(m, s)
            print(timer, end = "\r")
            time.sleep(1)
            minutes -= 1
    
    def mainTimer():
        #First click start button
        print("*Starts focusing*")
        



    def countdownTimer():
        # While app is running

        while (True):

            mins, secs = divmod(25, 0) 
            timer = '{:02d}:{:02d}'.format(mins, secs) 
            print(timer, end="\r") 
            time.sleep(1) 
            t -= 1


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()