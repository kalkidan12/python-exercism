def is_criticality_balanced(temperature, neutrons_emitted):
    if(temperature < 800 and neutrons_emitted > 500):
        return temperature*neutrons_emitted < 500000
    return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage*current
    efficiency = (generated_power/theoretical_max_power)*100
    if(efficiency >= 80):
        return 'green' 
    if(efficiency >=60):
        return 'orange' 
    if(efficiency >=30):
        return 'red' 
    if(efficiency <=30):
        return 'black' 
    



def fail_safe(temperature, neutrons_produced_per_second, threshold):
    if(temperature * neutrons_produced_per_second < threshold*0.9):
        return 'LOW'
    if(temperature * neutrons_produced_per_second >= threshold*0.9 and temperature * neutrons_produced_per_second <= threshold*1.1):
        return 'NORMAL'
    
    return 'DANGER'
