import shutil
import ctypes
import sys

"""
author: Juraj Zovinec
description: adjust_gcode is simple script which grabs G1 and G0 path commands from file named "gcode.gcode". 
For those commands is set F argument (speed).
if you have installed python 3, you can run this script for cmd line python adjust_gcode.py
"""

def main():

    usb_path = "E:\\"
    input_gcode = open("gcode.gcode", "r")
    desired_g1_feedrate = "F1000" #pen speed while pen is driving

    output_gcode_write = open("gcodeWithFeed.gcode", "w")
    output_gcode_write.write("")
    output_gcode_write.close()

    output_gcode_append = open("gcodeWithFeed.gcode", "a+")

    output_gcode_list = []

    for each_line in input_gcode.readlines():
        each_line = each_line.rstrip()
        each_line = each_line.strip()

        if "G1" in each_line and "F" not in each_line:
            output_gcode_list.append(each_line + " " + desired_g1_feedrate)

        if "G0" in each_line:
            output_gcode_list.append("M400")
            output_gcode_list.append("M280 P0 S100")
            output_gcode_list.append(each_line)
            output_gcode_list.append("M400")
            output_gcode_list.append("M280 P0 S0")
            output_gcode_list.append("M400")

    output_gcode_append.write("M280 P0 S100" + "\n")
    output_gcode_append.write("G28 XY" + "\n")

    for each_line in output_gcode_list:
        output_gcode_append.write(each_line + "\n")

    output_gcode_append.write("M280 P0 S100" + "\n")
    output_gcode_append.write("G28 XY" + "\n")

    output_gcode_append.close()
    input_gcode.close()

    try:
        shutil.copy2("GcodeAdjustedFor2DPlotter.gcode", usb_path)
    except FileNotFoundError:
        ctypes.windll.user32.MessageBoxW(0, "Plug In USB", "Result", 1)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        ctypes.windll.user32.MessageBoxW(0, "Could not export file on USB drive, result file stored as adjusted.gcode", "Result", 1)
    else:
        print('good')
        ctypes.windll.user32.MessageBoxW(0, "FileExported on USB drive", "Result", 1)


main()

