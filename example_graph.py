'''

reading channel 0 example

this script may be used from the command line:

        "python example_graph.py"

'''
# 4. April 2020, ChrisMicro: initial version

import scope
import numpy as np
import matplotlib.pyplot as plt
import time

# the path depends on your PC
device_path="/dev/usbtmc2"

# Create scope object and retrieve data
# scope.DS1000(device_path, num_channels):
scp = scope.DS1000(device_path, 2)

# set long memory depth, for DS1052 this is 524288 values for two channels
# set normal memory depth, for DS1052 this is 8192 values for two channels in stop mode
#scp.set_MemoryLong()
scp.set_MemoryNormal()

def showData():

  waveform_pnts_mode = "RAW" # use raw for 8192 points in run or 524288 points in stop mode
  #waveform_pnts_mode = "NOR" # use normal for 600 points
  scp.run()
  time.sleep(1)
  scp.stop() # oscilloscope has to be stopped to get long data
  scp.query_scope(waveform_pnts_mode)
  
  x = scp.time_axis[scope.SAMPLES] * scp.time_per_division

  #samplingTime=scp.time_per_division
  samplingTime=x[2]-x[1]
  print("sampling time:",samplingTime)
  print("window time time:",(len(x)-1)*samplingTime)

  # channel index starts from 0
  # Be sure that channel 0 is activated in the oscilloscope ( use buttons ) 
  channel=scp.active_channels[0]
  # get data
  y = channel.volt_points * channel.volts_div
  print("data length:",len(y))

  plt.plot(x,y);
  plt.title("Rigol DS1052E")
  plt.xlabel("time [s]")
  plt.ylabel("Voltage [V]")
  plt.grid();
  plt.show();

showData()


