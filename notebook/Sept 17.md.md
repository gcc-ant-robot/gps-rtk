
## Goals and Requirements
**GOAL: **  Use one of our C099-F9P Boards to stream correction data to the other board in a way that could scale to streaming data to multiple boards (multiple rovers).
* 1:N Base station to rovers
* Long range - say 300 feet ish.

From the product description: 
> The C099-F9P application board allows efficient evaluation of ZED-F9P, the u-blox F9 high precision positioning module. The ZED-F9P GNSS module provides multi-band GNSS and comes with built-in RTK technology providing centimeter level accuracy to users. The C099-F9P application board integrates the ZED-F9P module and includes an ODIN-W2 short range module for connectivity options. The application board is designed to support evaluation of the most common use cases. T**he feature set supports using two C099-F9P application boards operating as Rover and Base**, where the two boards communicate over a direct Wi-Fi connection. Another supported use case is **pairing a mobile phone running an NTRIP client to the C099-F9P** application board using Bluetooth. The evaluation software, u-center, provides a powerful platform for evaluation of u-blox GNSS receivers. With u-center, data can be logged as well as visualized in real time. The u-center software contains an NTRIP server/client which can be used to manage the **RTCM** correction stream from/to a C099-F9P application board. [[] https://www.u-blox.com/sites/default/files/C099-F9P-AppBoard\_ProductSummary\_%28UBX-18022364%29.pdf ][1][1]


Notes: This section shows how the ZED-F9P is used as a rover using correction information provided over the
internet using NTRIP. This is usually provided by a host from a single reference station or as a Network
RTK Virtual Reference Service (VRS). 

There are two ways to get RTCM data to the rover C099-F9P:
1. You can either direct stream from another C099-F9P over WiFi. See page 21 of the C099-F9P User Guide (it’s in the documentation folder)
	> Can this method scale to multiple roving C099-F9P units?
2. You can connect your Roving C099-F9P to a NTRIP Client.  (This could be a computer with u-center over USB or an android phone over bluetooth).  See Page 19 of [https://www.u-blox.com/sites/default/files/C099-F9P-AppBoard-ODIN-W2-CSW\_UserGuide\_%28UBX-18055649%29.pdf][2]

I’m following the setup on page 21 of the C099-F9P user guide (stream RTCM data to the rover over wifi).

See `./imgs/img0.png` \<- I’m having trouble connecting to the board’s serial console with s-connect.
* Actually, I’m having this exact issue: [https://portal.u-blox.com/s/question/0D52p00008HKEEDCA5/cannot-get-the-odinw2-on-c099f9p-into-at-mode-using-scenter][3]
> * Picking up here, I’ll follow the guide to update the firmware on thre board.

[1]:	https://www.u-blox.com/sites/default/files/C099-F9P-AppBoard_ProductSummary_%28UBX-18022364%29.pdf
[2]:	https://www.u-blox.com/sites/default/files/C099-F9P-AppBoard-ODIN-W2-CSW_UserGuide_%28UBX-18055649%29.pdf
[3]:	https://portal.u-blox.com/s/question/0D52p00008HKEEDCA5/cannot-get-the-odinw2-on-c099f9p-into-at-mode-using-scenter