# Generating G-code

## Pen G-code ! ! !

If you Used Pen holder with servo arm and Lego axels:
* pen down M280 P0 S100
* pen up M280 P0 S0

If you Used Pen holder with gear:
* pen down M280 P0 S0
* pen up M280 P0 S100

## My workaround for generating g-code (avoid if possible)

I do not recommend this tutorial unless you can make your Inkscape working nicely. This folder only describes my workaround which is far away from effective.
Softwares used for this tutorial:

* G-CODE Generator - by Opt Lasers v1.1
* Inkscape v0.9.2

Preparation:
1. Move 2D Plotter.gcd to Setting folder of G-CODE generator

Steps for creating g-code for your 2D plotter:

1. Open Inkscape and import picture you would like to plot
2. Click on the imported object with right mousebutton and select Trace Bitmap
3. Create Bitmap and drag out imported object
4. Save as .dxf
5. Open G-CODE Generator
6. Open DXF File (-> select your .dxf from Inkscape)
7. Go to G-CODE tab and select Generate G-code
8. Save G-code as "gcode.gcode" into folder where is adjust_gcode.py
9. Run python script -> Output G-Code is can be loaded to 2D plotter

In case you decided to follow those instructions and struggle with any aspect of 2D plotter (Hardware, Firmware or G-Code generation) feel free to contact me.

## SW links
* https://optlasers.com/cnc-software/g-code-generator
* https://inkscape.org/release/inkscape-1.0.2/