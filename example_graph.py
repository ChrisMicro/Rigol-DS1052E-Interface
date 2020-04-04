# reading channel 0 example

# 4. April 2020, ChrisMicro: initial version

import scope
import numpy as np
import matplotlib.pyplot as plt

# the path depends on your PC
device_path="/dev/usbtmc2"

# Create scope object and retrieve data
# scope.DS1000(device_path, num_channels):
scp = scope.DS1000(device_path, 2)


def showData():

  waveform_pnts_mode = "RAW"
  scp.query_scope(waveform_pnts_mode)
  
  x = scp.time_axis[scope.SAMPLES] * scp.time_per_division

  # channel index starts from 0
  # Be sure that channel 0 is activated in the oscilloscope ( use buttons ) 
  channel=scp.active_channels[0]
  # get data
  y = channel.volt_points * channel.volts_div

  plt.plot(x,y);
  plt.title("Rigol DS1052E")
  plt.xlabel("time [s]")
  plt.ylabel("Voltage [V]")
  plt.grid();
  plt.show();

showData()


