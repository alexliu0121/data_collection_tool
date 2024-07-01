# Data Collection Tool for AgTech

## Overview
This tool collects external data relevant to fertilizer inventory and demand planning. It currently supports data collection from economic indicators and social media trends from websites. The tool is designed to be modular and easily extendable to include additional data sources.

## Setup

### Prerequisites
- Python 3.11.5
- beautifulsoup4==4.12.3
- pandas==2.2.2
- PyYAML==6.0.1
- PyYAML==6.0.1
- Requests==2.32.3

### Installation
1. Clone the repository:
```bash
git clone https://github.com/alexliu0121/ .git
cd data_collection_tool
```
2. Install the required libraries:
```bash
pip install -r requirements.txt
```
3. Configure the data sources in config.yaml:
Update url for both economic_indicators and social_media_trends.

### Usage
Run the data collection script:
```bash
python data_collection.py
```

### Output
The collected data will be saved in the data directory as specified in config.yaml.

### Extending The Tool
To add a new data source, create a new Python module and update data_collection.py to include the new data collection logic.

### Logging
Logs will be saved in data_collection.log file.

## Contact
If you have any questions or feedback, feel free to reach out to alexliu0121@gmail.com.