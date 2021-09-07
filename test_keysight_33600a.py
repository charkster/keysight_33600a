#!/usr/bin/python3

from __future__ import print_function
import pyvisa
from keysight_33600a import keysight_33600a
import time

rm = pyvisa.ResourceManager('@py')
k33611a = rm.open_resource('USB0::2391::18439::MY59000716::0::INSTR')
keysight_33611a = keysight_33600a(pyvisa_resource=k33611a)

#print(k33611a.query("*IDN?"))
#k33611a.write("*RST")
print(keysight_33611a.get_unique_scpi_list())
