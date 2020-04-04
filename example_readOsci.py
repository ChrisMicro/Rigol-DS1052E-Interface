'''

reading channel 0 example

this script may be used from the command line:

        "python example_readOsci.py"

'''
# 4. April 2020, ChrisMicro: initial version

import scope

# the path depends on your PC
device_path="/dev/usbtmc2"

# Create scope object and retrieve data
# scope.DS1000(device_path, num_channels):
scp = scope.DS1000(device_path, 2)


def showData():

  waveform_pnts_mode = "RAW"
  scp.query_scope(waveform_pnts_mode)
  
  x=scp.time_axis[scope.SAMPLES]

  # channel index starts from 0
  channel=scp.active_channels[0]
  y=channel.volt_points
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


