# Base Station Auto Survey in 

With the current implementation, the Base station’s F9P unit has already had it’s settings flashed with the base station RTK configuration (located at [F9P Base config C99.txt][1]).  All of these settings were stored in Flash on the gps.  However, the user still needs to flash the survey in start commands to the base station every time it is turned on.  (This is because the [F9P Base Survey in start.txt][2] stores it’s settings in RAM). 

In order to make the base station so that the user can simply plug it in and let it begin the survey in itself, I’ve created an alternative to the `F9P Base Survey in start.txt` file, which is located here: [https://github.com/gcc-ant-robot/gps-rtk/blob/master/code/BaseStationPermanentSurveyIn.txt][3] or in this repository at `/code/`.

This has been flashed to the base station’s F9P unit so that it automatically goes in to survey in mode when plugged in.


[1]:	https://github.com/u-blox/ublox-C099_F9P-uCS/blob/master/zed-f9p/F9P%20Base%20config%20C99.txt "F9P Base config C99.txt"
[2]:	https://github.com/u-blox/ublox-C099_F9P-uCS/blob/master/zed-f9p/F9P%20Base%20Survey%20in%20start.txt "F9P Base Survey in start.txt"
[3]:	https://github.com/gcc-ant-robot/gps-rtk/blob/master/code/BaseStationPermanentSurveyIn.txt