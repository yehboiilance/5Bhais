import customtkinter as ctk
import time

# Initialize the application
app = ctk.CTk()
app.title("Focus Timer")
app.geometry("400x300")

# Function to start the countdown
def start_countdown(duration):
    for remaining in range(duration, 0, -1):
        mins, secs = divmod(remaining, 60)
        timer_label.configure(text=f"{mins:02d}:{secs:02d}")
        app.update()
        time.sleep(1)
    timer_label.configure(text="Time's up!")

# Button command functions
def set_time_5min():
    start_countdown(5 * 60)

def set_time_10min():
    start_countdown(10 * 60)

def set_time_15min():
    start_countdown(15 * 60)

def set_time_30min():
    start_countdown(30 * 60)

# Create buttons
button_5min = ctk.CTkButton(app, text="5 Minutes", command=set_time_5min)
button_10min = ctk.CTkButton(app, text="10 Minutes", command=set_time_10min)
button_15min = ctk.CTkButton(app, text="15 Minutes", command=set_time_15min)
button_30min = ctk.CTkButton(app, text="30 Minutes", command=set_time_30min)

# Arrange buttons in a grid
button_5min.grid(row=0, column=0, padx=20, pady=20)
button_10min.grid(row=0, column=1, padx=20, pady=20)
button_15min.grid(row=1, column=0, padx=20, pady=20)
button_30min.grid(row=1, column=1, padx=20, pady=20)

# Create a label for the timer display
timer_label = ctk.CTkLabel(app, text="00:00", font=("Helvetica", 48))
timer_label.grid(row=2, column=0, columnspan=2, pady=20)

# Start the application
app.mainloop()
