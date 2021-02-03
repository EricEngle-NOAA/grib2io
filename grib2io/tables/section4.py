table_4_1_0 = {
'0':'Temperature',
'1':'Moisture',
'2':'Momentum',
'3':'Mass',
'4':'Short-wave radiation',
'5':'Long-wave radiation',
'6':'Cloud',
'7':'Thermodynamic Stability indicies',
'8':'Kinematic Stability indicies',
'9':'Temperature Probabilities*',
'10':'Moisture Probabilities*',
'11':'Momentum Probabilities*',
'12':'Mass Probabilities*',
'13':'Aerosols',
'14':'Trace gases',
'15':'Radar',
'16':'Forecast Radar Imagery',
'17':'Electrodynamics',
'18':'Nuclear/radiology',
'19':'Physical atmospheric properties',
'20':'Atmospheric chemical Constituents',
'21-189':'Reserved',
'190':'CCITT IA5 string',
'191':'Miscellaneous',
'192-254':'Reserved for Local Use',
'192':'Covariance',
'255':'Missing',
}

table_4_1_1 = {
'0':'Hydrology basic products',
'1':'Hydrology probabilities',
'2':'Inland water and sediment properties',
'3-191':'Reserved',
'192-254':'Reserved for Local Use',
'255':'Missing',
}

table_4_1_2 = {
'0':'Vegetation/Biomass',
'1':'Agricultural/Aquacultural Special Products',
'2':'Transportation-related Products',
'3':'Soil Products',
'4':'Fire Weather Products',
'5':'Land Surface Products',
'6-191':'Reserved',
'192-254':'Reserved for Local Use',
'255':'Missing',
}

table_4_1_3 = {
'0':'Image format products',
'1':'Quantitative products',
'2':'Cloud Properties',
'3':'Flight Rules Conditions',
'4':'Volcanic Ash',
'5':'Sea-surface Temperature',
'6':'Solar Radiation',
'7-191':'Reserved',
'192-254':'Reserved for Local Use',
'192':'Forecast Satellite Imagery',
'255':'Missing',
}

table_4_1_4 = {
'0':'Temperature',
'1':'Momentum',
'2':'Charged Particle Mass and Number',
'3':'Electric and Magnetic Fields',
'4':'Energetic Particles',
'5':'Waves',
'6':'Solar Electromagnetic Emissions',
'7':'Terrestrial Electromagnetic Emissions',
'8':'Imagery',
'9':'Ion-Neutral Coupling',
'10-191':'Reserved',
'192-254':'Reserved for Local Use',
'255':'Missing',
}

table_4_1_10 = {
'0':'Waves',
'1':'Currents',
'2':'Ice',
'3':'Surface Properties',
'4':'Sub-surface Properties',
'5-190':'Reserved',
'191':'Miscellaneous',
'192-254':'Reserved for Local Use',
'255':'Missing',
}

table_4_3 = {
'0':'Analysis',
'1':'Initialization',
'2':'Forecast',
'3':'Bias Corrected Forecast',
'4':'Ensemble Forecast',
'5':'Probability Forecast',
'6':'Forecast Error',
'7':'Analysis Error',
'8':'Observation',
'9':'Climatological',
'10':'Probability-Weighted Forecast',
'11':'Bias-Corrected Ensemble Forecast',
'12':'Post-processed Analysis (See Note)',
'13':'Post-processed Forecast (See Note)',
'14':'Nowcast',
'15':'Hindcast',
'16':'Physical Retrieval',
'17':'Regression Analysis',
'18':'Difference Between Two Forecasts',
'19-191':'Reserved',
'192-254':'Reserved for Local Use',
'192':'Forecast Confidence Indicator',
'193':'Probability-matched Mean',
'194':'Neighborhood Probability',
'195':'Bias-Corrected and Downscaled Ensemble Forecast',
'196':'Perturbed Analysis for Ensemble Initialization',
'197':'Ensemble Agreement Scale Probability',
'198':'Post-Processed Deterministic-Expert-Weighted Forecast',
'199':'Ensemble Forecast Based on Counting',
'200':'Local Probability-matched Mean',
'255':'Missing',
}

