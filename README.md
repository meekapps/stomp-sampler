# stomp-sampler
A Raspberry Pi powered sampler with stompbox pedal operation.

![Case](http://cdn3.volusion.com/scund.bojht/v/vspfiles/photos/options/500-1001-1345-T.jpg?1398344390)
#### 3/5/15

### Goals
* Push button operation sampler.
* Standard two-button guitar stompbox pedal form-factor.
* One-shot sample playback, queueing, stopping.
* 4+ sample storage via SD or USB.
* Visual indication (4 LED array) of which sample is queued.
* Battery operation.
* Standard 1/4" mono audio output to DI box.

### Parts
* [Raspberry Pi][pi] - *Model A+, 256 MB RAM, 3.5mm audio*

* [Power Supply][power] - *5V, 1000mA USB*

* [SD Card][sd] - *8GB, microSD+adapter, Class 10, 10Mb/s*

* Footswitches (2) *research SPST vs. DPDT vs. TPDT*

* LEDs (4+) - possibly in ascending color Green, Yellow, Orange, Red

* [AA Battery pack][aa]

* [IB4001 Diode][diode] - *Put in series to drop 4xAA alkaline from 6V to 5.3V*

* [Enclosure][enc] - *1590BB H42, 4-hole, 2-footswitch, 4.67" x 3.68" x 1.18"*

* Etc. Wire / Resistors / Capacitors, TBD.



###Milestones
1. ~~Acquire starting parts - Raspberry Pi, Power supply, SD card.~~
2. ~~Format SD card, install Raspbian on Pi.~~
3. Simple Python playback of WAV file from SD card.
4. Use mechanical switch via GPIO for playback/pause.
5. Write Python audio queue application.
6. Design circuit, order internal parts.
7. Integrate footswitch buttons with audio queue app.
8. LED indicators show queue index.
9. 1/4" audio output.
10. Battery powered operation.
11. Design enclosure and die cast drilling template.
12. Assemble enclosure.


### Resources

* [Parts list Doc][parts] - *Shared Google doc*

* [Mammoth Electronics][mammoth] - *guitar pedal parts*

* [Adafruit][ada] - *Raspberry Pi parts*

* [Octopart][octopart] - *Electronic part search engine*

* [Graphical Resistance Calculator][rescalc] - *Resistor color code lookup GUI*

* [Pi4J Project][pins] - *Raspberry Pi GPIO pins*  

* [Pyglet][pyglet] - *Python multimedia module*


[parts]:https://docs.google.com/spreadsheets/d/1p6p0Bd8CLel-TAVeZC0bcEx_INBNSggYxUmjXTRixgc/edit#gid=0
[enc]:http://www.mammothelectronics.com/4S1590BB-p/500-1001.htm
[pi]:http://www.adafruit.com/products/2266
[sd]:http://www.newegg.com/Product/Product.aspx?Item=N82E16820139532
[power]:https://www.adafruit.com/products/501
[aa]:http://www.adafruit.com/products/830
[diode]:http://www.adafruit.com/products/755
[octopart]:https://octopart.com
[rescalc]:http://www.dannyg.com/examples/res2/resistor.htm

[mammoth]:http://www.mammothelectronics.com/
[ada]:http://www.adafruit.com
[pins]:http://pi4j.com/pins/model-a-plus.html














