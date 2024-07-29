# importing the time module  
import time  
# defining the countdown function.  
def countdown(minutes):      
    while (minutes):
        m, s = divmod(minutes, 60)  
        timer = '{:02d}:{:02d}'.format(m, s)  
        print(timer, end="\r")  
        time.sleep(1)  
        minutes -= 1       
    print('Fire in the hole!!')  
# input the time value in seconds  

# function call at the program  
countdown(1500)  