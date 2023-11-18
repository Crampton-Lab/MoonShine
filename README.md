# MoonShine
## Updated Sep 21, 2023
<img src="/others/moonshine_logo.png" width=50% height=50%>

WEBSITE UNDER CONSTRUCTION, PENDING REVIEW OF A MANUSCRIPT.

MoonShine is a suite of tools that predicts moonlight ground illuminance and re-create moonlight cycle, useful for field and experimental ecologists.

PUT PUBLICATION INFORMATION HERE LATER
# Moonlight ground illuminance prediction:
## Install MoonShineR package:
1. Install and load library _devtools_ (aviliable on CRAN) in R.
<br/><br/>
`install.packages("devtools")`
<br/><br/>
`library(devtools)`

2. Run the folloing line in R to install MoonShineR from Crampton-Lab GitHub repository: 
`devtools::install_github("Crampton-Lab/MoonShineR_package")`
3. Restart R session:  
`.rs.restartR()`
4. Load MoonShineR library:  
`library(MoonShineR)`
5. Check out R docuentations of the two MoonShineR functions:  
`?MoonShineR::predict_lux`  
`?MoonShineR::plot_lux`
6. Also see Chapter 1 "MoonShineR package" of the online instruction manual:  https://lokpoon.github.io/MoonShine_manual/overview.html

MoonShineR pacakage GitHub repository:  
https://github.com/Crampton-Lab/MoonShineR_package
# Moonlight cycle re-creation:
See online instruction manual: https://lokpoon.github.io/MoonShine_manual/overview.html  
This current repository hosts the files mentioned in this manual. The following is a checklist of the files provided.
## Files that run on the computer
### The two versions of MoonShineR scheduler R program:
- `moonshineR_moonlight_scheduler.R`
- `moonshineR_sunlight_twilight_scheduler.R`
### LED spectrum preview excel file:
- `RGBW_LED_spectrum.xlsx`
### Manual scheduler excel template file:
- `manual_scheduler.xlsx`
## Files that run on the Raspberry Pi
### The moon and sun versions of MoonShineP Python program:
- control_moon folder containing `moonshine_moon.py`
- control_sun folder containing `moonshine_sun.py`
### The moon and sun versions of `clear.py` for turnning off the LED arrays:
- `clear_moon.py`
- `clear_sun.py`
