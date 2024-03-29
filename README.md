[![License: MIT](https://img.shields.io:/github/license/kbrezinski/COVID-BiLSTM?logoColor=yellow)](https://github.com/kbrezinski/COVID-BiLSTM/blob/main/LICENSE)

# COVID-BiLSTM
This repo contains a time series analysis of wastewater indicators, mobility reports and other useful indicators to predict negative health outcomes associated with COVID-19.

## Table of Contents
* [Setup](#setup)
* [Usage](#usage)
* [Data Sources](#data-sources)

## Setup

1. `git clone https://github.com/kbrezinski/COVID-BiLSTM`
2. Open Anaconda console and navigate into project directory `cd PATH_TO_REPO`
3. Run `conda env create` from project directory (this will create a brand new conda environment).
4. Run `activate covid-bilstm`

That's it! It should work out-of-the-box executing environment.yml file which deals with dependencies.

## Usage

To be completed...

## Data Sources
* [Google COVID-19 Open-Data](https://github.com/GoogleCloudPlatform/covid-19-open-data) - mobility, government response, vaccination rate
* [Government of Canada - COVID Daily Epidemiology Update](https://health-infobase.canada.ca/covid-19/epidemiological-summary-covid-19-cases.html) - test, case and test rates, moving average case rates/death rate
* [Canadian Wastewater Survey](https://www150.statcan.gc.ca/n1/pub/38-26-0002/382600022022001-eng.htm) - COVID wastewater data for select regions in Canada
* [HealthCare Data, Vaccination Rates](https://resources-covid19canada.hub.arcgis.com/datasets/covid19canada::provincial-daily-totals/about/)

Province Specific:
* [Ontario COVID-19 Data Tool](https://www.publichealthontario.ca/en/Data-and-Analysis/Infectious-Disease/COVID-19-Data-Surveillance/COVID-19-Data-Tool?tab=summary) - hospitilization rates, ICUs
* 

## Citation

If you find this code useful, please cite the following:

```
@misc{Brezinski2022,
  author = {Brezinski, Kenneth},
  title = {COVID-BiLSTM},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/kbrezinski/COVID-BiLSTM}},
}
```
