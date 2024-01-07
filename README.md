# Analyzing-Weird-College-Football-Offenses

A small number of FBS College Football teams each year use "Option" offenses. These offenses differ significantly from the more standard offenses used by most teams. A common truism among College Football fans says that we can expect a defense to play better against Option offenses if it has more experience against them. I test that truism in this project, finding evidence in play-by-play data from 2004-2023 that supports it. 

The package contains 5 Python (.py) files, a Jupyter notebook (.ipynb), and the HTML conversion of the notebook. The Python files gather the required data from the [CollegeFootballData.com](CollegeFootballData.com) API. To use them, install the [cfbd package](https://github.com/CFBD/cfbd-python), request an [API key](https://collegefootballdata.com/key) and paste where directed in config.py. The other Python files can be modified to gather data from different year ranges by changing the first_year and last_year variables. The analysis can be found in the notebook or HTML file.


