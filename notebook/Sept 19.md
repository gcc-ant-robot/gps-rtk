
> **See `./Sept 26.md` for more complete instructions on upgrading the ODIN W2’s firmware.**

We need to update the Odin-w2 firmware to place it in WiFi mode.  I’m following section 7.2 here: [https://www.u-blox.com/sites/default/files/C099-F9P-AppBoard-ODIN-W2-CSW\_UserGuide\_%28UBX-18055649%29.pdf][1]

￼See `./imgs/img1.png` for the solution: 

> 87YJ (Customer)
> 5 months ago
> I know this thread is old, but if it's any help. When you get the +++ and blick\_led.... that's a sign that the board is running the MBED firmware. I dont think that MBED responds to AT commands. It has its own set of commands and the system is trying to tell you what commands are available. To get AT command responses, follow the instructions in the C099 ODIN-W2 connectivity software to update the ODIN-W2 the firmware over to the AT command based native FW and then you can get proper responses from the AT commands. Here's a link to the manual: https://www.u-blox.com/sites/default/files/C099-F9P-AppBoard-ODIN-W2-CSW\_UserGuide_%28UBX-18055649%29.pdf_
> [https://portal.u-blox.com/s/question/0D52p00008HKE8jCAH/how-to-connect-odinw2-on-c099f9p-via-bluetooth-with-mobile][2]

So we need to uninstall the MBED firmware by refreshing with native firmware.  I’m following section “7.2 ODIN-W2 firmware update” here: [https://www.u-blox.com/sites/default/files/C099-F9P-AppBoard-ODIN-W2-CSW\_UserGuide\_%28UBX-18055649%29.pdf][3]

* Here’s the firmware download site: [https://www.u-blox.com/en/product/odin-w2-series#tab-documentation-resources][4]
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



[1]:	https://www.u-blox.com/sites/default/files/C099-F9P-AppBoard-ODIN-W2-CSW_UserGuide_%28UBX-18055649%29.pdf
[2]:	https://portal.u-blox.com/s/question/0D52p00008HKE8jCAH/how-to-connect-odinw2-on-c099f9p-via-bluetooth-with-mobile
[3]:	https://www.u-blox.com/sites/default/files/C099-F9P-AppBoard-ODIN-W2-CSW_UserGuide_%28UBX-18055649%29.pdf
[4]:	https://www.u-blox.com/en/product/odin-w2-series#tab-documentation-resources