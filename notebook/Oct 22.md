Oct 22

# Working GPS RTK

1. Plug base station into DC Power jack
2. Flash basestation start configuration from u-center
3. Disconnect usb from base station recie3ver
4. Plug in rover receiver.  
5. ￼￼Verify that `3D/DGNSS/FLOAT` message is seen in the rover’s `Fix Mode` window.


> Useful for verification: - battery power for rover?
> Would be clutch if we could see there rover’s position from the base station.

## RTK Float vs. RTK Fixed 
It seems that a RTK fixed solution is generally more accurate and desirable than the RTK float solution.  
* if the distance between the two radios is not very large, try waiting or warm starting the rover to obtain a RTK Fixed solution.  
	* (I restarted my rover and went from RTK float to RTK fixed)