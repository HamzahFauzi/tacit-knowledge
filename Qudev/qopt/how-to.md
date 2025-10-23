### OBIS LS Laser
The laser unit is already assembled and, by default, fiber-connected to the G&H AOM. The laser will output 532 nm green beam with vertically polarized light (100:1 ratio). The max intesity is 20 mW and software controlled.

### Acoustic Opto Modulator (AOM)

The OBIS LS laser is modulated by a G&H Fiber-Coupled Acousto-Optic Modulator (Fiber-Q® 532 nm, 200 MHz). The AOM is driven by a 3910 series RF driver.

First connect the RF output to the AO modulator with an SMA jack connector. The RF output impedance is 50 ohms. Always connect the RF output to an AO device (or a 50 Ohm load) prior to connecting power to the driver. Fail to do so might damage the driver!

Next, power the driver using a LeCroy power supply placed nearby. Connect the power supply to the driver using a special BNC cable. Set the voltage to 24 V, and then turn the voltage ON. If the green LED on the rear panel of the driver turns ON, it indicates that the driver is activated and the voltage is being properly supplied. If not, you need to increase the voltage. The 3910 drivers will run on voltages from +24V - +28V.


Next, connect the analog modulation port to a dedicated function generator (WF1973). This port uses an SMB jack connector and accepts a 0–1 V input signal with an input impedance of 50 Ω. The maximum RF output occurs at 1 V, while the minimum RF power corresponds to 0 V. The RF output power varies linearly with the input voltage between 0 and 1 V.

