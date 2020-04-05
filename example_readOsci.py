'''

reading channel 0 example

this script may be used from the command line:

        "python example_readOsci.py"

'''
# 4. April 2020, ChrisMicro: initial version

import scope
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

  waveform_pnts_mode = "RAW" # NOR,RAW,MAX see Programming Guide
  # in RAW mode number of volt_points depend on the oscilloscopes 
  # MemDeph setting and if the osciiloscope is in run or stop mode
  # RAW together with the stop mode returns the longes data

  scp.run()
  time.sleep(1)
  scp.stop() # oscilloscope has to be stopped to get long data
  scp.query_scope(waveform_pnts_mode)
  

  x=scp.time_axis[scope.SAMPLES]

  # channel index starts from 0
  channel=scp.active_channels[0]
  y=channel.volt_points
  print("data len read:",len(y))
  print("time , data")
  for n in range(0,10):
    print(x[n],y[n])
  
  print()
  print("###### signal properties ######")
  channel=scp.active_channels[0]
  print("vmax:",channel.vmax)
  print("vmin:",channel.vmin)
  print("vpp:",channel.vpp)
  print("vrms:",channel.vrms,"( root mean square voltage )")
  print()

showData()


