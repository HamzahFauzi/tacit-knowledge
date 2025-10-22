#=== Define package ===#
import time
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import csv
import pyvisa
import  os


#=== Open VISA ===#
rm = pyvisa.ResourceManager()


#=== Define GPIB Address ===#
GPIBAddress_1 = 'GPIB0::24::INSTR'
GPIBAddress_2 = 'GPIB0::18::INSTR'

keithley_VDS = rm.open_resource(GPIBAddress_1)
keithley_VG = rm.open_resource(GPIBAddress_2)


#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#  MEASUREMENT PARAMETER  #--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#

#==== Directory and Filename ====#
save_dir = "D:/2_Work/Research/Experiments/5_TMDs and device/Data/IV/20251017"
file_name = "20250918_Test "

#******* (Fixed VD, sweeping VG) *******#
#==== VDS parameter =====#
vds_set = 0.20 #in V
vds_step = 0.02 #in V
vds_delay = 0.5  # in seconds between steps
vds_current_limit = 0.5 #in A 

#==== VG parameter =====#
vg_set = 0 #in V
vg_step = 0 #in V
vg_delay = 0.2  # in seconds between steps
vg_current_limit = 0.5 #in A 

#=== time ===#
t_measure = 300 # in seconds
t_delay = 0.1 #in seconds

#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#


#=== set timeout, termination characters ===#
keithley_VDS.timeout = 5000  # in ms
keithley_VG.timeout = 5000  # in ms
keithley_VDS.write_termination = '\n'
keithley_VG.write_termination = '\n'
keithley_VDS.read_termination = '\n'
keithley_VG.read_termination = '\n'


#=== Instrument Initialization ===#
keithley_VDS.write('*RST')
keithley_VDS.write(':SOUR:FUNC VOLT')
keithley_VDS.write(':SOUR:VOLT:DEL 0')
keithley_VDS.write(':SENS:FUNC "CURR"')
keithley_VDS.write('SENS:CURR:NPLC 1')
keithley_VDS.write(f':SOUR:VOLT:ILIM:LEV {vds_current_limit}')
keithley_VDS.write(':OUTP ON')

keithley_VG.write('*RST')
keithley_VG.write(':SOUR:FUNC VOLT')
keithley_VG.write(':SOUR:VOLT:DEL 0')
keithley_VG.write(':SENS:FUNC "CURR"')
keithley_VG.write('SENS:CURR:NPLC 1')
keithley_VG.write('SENS:CURR:RANG 0.01')
#keithley_VG.write(f':SOUR:VOLT:ILIM:LEV {vg_current_limit}')
keithley_VG.write(':OUTP ON')


#=== Creating directory and CSV file ===#

csv_filename = os.path.join(save_dir, file_name + "-Time.csv")
if not os.path.exists(csv_filename):
    df = pd.DataFrame(columns=["Time (s)", "IDS (A)", "IG (A)"])
    df.to_csv(csv_filename, index=False)


#=== Setup Plot / activate interactive mode ===#
plt.ion()

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
x_data, y1_data, y2_data = [], [], []

line1, = ax1.plot(x_data, y1_data, marker="o")
line2, = ax2.plot(x_data, y1_data, marker="o")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("ID")
ax1.set_title("ID-Time transfer curve")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("IG")
ax2.set_title("IG-Time (Leak current))")



#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--# MEASUREMENT PROCESS  #--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#
try:
    # === Set VD ===#
    if vds_set != 0:
        vd_measure = np.linspace(0, vds_set, int((vds_set - 0)/vds_step) + 1)
        for i in vd_measure:
            #===== Interloop VD =====#
            keithley_VDS.write(f":SOUR:VOLT {i};")
            keithley_VDS.write(":READ?;")
            init_resp = keithley_VDS.read() 

            vds_set_to = i
            print(f"{i}; {init_resp}" )
            time.sleep(vds_delay)
    
    else:
        vds_0 = 0
        keithley_VDS.write(f":SOUR:VOLT {vds_0};")
        keithley_VDS.write(":READ?;")
        init_resp = keithley_VDS.read() 
        vds_set_to = 0

        print(f"0.0; {init_resp}")
    
    print(f"VDS = {vds_set_to}")
    time.sleep(1)

    #==== Append to CSV ====#
    new_row = pd.DataFrame([[vds_set_to, '', '']], columns=["Time (s)", "IDS (A)", "IG (A)"])
    new_row.to_csv(csv_filename, mode='a', header=False, index=False)

       
    #=== set VG ===#
    if vg_set != 0:
        vg_measure = np.linspace(0, vg_set, int((vg_set - 0)/vg_step) + 1)
    
        for i in vg_measure:
            #===== Interloop VD =====#
            keithley_VG.write(f":SOUR:VOLT {i};")
            keithley_VG.write(":READ?;")
            init_resp = keithley_VG.read() 

            vg_set_to = i
            print(f"{i}; {init_resp}" )
            time.sleep(vg_delay)
    else:  
        vg_0 = 0
        keithley_VG.write(f":SOUR:VOLT {vg_0};")
        keithley_VG.write(":READ?;")
        init_resp = keithley_VG.read() 
        vg_set_to = 0

        print(f"0.0; {init_resp}")

    print(f"VG = {vg_set_to}")
    time.sleep(1)

    #==== Append to CSV ====#
    new_row = pd.DataFrame([[vg_set_to, '', '']], columns=["Time (s)", "IDS (A)", "IG (A)"])
    new_row.to_csv(csv_filename, mode='a', header=False, index=False)


    #=== ID-Time ===#
    t_loop = np.linspace(0, t_measure, int((t_measure - 0)/t_delay) + 1)

    for j in t_loop:
        
        t_stamp = j
                         
        keithley_VG.write(":READ?")
        response_Ig = keithley_VG.read()

        keithley_VDS.write(":READ?")
        response_Ids = keithley_VDS.read() 
                    
        ids_meas = float(response_Ids)
        ig_meas = float(response_Ig)
                    
        x_data.append(t_stamp)
        y1_data.append(ids_meas)
        y2_data.append(ig_meas)
                    
        #==== Update plot ====#
        line1.set_data(x_data, y1_data)
        ax1.relim()
        ax1.autoscale_view()
        fig1.canvas.draw()
        fig1.canvas.flush_events()
        line2.set_data(x_data, y2_data)
        ax2.relim()
        ax2.autoscale_view()
        fig2.canvas.draw()
        fig2.canvas.flush_events()

        print(f"{j}; {response_Ids}")

        #==== Append to CSV ====#
        new_row = pd.DataFrame([[t_stamp, ids_meas, ig_meas]], columns=["Time (s)", "IDS (A)", "IG (A)"])
        new_row.to_csv(csv_filename, mode='a', header=False, index=False)

        time.sleep(t_delay)
        
        
    #======= Return VG and VDS to 0 V ======#
    keithley_VDS.write(f":SOUR:VOLT 0")
    keithley_VG.write(f":SOUR:VOLT 0")
    plt.show()


#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#


except KeyboardInterrupt:
    print("\nMeasurement interrupted by user.")

finally:
    print("Turning off output and resetting Keithley...")
    try:
        keithley_VDS.write(":OUTP OFF")
        keithley_VG.write(":OUTP OFF")
        keithley_VDS.write("*RST;")
        keithley_VG.write("*RST;")
    except Exception as e:
        print(f"Error during shutdown: {e}")
    keithley_VDS.close()
    keithley_VG.close()
    rm.close()
    plt.ioff()
    print("Cleanup done.")