table_4_4 = {
'0':'Minute',
'1':'Hour',
'2':'Day',
'3':'Month',
'4':'Year',
'5':'Decade (10 Years)',
'6':'Normal (30 Years)',
'7':'Century (100 Years)',
'8':'Reserved',
'9':'Reserved',
'10':'3 Hours',
'11':'6 Hours',
'12':'12 Hours',
'13':'Second',
'14-191':'Reserved',
'192-254':'Reserved for Local Use',
'255':'Missing',
}

table_4_5 = {
'0':['Reserved','unknown'],
'1':['Ground or Water Surface','unknown'],
'2':['Cloud Base Level','unknown'],
'3':['Level of Cloud Tops','unknown'],
'4':['Level of 0o C Isotherm','unknown'],
'5':['Level of Adiabatic Condensation Lifted from the Surface','unknown'],
'6':['Maximum Wind Level','unknown'],
'7':['Tropopause','unknown'],
'8':['Nominal Top of the Atmosphere','unknown'],
'9':['Sea Bottom','unknown'],
'10':['Entire Atmosphere','unknown'],
'11':['Cumulonimbus Base (CB)','m'],
'12':['Cumulonimbus Top (CT)','m'],
'13':['Lowest level where vertically integrated  cloud cover exceeds the specified percentage (cloud base for a given percentage cloud cover)','%'],
'14':['Level of free convection (LFC)','unknown'],
'15':['Convection condensation level (CCL)','unknown'],
'16':['Level of neutral buoyancy or equilibrium (LNB)','unknown'],
'17-19':['Reserved','unknown'],
'20':['Isothermal Level','K'],
'21':['Lowest level where mass density exceeds the specified value  (base for a given threshold of mass density)','kg m-3'],
'22':['Highest level where mass density exceeds the specified value (top for a given threshold of mass density)','kg m-3'],
'23':['Lowest level where air concentration exceeds the specified value (base for a given threshold of air concentration','Bq m-3'],
'24':['Highest level where air concentration exceeds the specified  value (top for a given threshold of air concentration)','Bq m-3'],
'25':['Highest level where radar reflectivity exceeds the specified  value (echo top for a given threshold of reflectivity)','dBZ'],
'26-99':['Reserved','unknown'],
'100':['Isobaric Surface','Pa'],
'101':['Mean Sea Level','unknown'],
'102':['Specific Altitude Above Mean Sea Level','m'],
'103':['Specified Height Level Above Ground','m'],
'104':['Sigma Level','unknown'],
'105':['Hybrid Level','unknown'],
'106':['Depth Below Land Surface','m'],
'107':['Isentropic (theta) Level','K'],
'108':['Level at Specified Pressure Difference from Ground to Level','Pa'],
'109':['Potential Vorticity Surface','K m2 kg-1 s-1'],
'110':['Reserved','unknown'],
'111':['Eta Level','unknown'],
'112':['Reserved','unknown'],
'113':['Logarithmic Hybrid Level','unknown'],
'114':['Snow Level','Numeric'],
'115':['Sigma height level (see Note 4)','unknown'],
'116':['Reserved','unknown'],
'117':['Mixed Layer Depth','m'],
'118':['Hybrid Height Level','unknown'],
'119':['Hybrid Pressure Level','unknown'],
'120-149':['Reserved','unknown'],
'150':['Generalized Vertical Height Coordinate (see Note 4)','unknown'],
'151':['Soil level (See Note 5)','Numeric'],
'152-159':['Reserved','unknown'],
'160':['Depth Below Sea Level','m'],
'161':['Depth Below Water Surface','m'],
'162':['Lake or River Bottom','unknown'],
'163':['Bottom Of Sediment Layer','unknown'],
'164':['Bottom Of Thermally Active Sediment Layer','unknown'],
'165':['Bottom Of Sediment Layer Penetrated By Thermal Wave','unknown'],
'166':['Mixing Layer','unknown'],
'167':['Bottom of Root Zone','unknown'],
'168':['Ocean Model Level','Numeric'],
'169':['Ocean level defined by water density (sigma-theta)  difference from near-surface to level (see Note 7)','kg m-3'],
'170':['Ocean level defined by water potential temperature  difference from near-surface to level (see Note 7)','K'],
'171-173':['Reserved','unknown'],
'174':['Top Surface of Ice on Sea, Lake or River','unknown'],
'175':['Top Surface of Ice, under Snow, on Sea, Lake or River','unknown'],
'176':['Bottom Surface (underside) Ice on Sea, Lake or River','unknown'],
'177':['Deep Soil (of indefinite depth)','unknown'],
'178':['Reserved','unknown'],
'179':['Top Surface of Glacier Ice and Inland Ice','unknown'],
'180':['Deep Inland or Glacier Ice (of indefinite depth)','unknown'],
'181':['Grid Tile Land Fraction as a Model Surface','unknown'],
'182':['Grid Tile Water Fraction as a Model Surface','unknown'],
'183':['Grid Tile Ice Fraction on Sea, Lake or River as a Model Surface','unknown'],
'184':['Grid Tile Glacier Ice and Inland Ice Fraction as a Model Surface','unknown'],
'185-191':['Reserved','unknown'],
'192-254':['Reserved for Local Use','unknown'],
'200':['Entire atmosphere (considered as a single layer)','unknown'],
'201':['Entire ocean (considered as a single layer)','unknown'],
'204':['Highest tropospheric freezing level','unknown'],
'206':['Grid scale cloud bottom level','unknown'],
'207':['Grid scale cloud top level','unknown'],
'209':['Boundary layer cloud bottom level','unknown'],
'210':['Boundary layer cloud top level','unknown'],
'211':['Boundary layer cloud layer','unknown'],
'212':['Low cloud bottom level','unknown'],
'213':['Low cloud top level','unknown'],
'214':['Low cloud layer','unknown'],
'215':['Cloud ceiling','unknown'],
'216':['Effective Layer Top Level','m'],
'217':['Effective Layer Bottom Level','m'],
'218':['Effective Layer','m'],
'220':['Planetary Boundary Layer','unknown'],
'221':['Layer Between Two Hybrid Levels','unknown'],
'222':['Middle cloud bottom level','unknown'],
'223':['Middle cloud top level','unknown'],
'224':['Middle cloud layer','unknown'],
'232':['High cloud bottom level','unknown'],
'233':['High cloud top level','unknown'],
'234':['High cloud layer','unknown'],
'235':['Ocean Isotherm Level (1/10 ° C)','unknown'],
'236':['Layer between two depths below ocean surface','unknown'],
'237':['Bottom of Ocean Mixed Layer (m)','unknown'],
'238':['Bottom of Ocean Isothermal Layer (m)','unknown'],
'239':['Layer Ocean Surface  and 26C Ocean Isothermal Level','unknown'],
'240':['Ocean Mixed Layer','unknown'],
'241':['Ordered Sequence of Data','unknown'],
'242':['Convective cloud bottom level','unknown'],
'243':['Convective cloud top level','unknown'],
'244':['Convective cloud layer','unknown'],
'245':['Lowest level of the wet bulb zero','unknown'],
'246':['Maximum equivalent potential temperature level','unknown'],
'247':['Equilibrium level','unknown'],
'248':['Shallow convective cloud bottom level','unknown'],
'249':['Shallow convective cloud top level','unknown'],
'251':['Deep convective cloud bottom level','unknown'],
'252':['Deep convective cloud top level','unknown'],
'253':['Lowest bottom level of supercooled liquid water layer','unknown'],
'254':['Highest top level of supercooled liquid water layer','unknown'],
'255':['Missing','unknown'],
}

