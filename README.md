# Repository Name

## Introduction
This GitHub repository contains a Python script for analyzing NFL player performance data using the `nfl_data_py` library, focusing on rushing plays. The script calculates various statistics, including Expected Yards Over Expectation (RYOE), and identifies top-performing rushers based on these metrics. This README provides an overview of the code, how to use it, and its intended purpose.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Data Source](#data-source)
- [Methodology](#methodology)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Requirements
To run this code, you need the following Python libraries installed:
- `pandas`
- `numpy`
- `nfl_data_py`
- `statsmodels`
- `matplotlib`
- `seaborn`

You can install these packages using `pip`:
```bash
pip install pandas numpy nfl_data_py statsmodels matplotlib seaborn
```

## Installation
1. Clone this repository to your local machine using Git:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   ```

2. Navigate to the repository directory:
   ```bash
   cd your-repo
   ```

3. Run the Python script:
   ```bash
   python your_script.py
   ```

## Usage
The provided script, `your_script.py`, imports NFL player performance data and performs analysis on rushing plays. It calculates the Expected Yards Over Expectation (RYOE) and identifies top-performing rushers. Simply run the script to obtain the results.

```bash
python your_script.py
```

## Data Source
The data used in this analysis is sourced from the `nfl_data_py` library and contains information about NFL plays and player statistics. Ensure you have access to this data source or update the code to fetch data from an appropriate source.

## Methodology
The code in the script performs the following steps:
1. Imports the required libraries.
2. Imports NFL play-by-play data for a specific season (currently set to 2023).
3. Filters and cleans the data to focus on rushing plays with necessary attributes.
4. Calculates Expected Yards using a linear regression model.
5. Calculates RYOE and expected fantasy points for each rushing play.
6. Aggregates the data to get player-level statistics.
7. Filters and renames columns for better readability.

## Results
The code outputs a DataFrame with player-level statistics, including RYOE, yards per carry, expected yards, and more. The DataFrame is sorted by RYOE in descending order, identifying the top-performing rushers. Players with a minimum of 50 rushing plays are included in the analysis.

## Contributing
If you would like to contribute to this project or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

## License
This project is licensed under the [MIT License](LICENSE), which means you are free to use, modify, and distribute the code as long as you include the original license and disclaimer.
