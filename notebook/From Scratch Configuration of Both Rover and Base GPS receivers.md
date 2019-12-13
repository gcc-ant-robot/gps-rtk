# Introduction

# References:
C099-F9P User Guide (Insert Link)

# Board Components & Description
Each C099-F9P board has two main modules:
* F9P DGNSS Receiver: This module is the GPS receiver of the baord.  It receives RTCM data from an external source and usilizes the GPS antenna to create an RTK solution.
* ODIN-W2 Wifi/Bluetooth Gateway: this module acts as a radio link, enabling the F9P to recieve RTCM data wirelessly over a wifi or bluetooth network.

> NOTE: in order to avoid confusing COM ports with one another, it is recommended that the user only connect ONE gps development board to their laptop at a time. Otherwise, it is possible that you might accidentally upload configuration settings to the rover which were meant for the base station, or visa-versa.

# Preliminary Setup
1. Download and unzip (or extract if you're on windows) the configuration folder here: https://gcc-gps-rtk.s3.amazonaws.com/GCC_Ublox_GPSRTK_Config.zip
2. Make sure you've downloaded and installed Ublox **U-Center and S-Center**.

# Base Station
1. Connect the Wifi and GPS Antennas to the base station board.
2. Make sure all jumpers are removed from the base station board except the single jumper located next to the battery connector.
3. Connect the base station gps receiver to your laptop with a USB cable as shown in **insert figure 1**.

> Note, my macbook pro does not have USB A ports, and so I am using an inline converter as seen in figure 1.  This dongle can be ignored as it is basically a USB passthrough, converting USB-C to USB-A.

## Flash new firmware to the Base Station's ODIN W2 Unit.
When receiving a new gps unit, the firmware on the ODIN W2 (also known as "ODIN") will likely need to be updated.  This process is shown below and mirrors page **insert link and page to document**, except that the files which the manual recommends downloading are already contained in the configuration folder which you downloaded in step **insert step 1.1**.

1. Open the S-Center app on your Windows Laptop.
2. Click "Refresh COM Ports".  Note which port corresponds to the device name ending in "ODIN-W2".  For me, this is COM4.  **insert com4 show picture**
3. Place a jumper over the "SB ODIN" pins (pin pair closest to the Large RGB LED on your development board.) **insert sb picture**.
4. Now, restart the development board by either unplugging the USB cable from your laptop and reconnecting it, or by pressing the "RESET" button on the development baord (button closest to the GPS connector on the board).
5. The ODIN is now in safeboot mode, and is ready to have a new firmware version flashed to its memory.
6. In File Explorer, navigate into the configuration folder which you downloaded in **step 1.1**.  I extracted my folder to `~/Downloads/`, so navigate to `\\Mac\Home\Downloads\GCC_Ublox_GPSRTK_Config\`
7. Now, within this folder, go to the `ODIN-W26X-7` directory which should be at `.GCC_Ublox_GPSRTK_Config\ODIN-W26X-7\`.  You should see the files shown in **insert wxfolder picture.**.
8. In File Explorer's "File" menu, click on "Open Windows PowerShell", this will give you a PowerShell terminal inside the `ODIN-W26X-7` folder.
9. Flash the bootloader by pasting the following into the powershell window, replacing `COM4` with your own COM port: `.\stm32flash.exe -b 115200 -w '.\Bootloader - only needed for recovery\\ODIN-W2-BOOT-v0.8.2.bin' -s 0x000000 COM4`  **insert bootload**
10. Now, flash the firmware update to the ODIN by pasting the following command, again replacing `COM4` with the COM port for your ODIN: `.\stm32flash.exe -b 115200 -w .\ODIN-W26X-SW-7.1.0-020.bin -S 0x8010000 COM4`.  Note that this command should take several minutes to run successfully, but you'll know that it's working if you see something aking to figure **insert odinfirm**.
11. When the previous step is complete, remove the "SB ODIN" jumper and restart the GPS receiver by either pressing the RESET button or unplugging/plugging the USB cable back into your laptop.
12. We will now test the ODIN's firmware upgrade by attempting to connect to it with S-Center.
13. Go back to the S-Center App, you will now connect to the ODIN with the settings showing in figure **insert s-centerconnection** by clicking "Open Port".  Remember to replace `COM4` with the COM address associated with your ODIN module.
14. Before entering any data on the ODIN module through the s-center interface, click the "EVK-ODIN-W2 via ST-LINK" button shown in **insert evk picture**.
15. Verify that you have a working connection to the ODIN by clicking the "AT Mode" button.  You should see some text flash through the console ending with "OK".
16. Change to the "User Defines" tab in S-Center.  Enter and run the following commands sequentially.  These commands change the baud rate of the ODIN to 460800 baud, write the configuration to memory, and then restart the unit.  This is necessary (in my understanding) because the GPS receiver communicates at 460800 baud.
``
AT+UMRS=460800,2,8,1,1,0
AT&W
AT+CPWROFF
``

The output of running these commands should look something like this in the terminal. ``AT+UMRS=460800,2,8,1,1,0
OK
AT&W
OK
AT+CPWROFF
OK
��``
We will have to reconnect to the ODIN module at 460800 baud.

17. Click "Close Port" in the S-Center Window.
18. Now click "Open Port" in the S-Center Window to bring up the connection configuration page.  We will keep the same settings as we used before **insert s-centerconnection**, except change the Baud rate to 460800.  Connect to the ODIN.  If you see the AT console spit out readable messages, then congradulations! Continue with the ODIN Base Configuration section below.

## ODIN Base Station Configuration
In this section, we have just flashed new firmware to the base station's ODIN W2 module, resetting it to its factory defaults.  We will now load a configuration file to it which will allow it to brodcast correction data from the base-station's F9P GPS receiver over the network to a known IP address (which will be the IP of the rover.)  This configuration will also tell the base station to connect to the rover's wifi network (which will be called "UBXWifi").  These instructions correspond to section 6.1 (page 24) of the C099-F9P UserGuide.
1. While connected to the ODIN module of the base-station in S-Center (for instructions, see previous section), click on the "File Menu" in S-Center.
2. Click "Download Configuration" and navigate to the `Base ODIN-W2 Station UDP client.txt` file within the configuration folder you downloaded in **insert download step reference**.  Within the Configuration folder, this text file is located at `.\GCC_Ublox_GPSRTK_Config\ublox-C099_F9P-uCS-master\odin-w2\Base ODIN-W2 Station UDP client.txt`,
3. Once this file is selected, click the "Open" button to load these settings onto your ODIN W2 module.
4. Connect the ODIN to the F9P unit by placing a jumper in position `30E`. See Figure **insert 3oe**.
5. Continue with next section "Base Station F9P Configuration"

## Base Station F9P Configuration
In this section, we tell the base station's GPS receiver (F9P) to stream RTCM data to the ODIN, which has just been configured to receive this data in the last section.  We deviate from the user guides instructions on this operation (given in section 6.1.3.1 of the user guide) so that the base station automatically begin's its survey-in operation when power is connected.
1. Open U-Center
2. Connecting to the GPS Receiver: in the "Receiver" menu of UBlox, select "Connection > Com15", replacing "COM15" with the address of your GPS unit.

> Note, this com port will not be the same com port which you used to communicate with your ODIN module. There is a USB multiplexor on the GPS development board, which has multiple virtual COM ports for the different on-board devices.  From previous experince, the COM port of the GPS receiver which you should use with the U-Center software tends to be the highest COM number which appears.  When connected to the GPS receiver, you'll see that the instrument fields will begin to show live GPS data as seen in Figure **insert live data picture**.

3. Reset the GPS receiver to its default settings, as seen in Figure **insert resetdefaults**.

As shown in Section 6.1.3.1 of the user manual, load the base station's F9P configuration file into the GPS units memory:

4. In the View menu, select "Generation 9 Configuration View"
5. Select the "Advanced Configuration" sidebar item in the Generation 9 Configuration View window.
6. Click the "Load" Button on the right hand side of the screen.
7. Select the "F9P Base config C99.txt" file from the configuration folder you downloaded in **insert step 1 reference** and click "Send".  Note, this configuration file is at `.\GCC_Ublox_GPSRTK_Config\ublox-C099_F9P-uCS-master\zed-f9p\F9P Base config C99.txt` within the configurations folder.

> A video showing steps 4-7 is located at **insert video**

> The settings which have just been uploaded to the board setup the pipeline for sending RTCM correction data.  However, no data will flow from the F9P to the ODIN until we enable the Survey_In functionality of the base station. For this reason, we enter the following settings:

8. Again, in the View menu of U-Center, select the "Generation 9 Configuration View" and then go to the "Advanced Configuration" sidebar item.
9. In the left scroll window, scroll down and expand the `CFG-TMODE` section.
10. Select the `CFG-TMODE-MODE` option, and then use the "Modify" tool on the right hand side of the window to set the value to `1` for "SURVEY_IN", and add this to the flash layer so that this change will be stored in non-volitile memory.  This option enables the base station's "Survey In" feature, which allows the base station to determine it's own reference point from which it will derive GPS errors and subsequent correction information.
11. Now select the `CFG-TMODE-SVIN_MIN_DUR` and set its value to `60` and add this to the flash layer as well.  This tells the base station to wait at least 60 seconds before beginning to send correction data.  
12. Now select the `CFG-TMODE-SVIN_ACC_LIMIT` and set its value to `50000`.  Add this to the flash layer as well.  This sets threshold on the GPS location standard deviation which must be met before correction data will be sent to the rover.
13. Remember to press the SEND button before closing this window to upload these settigns to the GPS receiver!

To recap steps 10-12, we updated the following settings:
``
Flash CFG-TMODE-MODE       1                    # write value 1 - SURVEY_IN        to item id 20030001 in layer 0
Flash CFG-TMODE-SVIN_MIN_DUR 0x3c                 # write value 60  0x3c             to item id 40030010 in layer 0
Flash CFG-TMODE-SVIN_ACC_LIMIT 0xc350               # write value 50000  0xc350        to item id 40030011 in layer 0
``

A video showing these steps is located at **insert video 2**.

> Note, if you wanted the base station to use a fixed location (bypassing the base station's survey-in feature, you would not complete steps 8- **insert stop step)**

> You can check that your configuration changes to the Base Station's F9P unit have been successful by going to "View > Messages View" in the U-Center window menu, and then using the left sidebar to view the `UBX-NAV-SVIN` message.  In Figure **insert svin**, we can see that the Survey In process has begun but that even though it's been running for almost 400 seconds, its solution is not valid because the mean standard deviation of the gps solutions is almost 30 meters, which is above the threshold we set in step 12. 

The GPS Receiver Base Station should now be good to go!


# Rover Setup

## Flash the Rover ODIN-W2 with new Firmware.
Please follow the "Flash new firmware to the Base Station's ODIN W2 Unit" section above since flashing firmware to the ODIN-W2 is an identical process for both the rover and the base station.  (The purpose of flashing new firmware is to reset the ODIN-W2 to a known state).  Stop following the base station guide when you reach the end of the section, before loading text configuration files onto the unit.

## ODIN Rover Configuration
In this section, we have just flashed new firmware to the rover's ODIN W2 module, resetting it to its factory defaults.  We will now load a configuration file to it which will allow it to receive correction data from the base station.  This section will also setup the rover GPS development board to put out its own WiFi network, to which the base station will connect.

Begin with the rover gps development board plugged into your laptop with a USB cable.

1. Open S-Center and connect to the rover with the settings shown in figure **insert rover s-center**, replacing `COM8` with the COM port of your rover's ODIN module. Note: you may need to use the "Refresh COM Ports" button if you do not see a COM port for your ODIN module.
2. "File Menu" in S-Center.
3. Click "Download Configuration" and navigate to the `Rover ODIN-W2 Access Point UDP Server.txt` file within the configuration folder you downloaded in **insert download step reference**.  Within the Configuration folder, this text file is located at `.\GCC_Ublox_GPSRTK_Config\ublox-C099_F9P-uCS-master\odin-w2\Rover ODIN-W2 Access Point UDP Server.txt`,
4. Once this file is selected, click the "Open" button to load these settings onto your ODIN W2 module.
5. Connect the ODIN to the F9P unit by placing a jumper in position `30E`. See Figure **insert 3oe**.
7. You'll know that you performed this section correctly when you see a "UBXWifi" wifi network appear.
6. Continue with next section "Rover F9P Configuration"


## Rover F9P Configuration
In this step, we configure the Rover gps development board's F9P module to receive RTCM corrections from the rover's ODIN-W2 Module.
1. Begin with the rover's gps development board connected to your laptop over USB.
2. Open U-Center and connect to the Rover GPS unit by selecting "Receiver > COM15", replacing `COM15` with the COM port of your board. (remember that you may have to try several COM ports and see which one spits out GPS data.)
3. Reset the GPS Receiver by clicking the button shown in Figure **insert reset figure**.

Much the same as with the base station F9P configuration, flash the f9p configuration to the GPS as follows:

4. In the View menu, select "Generation 9 Configuration View"
5. Select the "Advanced Configuration" sidebar item in the Generation 9 Configuration View window.
6. Click the "Load" Button on the right hand side of the screen.
7. Select the "F9P Rover config C99.txt" file from the configuration folder you downloaded in **insert step 1 reference** and click "Send".  Note, this configuration file is at `.\GCC_Ublox_GPSRTK_Config\ublox-C099_F9P-uCS-master\zed-f9p\F9P Rover config C99.txt` within the configurations folder.
8. Restart the rover GPS by pressing the RESET button.


# Test
* Go outside, plug the Base station into a battery pack.  Give it several minutes to survey in.
* Take your laptop and use U-Connect to connect to the rover GPS unit.  See if you can get a `DGNSS/RTK/Fixed` Solution!

# List of Terms
* RTCM: Correction data which is sent from the GPS Base station to the Rover Module in order to improve the accuracy of the Rover's location solution.