table_4_6 = {
'0':'Unperturbed High-Resolution Control Forecast',
'1':'Unperturbed Low-Resolution Control Forecast',
'2':'Negatively Perturbed Forecast',
'3':'Positively Perturbed Forecast',
'4':'Multi-Model Forecast',
'5-191':'Reserved',
'192-254':'Reserved for Local Use',
'192':'Perturbed Ensemble Member',
'255':'Missing',
}

table_4_7 = {
'0':'Unweighted Mean of All Members',
'1':'Weighted Mean of All Members',
'2':'Standard Deviation with respect to Cluster Mean',
'3':'Standard Deviation with respect to Cluster Mean, Normalized',
'4':'Spread of All Members',
'5':'Large Anomaly Index of All Members (see Note 1)',
'6':'Unweighted Mean of the Cluster Members',
'7':'Interquartile Range (Range between the 25th and 75th quantile)',
'8':'Minimum Of All Ensemble Members (see Note 2)',
'9':'Maximum Of All Ensemble Members (see Note 2)',
'7-191':'Reserved',
'192-254':'Reserved for Local Use',
'192':'Unweighted Mode of All Members',
'193':'Percentile value (10%) of All Members',
'194':'Percentile value (50%) of All Members',
'195':'Percentile value (90%) of All Members',
'196':'Statistically decided weights for each ensemble member',
'197':'Climate Percentile (percentile values from climate distribution)',
'198':'Deviation of Ensemble Mean from Daily Climatology',
'199':'Extreme Forecast Index',
'200':'Equally Weighted Mean',
'201':'Percentile value (5%) of All Members',
'202':'Percentile value (25%) of All Members',
'203':'Percentile value (75%) of All Members',
'204':'Percentile value (95%) of All Members',
'255':'Missing',
}

