
# Flashing a ODIN W2[]()

Today I will update the firmware on the second GPS unit.

<<<<<<< HEAD
1. Once Again, see Section 7.2 instructions here: [https://www.u-blox.com/sites/default/files/C099-F9P-AppBoard-ODIN-W2-CSW\_UserGuide\_%28UBX-18055649%29.pdf][2]
2. Download latest u-blox connectivity software and related documentation here: [https://www.u-blox.com/en/product/odin-w2-series][3]
3. Make sure that you have the stm32flash tool from here: [https://sourceforge.net/projects/stm32flash/][4]
=======
1. Once Again, see Section 7.2 instructions here: [https://www.u-blox.com/sites/default/files/C099-F9P-AppBoard-ODIN-W2-CSW\_UserGuide\_%28UBX-18055649%29.pdf][1]
2. Download latest u-blox connectivity software and related documentation here: [https://www.u-blox.com/en/product/odin-w2-series][2]
3. Make sure that you have the stm32flash tool from here: [https://sourceforge.net/projects/stm32flash/files/stm32flash-0.5-win64.zip/download][3]
>>>>>>> 1098f8e7591c763e574b6fec8d746373ab59bd11
4. Place the ODIN w2 in safeboot mode with jumper as detailed in the the Section 7.2 instructions.
5. This part is not well documented in the instructions, I’ve copied the `stm32flash` tool into the same directory as the downloaded firmware.  See here: ￼![][image-1]. 
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

	> You can check to see which com port the ODIN is on by using the “Open Port” window’s `Refersh COM Ports` button as seen here: ![][image-2]

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
* If you cannot connect in step 10 with the setting shown in **img8.png**, try connecting pressing the pink button in **img5.png**.  Then you should be able to connect with the settings in **img8.png** before continuing with step 10.
* In my experience, after not being able to connect with the settings shown in **img8.png** during step 10, I attempted to connect with the settings shown in **img11.png** and those worked.  In this case, I continued with step 11 after connecting.

[1]:	https://www.u-blox.com/sites/default/files/C099-F9P-AppBoard-ODIN-W2-CSW_UserGuide_%28UBX-18055649%29.pdf
[2]:	https://www.u-blox.com/en/product/odin-w2-series
[3]:	https://sourceforge.net/projects/stm32flash/files/stm32flash-0.5-win64.zip/download

[image-1]:	https://media.githubusercontent.com/media/gcc-ant-robot/gps-rtk/master/notebook/imgs/img6.png
[image-2]:	https://media.githubusercontent.com/media/gcc-ant-robot/gps-rtk/master/notebook/imgs/img7.png
