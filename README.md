# UCU-BP-1-grade-project

## Description
Parses https://www.metal-archives.com to analyze corellation between metal bands personal data, their split-up frequency, and song production frequency. Must help labels in choosing right bands for getting the greatest benefit. Takes about a month of work to get data; can be optimised by multithreading.

## Inputs and outputs
Takes no inputs, outputs are plots and bar charts, generated using matplotlib.pyplot

## Program structure:
band_list_scraper.py - scrapes the list of all bands on www.metal-archives.com . Stores their urls in band_url_list.txt
band_adt - classes, used to get band data from site.


## Requirements:
Last versions of Selenium, Firefox (as driver for Selenium), Python-Metallum, Matplotlib.
Installation of them:
Selenium - pip install selenium
Python-Metallum - pip install python-metallum
Matplotlib - pip install matplotlib
Firefox - https://www.mozilla.org/en-US/firefox/new/

## Usage
Run main.py.

## Contribution
Not allowed.

## License
MIT
