import config.Variables_Pid.pid_config as vpid

def minimizar_integral(integral):
    return max(min(integral, integral*0.7), -integral*0.7)
    
    