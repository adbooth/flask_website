# Natural Light Alarm Clock
###### By Seth Karas & Andrew Booth
---
#### Why/What?
We choose to pursue an energy efficient, light-based alarm clock for the deaf or hard-of-hearing persons.  There are a variety of vibration-based alarm clock to wake up people who are hard of hearing.  After researching, the vibration-based alarms are typically embedded into head pillows.  If the user is not laying right on, or near the vibration device in the pillow, they become unreliable.
Also, we targeted this device towards elderly or bed-ridden patients.  It would offer these patients or individuals more freedom to control their surrounds.  The attached, wired switch acts a user control for the device giving the user full control to open or close the blinds.  This could also be used in skylight applications in homes and businesses.  With this information at hand, we choose to seek out a more reliable, helpful device.
We decided to utilize natural light to help awaken these individuals.  The device can be programmed like any other alarm clock, but instead of having a buzzer, playing music, or vibrating, our alarm opens the blinds in the room to allow natural light to enter.  It could be used on its own or in combination with previously stated alarms.

#### How:
Using an Arduino UNO as our control system, we utilize a DC Gearmotor as a winch to lift or lower the blinds.  The gearmotor is attached directly to the window frame.  Limit switches are used to control the top and bottom heights.  They can be adjusted to alter the range that the blinds can travel.  Another external, wired switch is attached and acts as a user control to lower or raise the blinds.  Other options would be to include a wireless breakout board to the Arduino to allow for an app-based control sub-system.

#### Usage:
The system is ready for use on startup. A short click to the button will lower the blinds if they are not already at the top or bottom. Otherwise, a short click will toggle the blinds between open and closed.
When a user wants to set a timer for the blinds to open, the user must hold down the button for 3 seconds. The light will flash quickly 3 times, meaning the system is now in programming mode which lasts for 1 minute. The user can now short click the button to increment the number of hours on the timer, and then hold down the button again for three seconds to exit programming mode. Exit is also confirmed by 3 quick flashes of the light.
After the timer is set, the user is still free to lower and raise the blinds as he/she wishes. The user can also cancel the timer by holding the button down for 3 seconds, confirmed by 3 quick flashes of the light.


#### Trials/Testing:
We performed three rounds of tests on the device.  Each round, the opening and closing of the blinds was controlled by either the Arduino code, or by using the external, user activated switch.  The results of each test were recorded. A failure in the operation of the device was recorded, but not adjusted until the round of test was complete. The only adjustments that had to be made were in the bottom limit switch.   The blinds were not always heavy enough to trigger the pressure activated switch.  Knowing that our motor was being utilized to about 4% of its total lifting capacity based on the types of blinds we were using for testing, we added small weights to the bottom of the blind to increase its chance of depressing the switch.  The test data can be found below.

#### Testing Results
1. Round 1
    - 18 of 20 successful (90%)
2. Round 2
    - 20 of 20 successful (100%)
3. Round 3
    - 20 of 20 successful (100%)

#### Components:
- (3) Low-Pressure normally open switched
    - (2) Mounted directly to window frame assembly
    - (1) For user control switch
- (1) Arduino UNO
    - Or other programmable IC
- (1) DC Power Supply
    - 6-12 Volts
    - Power-Sonic 6V - Sealed Lead Acid Battery - Model PS-640-F1
- (1) 6-12 Volt DC Gearmotor
    - Torque rating at least double the weight of the window blind
    - Hennkwell - 12V DC Gearmotor - PK32D210C-06
- (1) 1/4W Carbon Film Resistors
    - (2) 220 Ohm for current control on Arduino Digital Inputs
- (1) Electromechanical Relay
    - 3-5V Control Coil, 2Amp MAX DC Normally-Open Output
    - KEST - KS2E-M-DC3
