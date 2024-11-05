# MoonShine
## Updated Feb 1, 2024
<img src="/others/moonshine_logo.png" width=50% height=50%>

MoonShine is a suite of software tools and electronic hardware for predicting moonlight ground illuminance and for re-creating moonlight cycles in a laboratory environment using LED arrays. MoonShine is designed for field and experimental ecologists, chronobiologists, visual biologists, and physiologists. MoonShine also predicts and re-creates sunlight, making it a one-stop solution for creating full natural diel light cycles or for manipulating light cycles in a range of animal husbandry and experimental scenarios.

Instruction manual: https://lokpoon.github.io/MoonShine_manual/overview.html

# Citation
Poon, L., Jenks, I. T., Crampton, W. G. R. (2024). MoonShine: A software-hardware system for simulating moonlight ground illuminance and re-creating artificial moonlight cycles in a laboratory environment. Methods in Ecology and Evolution. <ins>https://doi.org/10.1111/2041-210X.14299</ins>

Technical support contact: Lok Poon (poonchiulok@gmail.com)

# Moonlight ground illuminance prediction:
## Install MoonShineR package:
1. Install and load library _devtools_ (available on CRAN) in R.
<br/><br/>
`install.packages("devtools")`
<br/><br/>
`library(devtools)`

2. Run the following line in R to install MoonShineR from Crampton-Lab GitHub repository: 
`devtools::install_github("Crampton-Lab/MoonShineR_package")`
3. Restart R session:  
`.rs.restartR()`
4. Load MoonShineR library:  
`library(MoonShineR)`
5. Check out R documentation of the two MoonShineR functions:  
`?MoonShineR::predict_lux`  
`?MoonShineR::plot_lux`
6. Also see Chapter 1 "MoonShineR package" of the online instruction manual: https://lokpoon.github.io/MoonShine_manual/lux_calculator.html

Note:
MoonShineR (v1.1) is tested working with these dependency packages versions:
	suncalc (<= 0.5.1),
	magrittr (<= 2.0.3),
	dplyr (<= 1.1.4),
	lubridate (<= 1.9.3),
	REdaS (<= 0.9.4),
	ggplot2 (<= 3.5.1)

If the package is not working, please first try installing the above packages in the specified version.

MoonShineR package GitHub source code repository:  
https://github.com/Crampton-Lab/MoonShineR_package
# Moonlight cycle re-creation:
See online instruction manual: https://lokpoon.github.io/MoonShine_manual/overview.html  
This current repository hosts the files mentioned in this manual. The following is a checklist of the files provided.
## Files that run on the computer
### The two versions of MoonShineR scheduler R program:
- `moonshineR_moonlight_scheduler.R`
- `moonshineR_sunlight_twilight_scheduler.R`
### LED spectrum preview Excel file:
- `RGBW_LED_spectrum.xlsx`
### Manual scheduler Excel template file:
- `manual_scheduler.xlsx`
## Files that run on the Raspberry Pi
### The moon and sun versions of MoonShineP Python program:
- control_moon folder containing `moonshine_moon.py`
- control_sun folder containing `moonshine_sun.py`
### The moon and sun versions of `clear.py` for turning off the LED arrays:
- `clear_moon.py`
- `clear_sun.py`
