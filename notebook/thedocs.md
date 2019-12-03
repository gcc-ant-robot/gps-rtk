# Table of Contents
- [Sept 12](#sept-12)
	- [Goals and Requirements](#goals-and-requirements)
		- [Troubleshooting](#troubleshooting)
- [Working GPS RTK](#working-gps-rtk)
	- [RTK Float vs. RTK Fixed](#rtk-float-vs.-rtk-fixed)
- [Base Station Auto Survey in](#base-station-auto-survey-in)




# Sept 12
<a name="sept-12"></a>

1. Following the getting started guide in ../documentation/
2. Downloaded and installed [https://www.u-blox.com/en/product/u-center][1]
\3. 



## Goals and Requirements
<a name="goals-and-requirements"></a>
**GOAL: **  Use one of our C099-F9P Boards to stream correction data to the other board in a way that could scale to streaming data to multiple boards (multiple rovers).
* 1:N Base station to rovers
* Long range - say 300 feet ish.

From the product description: 
> The C099-F9P application board allows efficient evaluation of ZED-F9P, the u-blox F9 high precision positioning module. The ZED-F9P GNSS module provides multi-band GNSS and comes with built-in RTK technology providing centimeter level accuracy to users. The C099-F9P application board integrates the ZED-F9P module and includes an ODIN-W2 short range module for connectivity options. The application board is designed to support evaluation of the most common use cases. T**he feature set supports using two C099-F9P application boards operating as Rover and Base**, where the two boards communicate over a direct Wi-Fi connection. Another supported use case is **pairing a mobile phone running an NTRIP client to the C099-F9P** application board using Bluetooth. The evaluation software, u-center, provides a powerful platform for evaluation of u-blox GNSS receivers. With u-center, data can be logged as well as visualized in real time. The u-center software contains an NTRIP server/client which can be used to manage the **RTCM** correction stream from/to a C099-F9P application board. [[] https://www.u-blox.com/sites/default/files/C099-F9P-AppBoard\_ProductSummary\_%28UBX-18022364%29.pdf ][1][2]


Notes: This section shows how the ZED-F9P is used as a rover using correction information provided over the
internet using NTRIP. This is usually provided by a host from a single reference station or as a Network
RTK Virtual Reference Service (VRS). 

There are two ways to get RTCM data to the rover C099-F9P:
1. You can either direct stream from another C099-F9P over WiFi. See page 21 of the C099-F9P User Guide (it’s in the documentation folder)
	> Can this method scale to multiple roving C099-F9P units?
2. You can connect your Roving C099-F9P to a NTRIP Client.  (This could be a computer with u-center over USB or an android phone over bluetooth).  See Page 19 of [https://www.u-blox.com/sites/default/files/C099-F9P-AppBoard-ODIN-W2-CSW\_UserGuide\_%28UBX-18055649%29.pdf][3]

I’m following the setup on page 21 of the C099-F9P user guide (stream RTCM data to the rover over wifi).

See `./imgs/img0.png`: ![./imgs/img0.png][image-1] \<- I’m having trouble connecting to the board’s serial console with s-connect.
* Actually, I’m having this exact issue: [https://portal.u-blox.com/s/question/0D52p00008HKEEDCA5/cannot-get-the-odinw2-on-c099f9p-into-at-mode-using-scenter][4]
> * Picking up here, I’ll follow the guide to update the firmware on thre board.
> 

> **See `./Sept 26.md` for more complete instructions on upgrading the ODIN W2’s firmware.**

We need to update the Odin-w2 firmware to place it in WiFi mode.  I’m following section 7.2 here: [https://www.u-blox.com/sites/default/files/C099-F9P-AppBoard-ODIN-W2-CSW\_UserGuide\_%28UBX-18055649%29.pdf][5]

￼See `./imgs/img1.png` for the solution: 

> 87YJ (Customer)
> 5 months ago
> I know this thread is old, but if it's any help. When you get the +++ and blick\_led.... that's a sign that the board is running the MBED firmware. I dont think that MBED responds to AT commands. It has its own set of commands and the system is trying to tell you what commands are available. To get AT command responses, follow the instructions in the C099 ODIN-W2 connectivity software to update the ODIN-W2 the firmware over to the AT command based native FW and then you can get proper responses from the AT commands. Here's a link to the manual: https://www.u-blox.com/sites/default/files/C099-F9P-AppBoard-ODIN-W2-CSW\_UserGuide_%28UBX-18055649%29.pdf_
> [https://portal.u-blox.com/s/question/0D52p00008HKE8jCAH/how-to-connect-odinw2-on-c099f9p-via-bluetooth-with-mobile][6]

So we need to uninstall the MBED firmware by refreshing with native firmware.  I’m following section “7.2 ODIN-W2 firmware update” here: [https://www.u-blox.com/sites/default/files/C099-F9P-AppBoard-ODIN-W2-CSW\_UserGuide\_%28UBX-18055649%29.pdf][7]

* Here’s the firmware download site: [https://www.u-blox.com/en/product/odin-w2-series#tab-documentation-resources][8]
* Jumper placed across `SAFEB ODIN`.
* USB cable connected (power on C099-F9P)
* See `imgs/img2.png`!  I copied the stm32 flasher tool into the download directory of the firmware update. 
	* We first upload a boot loader... 
	* The file that you want to flash **is not** `ODIN-W26X-SW-7.1.0-020.bin ` but rather, you need to `cd` into the `Bootloader - only needed for recovery` directory and then use the `ODIN-W2-BOOT-v0.8.2.bin ` binary!  
	* Here’s my command output: 
	```python
		PS C:\Users\theostangebye\Downloads\ODIN-W26X-7\Bootloader - only needed for recovery> ..\stm32flash.exe -b 115200 -w .\ODIN-W2-BOOT-v0.8.2.bin -s 0x000000 COM4
		stm32flash 0.5

		http://stm32flash.sourceforge.net/

		Using Parser : Raw BINARY
		Interface serial_w32: 115200 8E1
		Version      : 0x31
		Option 1     : 0x00
		Option 2     : 0x00
		Device ID    : 0x0419 (STM32F42xxx/43xxx)
		- RAM        : 192KiB  (12288b reserved by bootloader)
		- Flash      : 2048KiB (size first sector: 1x16384)
		- Option RAM : 65552b
		- System RAM : 30KiB
		Write to memory
		Erasing memory
		Wrote address 0x08002914 (100.00%) Done.

		PS C:\Users\theostangebye\Downloads\ODIN-W26X-7\Bootloader - only needed for recovery>
	```
* And then we upload the actual firmware update - following the instructions in section 7.2:
```python
	PS C:\Users\theostangebye\Downloads\ODIN-W26X-7> .\stm32flash.exe -b 115200 -w .\ODIN-W26X-SW-7.1.0-020.bin -S 0x8010000 COM4
	stm32flash 0.5

	http://stm32flash.sourceforge.net/

	Using Parser : Raw BINARY
	Interface serial_w32: 115200 8E1
	Version      : 0x31
	Option 1     : 0x00
	Option 2     : 0x00
	Device ID    : 0x0419 (STM32F42xxx/43xxx)
	- RAM        : 192KiB  (12288b reserved by bootloader)
	- Flash      : 2048KiB (size first sector: 1x16384)
	- Option RAM : 65552b
	- System RAM : 30KiB
	Write to memory
	Erasing memory
	Wrote address 0x08197338 (100.00%) Done.

	PS C:\Users\theostangebye\Downloads\ODIN-W26X-7>
```

* Note that that is a capital `-S`!
* Following the instructions, I was able to connect with the settings seen in `imgs/img4.png` and then click on the button shown in `imgs/img5.png` before applying the settings shown in `imgs/img3.png`.

> We should now be able to download configurations to the C099-F9P.  Next time, I’ll flash the other unit, and then set one up to be the rover and the base station.




Today I will update the firmware on the second GPS unit.

1. Once Again, see Section 7.2 instructions here: [https://www.u-blox.com/sites/default/files/C099-F9P-AppBoard-ODIN-W2-CSW\_UserGuide\_%28UBX-18055649%29.pdf][9]
2. Download latest u-blox connectivity software and related documentation here: [https://www.u-blox.com/en/product/odin-w2-series][10]
3. Make sure that you have the stm32flash tool from here: [https://sourceforge.net/projects/stm32flash/][11]
4. Place the ODIN w2 in safeboot mode with jumper as detailed in the the Section 7.2 instructions.
5. This part is not well documented in the instructions, I’ve copied the `stm32flash` tool into the same directory as the downloaded firmware.  See here: ￼![][image-2]. 
6. Now open up a powershelgl prompt and go to the `ODIN-W26X-7` Directory.  For me, that is in Downloads:
	```bash
	PS C:\Windows\System32\WindowsPowerShell\v1.0> cd 'C:\Users\theostangebye\Downloads\ODIN-W26X-7\'                      
	PS C:\Users\theostangebye\Downloads\ODIN-W26X-7> ls


		Directory: C:\Users\theostangebye\Downloads\ODIN-W26X-7


	Mode                LastWriteTime         Length Name
	----                -------------         ------ ----
	d-----        9/19/2019   2:05 PM                Bootloader - only needed for recovery
	-a----         9/9/2019   3:34 PM         102242 ODIN-W2-SW7-1-0_ReleaseNotes_(UBX-19041417).pdf
	-a----        8/27/2019  11:53 AM        1602360 ODIN-W26X-SW-7.1.0-020.bin
	-a----        2/10/2016   5:14 PM         252776 stm32flash.exe


	PS C:\Users\theostangebye\Downloads\ODIN-W26X-7>
	```
7. Now flash the bootloader with this command: `.\stm32flash.exe -b 115200 -w '.\Bootloader - only needed for recovery\\ODIN-W2-BOOT-v0.8.2.bin' -s 0x000000 COM11`.  Notice that my ODIN is on `COM11`. This could be different for you.  See image and note below for deciding which COM port the ODIN is on.  Output of command here:
	```bash
	PS C:\Users\theostangebye\Downloads\ODIN-W26X-7> .\stm32flash.exe -b 115200 -w '.\Bootloader - only needed for recovery\\ODIN-W2-BOOT-v0.8.2.bin' -s 0x000000 COM11
	stm32flash 0.5

	http://stm32flash.sourceforge.net/

	Using Parser : Raw BINARY
	Interface serial_w32: 115200 8E1
	Version      : 0x31
	Option 1     : 0x00
	Option 2     : 0x00
	Device ID    : 0x0419 (STM32F42xxx/43xxx)
	- RAM        : 192KiB  (12288b reserved by bootloader)
	- Flash      : 2048KiB (size first sector: 1x16384)
	- Option RAM : 65552b
	- System RAM : 30KiB
	Write to memory
	Erasing memory
	Wrote address 0x08002914 (100.00%) Done.
	```
8. Finally, flash the software update with the following command:
	`.\stm32flash.exe -b 115200 -w .\ODIN-W26X-SW-7.1.0-020.bin -S 0x8010000 COM11`
	Here’s the output of this command. (Below)  Notice that for me, the Odin was on `COM11`!  This could be different for you.

	> You can check to see which com port the ODIN is on by using the “Open Port” window’s `Refersh COM Ports` button as seen here: ![][image-3]

	```bash
	PS C:\Users\theostangebye\Downloads\ODIN-W26X-7> .\stm32flash.exe -b 115200 -w .\ODIN-W26X-SW-7.1.0-020.bin -S 0x8010000 COM11
	stm32flash 0.5

	http://stm32flash.sourceforge.net/

	Using Parser : Raw BINARY
	Interface serial_w32: 115200 8E1
	Version      : 0x31
	Option 1     : 0x00
	Option 2     : 0x00
	Device ID    : 0x0419 (STM32F42xxx/43xxx)
	- RAM        : 192KiB  (12288b reserved by bootloader)
	- Flash      : 2048KiB (size first sector: 1x16384)
	- Option RAM : 65552b
	- System RAM : 30KiB
	Write to memory
	Erasing memory
	Wrote address 0x08197338 (100.00%) Done.
	```
9. Remove safe boot jumper and press `RESET` button on GPS Unit.
10. You should now be able to connect to the ODIN using the settings shown here in s-connect: **img8.png**
11. In **img9.png**, you can see that I am successfully connected and communicating with the ODIN with AT commands.
12. Run the commands sequentially shown in **img10.png**, you’ll see that the device powers off and restarts with a square character.  This is because we told the unit to now communicate at 460800 baud.
13. Reconnect to the ODIN with the settings seen in **img11.png** to successfully reconnect and log back into the AT terminal.
14. Done!  See the successful AT messages in **img12.png**

### Troubleshooting
<a name="troubleshooting"></a>
* If you cannot connect in step 10 with the setting shown in **img8.png**, try connecting pressing the pink button in **img5.png**.  Then you should be able to connect with the settings in **img8.png** before continuing with step 10.
* In my experience, after not being able to connect with the settings shown in **img8.png** during step 10, I attempted to connect with the settings shown in **img11.png** and those worked.  In this case, I continued with step 11 after connecting.


> Just upgraded firmware - continuing with section 6.1 in the C099-F9P User guide (page 21 of 49)

1. See [3.1.5 RTK configuration][12] for detailed instructions on flashing data to GPS receiver.

￼￼￼￼￼Here: we see that survey in has not begun: ￼￼￼￼￼

Oct 22

# Working GPS RTK
<a name="working-gps-rtk"></a>

1. Plug base station into DC Power jack
2. Flash basestation start configuration from u-center
3. Disconnect usb from base station recie3ver
4. Plug in rover receiver.  
5. ￼￼Verify that `3D/DGNSS/FLOAT` message is seen in the rover’s `Fix Mode` window.


> Useful for verification: - battery power for rover?
> Would be clutch if we could see there rover’s position from the base station.

## RTK Float vs. RTK Fixed
<a name="rtk-float-vs.-rtk-fixed"></a>
It seems that a RTK fixed solution is generally more accurate and desirable than the RTK float solution.  
\* if the distance between the two radios is not very large, try waiting or warm starting the rover to obtain a RTK Fixed solution.  
	\* (I restarted my rover and went from RTK float to RTK fixed)

# Base Station Auto Survey in
<a name="base-station-auto-survey-in"></a>

With the current implementation, the Base station’s F9P unit has already had it’s settings flashed with the base station RTK configuration (located at [F9P Base config C99.txt][13]).  All of these settings were stored in Flash on the gps.  However, the user still needs to flash the survey in start commands to the base station every time it is turned on.  (This is because the [F9P Base Survey in start.txt][14] stores it’s settings in RAM). 

In order to make the base station so that the user can simply plug it in and let it begin the survey in itself, I’ve created an alternative to the `F9P Base Survey in start.txt` file, which is located here: [https://github.com/gcc-ant-robot/gps-rtk/blob/master/code/BaseStationPermanentSurveyIn.txt][15] or in this repository at `/code/`.

This has been flashed to the base station’s F9P unit so that it automatically goes in to survey in mode when plugged in.

[1]:	https://www.u-blox.com/en/product/u-center
[2]:	https://www.u-blox.com/sites/default/files/C099-F9P-AppBoard_ProductSummary_%28UBX-18022364%29.pdf
[3]:	https://www.u-blox.com/sites/default/files/C099-F9P-AppBoard-ODIN-W2-CSW_UserGuide_%28UBX-18055649%29.pdf
[4]:	https://portal.u-blox.com/s/question/0D52p00008HKEEDCA5/cannot-get-the-odinw2-on-c099f9p-into-at-mode-using-scenter
[5]:	https://www.u-blox.com/sites/default/files/C099-F9P-AppBoard-ODIN-W2-CSW_UserGuide_%28UBX-18055649%29.pdf
[6]:	https://portal.u-blox.com/s/question/0D52p00008HKE8jCAH/how-to-connect-odinw2-on-c099f9p-via-bluetooth-with-mobile
[7]:	https://www.u-blox.com/sites/default/files/C099-F9P-AppBoard-ODIN-W2-CSW_UserGuide_%28UBX-18055649%29.pdf
[8]:	https://www.u-blox.com/en/product/odin-w2-series#tab-documentation-resources
[9]:	https://www.u-blox.com/sites/default/files/C099-F9P-AppBoard-ODIN-W2-CSW_UserGuide_%28UBX-18055649%29.pdf
[10]:	https://www.u-blox.com/en/product/odin-w2-series
[11]:	https://sourceforge.net/projects/stm32flash/
[12]:	https://www.u-blox.com/en/docs/UBX-18010802#%5B%7B%22num%22%3A260%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22XYZ%22%7D%2C59.527%2C680.077%2Cnull%5D "3.1.5 RTK configuration"
[13]:	https://github.com/u-blox/ublox-C099_F9P-uCS/blob/master/zed-f9p/F9P%20Base%20config%20C99.txt "F9P Base config C99.txt"
[14]:	https://github.com/u-blox/ublox-C099_F9P-uCS/blob/master/zed-f9p/F9P%20Base%20Survey%20in%20start.txt "F9P Base Survey in start.txt"
[15]:	https://github.com/gcc-ant-robot/gps-rtk/blob/master/code/BaseStationPermanentSurveyIn.txt

[image-1]:	https://media.githubusercontent.com/media/gcc-ant-robot/gps-rtk/master/notebook/imgs/img0.png
[image-2]:	https://media.githubusercontent.com/media/gcc-ant-robot/gps-rtk/master/notebook/imgs/img6.png
[image-3]:	https://media.githubusercontent.com/media/gcc-ant-robot/gps-rtk/master/notebook/imgs/img7.png
