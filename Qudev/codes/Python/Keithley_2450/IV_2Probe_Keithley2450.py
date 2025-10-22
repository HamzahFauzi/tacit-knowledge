import time
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import csv
import pyvisa
import  os


#=== Open VISA === 
rm = pyvisa.ResourceManager()


#=== Define GPIB Address ===
GPIBAddress = 'GPIB0::24::INSTR'
keithley = rm.open_resource(GPIBAddress)

#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#  MEASUREMENT PARAMETER  #--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#


#=== Directory and CSV file name ===
save_dir = "D:/2_Work/Research/Experiments/5_TMDs and device/Data/IV/20251017"
file_name = "Measurement_test_6.csv"


#=== User Parameters (Global variable) ====
vds_from = -1 #in voltage
vds_to = 1  #in voltage
vds_step = 0.05 #in voltage
vds_delay = 0.2  # seconds between steps
current_limit = 0.1 #compliance limit (10 mA)


#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#


#=== set timeout, termination characters ===
keithley.timeout = 5000  # in ms
keithley.write_termination = '\n'
keithley.read_termination = '\n'


#=== Instrument Initialization ===
keithley.write('*RST')
keithley.write(':SOUR:FUNC VOLT')
keithley.write('SENS:CURR:NPLC 1')
keithley.write(':SENS:FUNC "CURR"')
keithley.write(f':SOUR:VOLT:ILIM:LEV {current_limit}')
keithley.write(':OUTP ON')


#=== Creating directory and CSV file ===#
csv_filename = os.path.join(save_dir, file_name)
if not os.path.exists(csv_filename):
    df = pd.DataFrame(columns=["Voltage (V)", "Current (A)"])
    df.to_csv(csv_filename, index=False)


#=== Setup Plot / activate interactive mode ===
plt.ion()
fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot(x_data, y_data, marker="o")
ax.set_xlabel("V_DS (V)")
ax.set_ylabel("I_DS (A)")


#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--# MEASUREMENT PROCESS  #--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#

#=== Sweeping to start voltage ===
v_init_step = vds_from/20
v_init = np.linspace(0, vds_from, int((vds_from - 0)/v_init_step) + 1)

for v_init_to in v_init:
    keithley.write(f":SOUR:VOLT {v_init_to};")
    keithley.write(":READ?;")
    init_resp = keithley.read() 

    print(f"{v_init_to}; {init_resp}" )

    time.sleep(1)


#=== Start the Measurement ===
vds = np.linspace(vds_from, vds_to, int((vds_to - vds_from)/vds_step) + 1)
print (vds)

try:
    for v in vds:
        keithley.write(f":SOUR:VOLT {v};")
        keithley.write(":READ?;")
        response = keithley.read()
        
        v_meas = v
        i_meas = float(response)
        
        x_data.append(v_meas)
        y_data.append(i_meas)
        
        # Update plot
        line.set_data(x_data, y_data)
        ax.relim()
        ax.autoscale_view()
        fig.canvas.draw()
        fig.canvas.flush_events()
        
        print(f"{v}; {response}")

        # Append to CSV
        new_row = pd.DataFrame([[v_meas, i_meas]], columns=["Voltage (V)", "Current (A)"])
        new_row.to_csv(csv_filename, mode='a', header=False, index=False)

        time.sleep(vds_delay)
              
    for v in reversed(vds):
        keithley.write(f":SOUR:VOLT {v};")
        keithley.write(":READ?;")
        response = keithley.read()
        
        v_meas = v
        i_meas = float(response)
        
        x_data.append(v_meas)
        y_data.append(i_meas)
        
        # Update plot
        line.set_data(x_data, y_data)
        ax.relim()
        ax.autoscale_view()
        fig.canvas.draw()
        fig.canvas.flush_events()
        
        print(f"{v}; {response}")

        # Append to CSV
        new_row = pd.DataFrame([[v_meas, i_meas]], columns=["Voltage (V)", "Current (A)"])
        new_row.to_csv(csv_filename, mode='a', header=False, index=False)

        time.sleep(vds_delay)

    plt.ioff()
    plt.show()


#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#


except KeyboardInterrupt:
    print("\nMeasurement interrupted by user.")

finally:
    print("Turning off output and resetting Keithley...")
    try:
        keithley.write(":OUTP OFF;")
        keithley.write("*RST;")
    except Exception as e:
        print(f"Error during shutdown: {e}")
    keithley.close()
    rm.close()
    plt.ioff()
    print("Cleanup done.")
