# MoonShine
## Updated Feb 1, 2024
<img src="/others/moonshine_logo.png" width=50% height=50%>

MoonShine is a suite of software tools and electronic hardware for predicting moonlight (and/or twilight and sunlight) ground illuminance and for re-creating moonlight cycles in a laboratory environment using LED arrays. MoonShine is designed for field and experimental ecologists, chronobiologists, visual biologists, and physiologists. MoonShine also predicts and re-creates sunlight, making it a one-stop solution for creating full natural diel light cycles or for manipulating light cycles in a range of animal husbandry and experimental scenarios.

Instruction manual: https://lokpoon.github.io/MoonShine_manual/overview.html

# Citation
Poon, L., Jenks, I. T., & Crampton, W. G. R. (2024). MoonShine: A software-hardware system for simulating moonlight ground illuminance and re-creating artificial moonlight cycles in a laboratory environment. Methods in Ecology and Evolution. <ins>https://doi.org/10.1111/2041-210X.14299</ins>

Technical support contact: Lok Poon (poonchiulok@gmail.com)

# Predict moonlight ground illuminance using the R package MoonShineR:
## Install and run:
1. MoonShineR is currently published in the CRAN repository. Install MoonShineR in R with `install.packages("MoonShineR")`. Alternatively, in RStudio, search for MoonShineR in the Packages tab and click Install.
2. Load the MoonShineR library:  
`library(MoonShineR)`
3. Check the R documentation for the two MoonShineR functions and try running the examples:
- `?MoonShineR::predict_lux`  for calculating a predicted illuminance dataframe.
- `?MoonShineR::plot_lux` for plotting the predicted illuminance dataframe.

CRAN documentation: https://cran.r-project.org/web/packages/MoonShineR/index.html

Source code repository: https://github.com/Crampton-Lab/MoonShineR_package
# Re-create light regimes using LED arrays for experiments:
Do not use the CRAN MoonShineR package. This requires an advanced version of MoonShineR scripts to generate a light schedule that is read by Pyhon scripsts running on a Raspberry Pi that control LED arrays.

Full instructions are available in the online instruction manual: https://lokpoon.github.io/MoonShine_manual/overview.html

The current repository hosts all required files mentioned in this manual. The following is a checklist of the files.
## Files for creating a light regime schedule table during the preparation phase (run on any personal computer)
### The two versions of the MoonShineR scheduler R program:
- `moonshineR_moonlight_scheduler.R`
- `moonshineR_sunlight_twilight_scheduler.R`
### LED spectrum preview Excel file:
- `RGBW_LED_spectrum.xlsx`
### Manual scheduler Excel template file:
- `manual_scheduler.xlsx`
## Files for executing the light regime (run on the Raspberry Pi that controls the LED arrays)
### The moon and sun versions of the MoonShineP Python program:
- control_moon folder containing `moonshine_moon.py`
- control_sun folder containing `moonshine_sun.py`
### The moon and sun versions of `clear.py` for turning off the LED arrays:
- `clear_moon.py`
- `clear_sun.py`