table_4_8 = {
'0':'Anomoly Correlation',
'1':'Root Mean Square',
'2-191':'Reserved',
'192-254':'Reserved for Local Use',
'255':'Missing',
}

table_4_9 = {
'0':'Probability of event below lower limit',
'1':'Probability of event above upper limit',
'2':'Probability of event between upper and lower limits (the range includes lower limit but no the upper limit)',
'3':'Probability of event above lower limit',
'4':'Probability of event below upper limit',
'5':'Probability of event equal to lower limit',
'6':'Probability of event in above normal category (see Notes 1 and 2)',
'9-191':'Reserved',
'192-254':'Reserved for Local Use',
'255':'Missing',
}

table_4_10 = {
'0':'Average',
'1':'Accumulation (see Note 1)',
'2':'Maximum',
'3':'Minimum',
'4':'Difference (value at the end of the time range minus value at the beginning)',
'5':'Root Mean Square',
'6':'Standard Deviation',
'7':'Covariance (temporal variance) (see Note 2)',
'8':'Difference ( value at the beginning of the time range minus value at the end)',
'9':'Ratio (see Note 3)',
'14-191':'Reserved',
'192-254':'Reserved for Local Use',
'192':'Climatological Mean Value: multiple year averages of quantities which are themselves means over some period of time (P2) less than a year. The reference time (R) indicates the date and time of the start of a period of time, given by R to R + P2, over which a mean is formed; N indicates the number of such period-means that are averaged together to form the climatological value, assuming that the N period-mean fields are separated by one year. The reference time indicates the start of the N-year climatology. N is given in octets 22-23 of the PDS.  If P1 = 0 then the data averaged in the basic interval P2 are assumed to be continuous, i.e., all available data are simply averaged together.  If P1 = 1 (the units of time - octet 18, code table 4 - are not relevant here) then the data averaged together in the basic interval P2 are valid only at the time (hour, minute) given in the reference time, for all the days included in the P2 period. The units of P2 are given by the contents of octet 18 and Table 4.',
'193':'Average of N forecasts (or initialized analyses); each product has forecast period of P1 (P1=0 for initialized analyses); products have reference times at intervals of P2, beginning at the given reference time.',
'194':'Average of N uninitialized analyses, starting at reference time, at intervals of P2.',
'195':'Average of forecast accumulations. P1 = start of accumulation period. P2 = end of accumulation period. Reference time is the start time of the first forecast, other forecasts at 24-hour intervals. Number in Ave = number of forecasts used.',
'196':'Average of successive forecast accumulations. P1 = start of accumulation period. P2 = end of accumulation period. Reference time is the start time of the first forecast, other forecasts at (P2 - P1) intervals. Number in Ave = number of forecasts used',
'197':'Average of forecast averages. P1 = start of averaging period. P2 = end of averaging period. Reference time is the start time of the first forecast, other forecasts at 24-hour intervals. Number in Ave = number of forecast used',
'198':'Average of successive forecast averages. P1 = start of averaging period. P2 = end of averaging period. Reference time is the start time of the first forecast, other forecasts at (P2 - P1) intervals. Number in Ave = number of forecasts used',
'199':'Climatological Average of N analyses, each a year apart, starting from initial time R and for the period from R+P1 to R+P2.',
'200':'Climatological Average of N forecasts, each a year apart, starting from initial time R and for the period from R+P1 to R+P2.',
'201':'Climatological Root Mean Square difference between N forecasts and their verifying analyses, each a year apart, starting with initial time R and for the period from R+P1 to R+P2.',
'202':'Climatological Standard Deviation of N forecasts from the mean of the same N forecasts, for forecasts one year apart. The first forecast starts wtih initial time R and is for the period from R+P1 to R+P2.',
'203':'Climatological Standard Deviation of N analyses from the mean of the same N analyses, for analyses one year apart. The first analyses is valid for period R+P1 to R+P2.',
'204':'Average of forecast accumulations. P1 = start of accumulation period. P2 = end of accumulation period. Reference time is the start time of the first forecast, other forecasts at 6-hour intervals. Number in Ave = number of forecast used',
'205':'Average of forecast averages. P1 = start of averaging period. P2 = end of averaging period. Reference time is the start time of the first forecast, other forecasts at 6-hour intervals. Number in Ave = number of forecast used',
'206':'Average of forecast accumulations. P1 = start of accumulation period. P2 = end of accumulation period. Reference time is the start time of the first forecast, other forecasts at 12-hour intervals. Number in Ave = number of forecast used',
'207':'Average of forecast averages. P1 = start of averaging period. P2 = end of averaging period. Reference time is the start time of the first forecast, other forecasts at 12-hour intervals. Number in Ave = number of forecast used',
'255':'Missing',
}

table_4_11 = {
'0':'Reserved',
'1':'Successive times processed have same forecast time, start time of forecast is incremented.',
'2':'Successive times processed have same start time of forecast, forecast time is incremented.',
'3':'Successive times processed have start time of forecast incremented and forecast time decremented so that valid time remains constant.',
'4':'Successive times processed have start time of forecast decremented and forecast time incremented so that valid time remains constant.',
'5':'Floating subinterval of time between forecast time and end of overall time interval.(see Note 1)',
'6-191':'Reserved',
'192-254':'Reserved for Local Use',
'255':'Missing',
}

table_scale_time_hours = {
'0': 60.,
'1': 1.,
'2': float(1.0/24.0),
'3': float(1.0/720.0),
'4': float(1.0/(365.0*24.0)),
'5': float(1.0/(10.0*365.0*24.0)),
'6': float(1.0/(30.0*365.0*24.0)),
'7': float(1.0/(100.0*365.0*24.0)),
'8': 1.,
'9': 1.,
'10': 3.,
'11': 6.,
'12': 12.,
'13': 3600.,
'14-255': 1.}
