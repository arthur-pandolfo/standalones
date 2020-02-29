#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
****************
(EN) DESCRIPTION
****************

This file acquires measurements of the scale Marte AD 200.
Each communication delivers 67 bites, of which:
- 25 to 32 (inclusive) are the offset
- 41 to 48 (inclusive) are the weight

The code exits if the scale registers zero. pyserial library required.
Running:

>>> python marte_ad_200.py serial_port baud_rate path_to_export_file

Exported file is plain text.

**************
(PT) DESCRIÇÃO
**************

Este arquivo adquire medições da balança Marte AD 200.
Cada comunicação retorna 67 bytes, dos quais:
- 25 até 32 (inclusive) são a tara
- 41 até 48 (inclusive) são o peso

O código se encerra se a balança registrar peso zero. Biblioteca pyserial
necessária.
Rodando:

>>> python marte_ad_200.py serial_port baud_rate caminho_para_exportar

Arquivo exportado é de texto.
"""

import serial
import datetime

### INPUTS
# to see the open ports: python -m serial.tools.list_ports
# to open a port (linux): sudo chmod 666 port_name (e.g.) /dev/ttyUSB0

serial_port,baud_rate,filepath = sys.args[0]

ser = serial.Serial(serial_port, baud_rate)

with open(filepath,'x') as file:
    try:
        while True:
            output = []
            while len(output) == 0:
                output = ser.read_until(b"ENTER.")
            output = str(output)
            now    = datetime.datetime.now()
            to_file = str(now)+';'+str(output)
            file.write(to_file+'\n')
            print(to_file)
    except:
        ser.close()
        pass
