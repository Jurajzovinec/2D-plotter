# Marling configuration for 2D plotter

This is my configuration of marlin for MKS_Base v1.4 mainboard and HD44780 lcd.

## List of configuration changes I have done:

* extruders have been deactivated
* heat bed has been deactivated 
* XY dimensions has been changed
* servos_0 have been allowed
* servo default angle has been changed
* X and Y direction has been changed
* Z endstop error has been deactivated
* "autohome" command has been declared only for X and Y axis
* main menu has been displaying less sub-menus
* name of the printer has been changed
* couple of marlinUI items have been renamed in english mode (for example "Print from media" has been changed to "Draw from media")

To look for all changes search for string "// Juraj" throughout all the project. Some short explanation is attached to every change.

## Upload process

1. Open this folder with VScode
2. Install Platformio VScode extension in order to upload Firmware on your mainboard
3. Build firmware 
4. Upload firmware on your mainboard



