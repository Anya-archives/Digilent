import dwf
from dwf import *
import time
# Open the device
dwf_dev = Dwf()
# Check if the device is open
if not dwf_dev:
    print("Failed to open device.")
else:
    print("device found")
