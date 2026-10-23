# MoonShine
## Updated Oct 23, 2026
<img src="/others/moonshine_logo.png" width=50% height=50%>

MoonShine is a suite of software tools and electronic hardware for predicting moonlight (and/or twilight and sunlight) ground illuminance and for re-creating moonlight cycles in a laboratory environment using LED arrays. MoonShine is designed for field and experimental ecologists, chronobiologists, visual biologists, and physiologists. MoonShine also predicts and re-creates sunlight, making it a one-stop solution for creating full natural diel light cycles or for manipulating light cycles in a range of animal husbandry and experimental scenarios.

## Predict ground illuminance using the MoonShineR R package
The **MoonShineR R package** is available through CRAN and should be installed directly from R.

### Install and run
1.	Install MoonShineR in R using:
`install.packages("MoonShineR")`
Alternatively, in RStudio, search for MoonShineR in the Packages tab and click Install.

2.	Load the MoonShineR package:
`library(MoonShineR)`

3.	Consult the R documentation for the two main MoonShineR functions and try running the examples:
- `?MoonShineR::predict_lux` for predicting ground illuminance.
- `?MoonShineR::plot_lux for` plotting the predicted illuminance.
- 
**CRAN documentation:** https://cran.r-project.org/package=MoonShineR
  
**Source code repository:** https://github.com/Crampton-Lab/MoonShineR_package

### Re-create light regimes using LED arrays for experiments:
The **MoonShineR moonlight and sunlight/twilight scheduler scripts**, which generate LED control schedules for use with MoonShineP, remain available in this GitHub repository. These provide additional functionality not included in the CRAN R package.

The stand-alone MoonShineR scheduler scripts generate light schedules that are read by MoonShineP, a Python program running on a Raspberry Pi that controls the LED arrays.

This GitHub repository contains the files required for experimental light re-creation, as listed below.

#### Files for creating a light regime schedule table during the preparation phase (run on any personal computer)

##### The two stand-alone MoonShineR scheduler scripts:
- `moonshineR_moonlight_scheduler.R`
- `moonshineR_sunlight_twilight_scheduler.R`

##### LED spectrum preview Excel file:
- `RGBW_LED_spectrum.xlsx`

##### Manual scheduler Excel template file:
- `manual_scheduler.xlsx`

##### Files for executing the light regime (run on the Raspberry Pi that controls the LED arrays)
**The moon and sun versions of the MoonShineP Python program:**
- control_moon folder containing `moonshine_moon.py`
- control_sun folder containing `moonshine_sun.py`

##### The moon and sun versions of clear.py for turning off the LED arrays:
- `clear_moon.py`
- `clear_sun.py`

### Instruction Manual
https://lokpoon.github.io/MoonShine_manual/overview.html

### Citation
Poon, L., Jenks, I. T., & Crampton, W. G. R. (2024). MoonShine: A software-hardware system for simulating moonlight ground illuminance and re-creating artificial moonlight cycles in a laboratory environment. Methods in Ecology and Evolution. 15, 701–715. https://doi.org/10.1111/2041-210X.14299

### Technical support contact: Lok Poon (poonchiulok@gmail.com)

