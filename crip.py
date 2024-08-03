import wx

class ClockApp(wx.App):
    def __init__(self):
        wx.App.__init__(self)
        self.frame = wx.Frame(None, title='Demo', size=(400, 300))
        self.panel = wx.Panel(self.frame)

        # Drop down menu
        menubar = wx.MenuBar()
        menu = wx.Menu()
        quit_item = menu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(menu, '&File')
        self.frame.SetMenuBar(menubar)
        
        # Bind
        self.frame.Bind(wx.EVT_MENU, self.on_quit, quit_item)

        # Timer
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_clock, self.timer)

        # Welcome message
        welcome_text = wx.StaticText(self.panel, label="Welcome to User", pos=(10, 10))

        # Start button
        start_button = wx.Button(self.panel, label="Start", pos=(10, 100))
        start_button.Bind(wx.EVT_BUTTON, self.on_start)

        # Rectangle for timer
        self.time_display = wx.StaticText(self.panel, label="00:00", pos=(10, 50), size=(100, 50))

        # Show the frame
        self.frame.Show()

    def on_quit(self, event):
        self.frame.Close()

    def on_start(self, event):
        self.timer.Start(1000)  # Timer will trigger every second

    def update_clock(self, event):
        # Update the clock display
        current_label = self.time_display.GetLabel()
        minutes, seconds = map(int, current_label.split(':'))
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
        self.time_display.SetLabel(f"{minutes:02}:{seconds:02}")

if __name__ == '__main__':
    app = ClockApp()
    app.MainLoop()
