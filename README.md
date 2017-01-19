# stomp-sampler
A Raspberry Pi powered sampler with stompbox pedal operation.

![Case](http://cdn3.volusion.com/scund.bojht/v/vspfiles/photos/options/500-1001-1345-T.jpg?1398344390)
#### 3/5/15

### Goals 1.0
* Push button operation sampler.
* Standard two-button guitar stompbox pedal form-factor.
* One-shot sample playback, queueing, stopping.
* 4+ sample storage via SD or USB.
* Visual indication (4 LED array) of which sample is queued.
* Battery operation.
* Standard 1/4" mono audio output to DI box.

### Goals 2.0
* Base on cheaper + smaller Raspberry Pi Zero.
* 5 sample indicator LEDs.
* 1 static power LED (it was impossible to tell if it was still booting or out of batteries).
* Wall power only. Battery power was impractically short.
* Larger case, based on 4s6500 components took up entire enclosure.
* Custom drill pattern.
* Custom paint job.

### Nice-to-haves 2.0
* Direct XLR out (that would require a DI box component to balance the signal using a transformer)
* WiFi adapter + web server to add samples wirelessly.

### Parts
* [Raspberry Pi][pi] - *Model A+, 256 MB RAM, 3.5mm audio*

* [Power Supply][power] - *5V, 1000mA USB*

* [SD Card][sd] - *8GB, microSD+adapter, Class 10, 10Mb/s*

* Footswitches (2) *latching SPDT*

* LEDs (4+) - possibly in ascending color Green, Yellow, Orange, Red

* 9V Battery adapter

* Power switch

* Mono audio jacks (2)

* [Verter 5V Buck-Boost][verter] *to run 5V from 9V pack*

* [Enclosure][enc] - *1590BB H42, 4-hole, 2-footswitch, 4.67" x 3.68" x 1.18"*

* Etc. Wire / Resistors / Capacitors, TBD.


###Milestones
1. ~~Acquire starting parts - Raspberry Pi, Power supply, SD card.~~
2. ~~Format SD card, install Raspbian on Pi.~~
3. ~~Setup and connect to Pi via SSH.~~
4. ~~Simple Python audio playback of WAV file from SD card out Pi audio.~~
5. ~~Use mechanical switch via GPIO for playback.~~
6. ~~Write audio queue application (Python) with playback/pause/next controls.~~
7. ~~Figure out better way to transfer files via SD card or USB.~~
8. ~~Design circuits, order internal parts.~~
9. ~~Integrate footswitch buttons with audio queue app.~~
10. ~~LED indicators show queue index.~~
11. ~~1/4" mono audio output, sum of stereo signal.~~
12. ~~Battery powered operation.~~
13. ~~Design enclosure and die cast drilling template.~~
15. ~~Pi single, root user + sampler boot process.~~
14. ~~Assemble enclosure.~~
15. ~~Speed up boot time.~~

### Resources

* [Parts list Doc][parts] - *Shared Google doc*
* [Mammoth Electronics][mammoth] - *guitar pedal parts*
* [Adafruit][ada] - *Raspberry Pi parts*
* [Octopart][octopart] - *Electronic part search engine*
* [Graphical Resistance Calculator][rescalc] - *Resistor color code lookup GUI*
* [GPIO pins][pins] - *Raspberry Pi GPIO pins, A+ board layout*  
* [Python-Dev][pythondev] - *needed for gpio*
* [RPi GPIO][gpio] - *interface with RPi's General Purpose IO pins.*
* [omxplayer][omxplayer] - *RPi audio player*
* [Stereo to Mono][stereosum] - *Summing stereo plug to mono out.*
* [Ext FS][extfs] - *mount Raspberry Pi formatted SD card on OS X*

[enc]:http://www.mammothelectronics.com/4S1590BB-p/500-1001.htm
[pi]:http://www.adafruit.com/products/2266
[sd]:http://www.newegg.com/Product/Product.aspx?Item=N82E16820139532
[power]:https://www.adafruit.com/products/501
[diode]:http://www.adafruit.com/products/755
[rescalc]:http://www.dannyg.com/examples/res2/resistor.htm
[pythondev]:https://packages.debian.org/sid/python-dev
[gpio]:https://pypi.python.org/pypi/RPi.GPIO
[mammoth]:http://www.mammothelectronics.com/
[ada]:http://www.adafruit.com
[pins]:http://pi4j.com/pins/model-a-plus.html
[omxplayer]:http://elinux.org/Omxplayer
[stereosum]:https://brashleraudio.files.wordpress.com/2012/08/screenhunter_02-aug-27-19-35.gif
[verter]:http://www.adafruit.com/product/2190
[extfs]:http://www.paragon-software.com/home/extfs-mac

### Drill sizes
* T1-3/4 LED bezel, mini toggles - 1/4" (6mm)
* T1-3/4 LED without bezel - 3/16"(5mm)
* 16mm pot - 9/32" (7mm)
* 24mm pot - 5/16" (8mm)
* audio jacks - 3/8" (10mm)
* footswitches - 15/32" (12mm) w/o washer, 1/2" with washer
* dc power jack - 15/32" (12mm)










