#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This Source Code is distributed under the MIT License - check
# https://github.com/arthur-pandolfo/standalones/blob/master/LICENSE for detais

"""
****************
(EN) DESCRIPTION
****************

This file acquires measurements of the scale Marte AD 6000.
Each communication delivers 67 bites, of which:
- 25 to 32 (inclusive) are the offset
- 41 to 48 (inclusive) are the weight

The code exits if the scale registers zero. pyserial library required.
Running:

>>> python marte_ad_6000.py serial_port baud_rate path_to_export_file

Exported file is plain text.

**************
(PT) DESCRIÇÃO
**************

Este arquivo adquire medições da balança Marte AD 6000.
Cada comunicação retorna 67 bytes, dos quais:
- 25 até 32 (inclusive) são a tara
- 41 até 48 (inclusive) são o peso

O código se encerra se a balança registrar peso zero. Biblioteca pyserial
necessária.
Rodando:

>>> python marte_ad_6000.py serial_port baud_rate caminho_para_exportar

Arquivo exportado é de texto.
"""
import sys

### INPUTS
# to see the open ports: python -m serial.tools.list_ports
# to open a port (linux): sudo chmod 666 port_name (e.g.) /dev/ttyUSB0

#serial_port = 'COM4'
#baud_rate   = 9600

serial_port,baud_rate,filepath = sys.args[0]

### CODE
def run_aquisition(file):
    ser  = serial.Serial(serial_port, baud_rate)
    
    while True:
        
        # the file is opened and closed every time in order not to lose
        # everything should something happen
        file = open(file.name,'a')
        
        # the scale sends 67 bytes at a time
        byte_val = ser.read(67)
        
        # the scale gives values in bytes. The following lines try to convert
        # the bytes that are retrieved into a value. The first value of a byte
        # is the sign of the value, which is discarded
        try:
            float_val    = float(byte_val[40:48])
            current_time = datetime.datetime.now()
            print(str(current_time),float_val)
        except ValueError:
            print("Data aquisition failed, trying again...")
            continue
        else:
            file.write(str(current_time)+';'+str(float_val)+'\n')
        
        if float_val == 0.0:
            print("Zero value found, exiting...")
            ser.close()
            file.close()
            break
       
        file.close()

# code starts here
import serial
import datetime

try:
    file = open(filepath,'r')
except FileNotFoundError:
    file = open(filepath,'w')
    run_aquisition(file)
else:
    print("There is already a file open. Change it and run again.")
    file.close()
