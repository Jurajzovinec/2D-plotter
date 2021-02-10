# 2D Plotter

Requirements:
* MKS Base v1.4 mainboard
* HD44780 lcd
* aluminium profiles 40x20 mm and 20x20 mm

This repository documents process of transforming old 3D printer to 2D plotter. Project consists of two mian parts:

1. Hardware
2. Firmware
3. G-code generation

## Hardware of 2D plotter

Hardware part of this project is mostly inspired by this video https://youtu.be/6874VkJRhn4, where Biseyler Yapalim describes fabrication of his laser drawing robot. Most of the components has been used in this project however there are some that I had to modify. These parts could be found in 

|--Hardware
|  |--PlotterPartsTo3Dprint

Also for this purpose I designed compact electronics enclouse which components could be found in 

|--Hardware
|  |--CompactElectronicCaseTo3Dprint

Tbh I was not totally satisfied with Biseyler Yapalim's solution of pen holder, so I decided to design my own. This solution could be found in

|--Hardware
|  |--PenHolderTo3Dprint

## Firmware of 2D plotter

Firmware part of this project is based on Jim's Brown modification of Marlin firmware, which he configured specialy for 3D printer Tevo Tarantula. I did couple of changes to this firmware in order to adjust it's functionality for 2D plotter and simplified user interface.

## Generating the g-code

3rd aspect of 2D plotter is process of creating g-code.

## 2D plotter in Action !

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/rGozqXQ0cDk/0.jpg)](https://www.youtube.com/watch?v=rGozqXQ0cDk)

## Source information
* BLUETOOTH XY PLOTTER -> yt series https://youtu.be/6874VkJRhn4, https://www.thingiverse.com/thing:4685871
* Jim's Brown Marlin firmware configuration -> https://github.com/JimBrown/MarlinTarantula
