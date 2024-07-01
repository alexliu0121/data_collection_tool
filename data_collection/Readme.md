# Data Collection Tool for AgTech

## Overview
This tool collects external data relevant to fertilizer inventory and demand planning. It currently supports data collection from economic indicators and social media trends from websites. The tool is designed to be modular and easily extendable to include additional data sources.

## Notes
- Noted that this is a code frame for future implementation
- The links in config.yaml file are not actual links but examples
- The task objectives I chose are social media trends and economic indicators

## Setup

### Prerequisites
- Python==3.11.5
- beautifulsoup4==4.12.3
- pandas==2.2.2
- PyYAML==6.0.1
- PyYAML==6.0.1
- Requests==2.32.3

### Installation
1. Clone the repository:
```bash
git clone https://github.com/alexliu0121/data_collection_tool.git
cd data_collection_tool
```
2. Create a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate
```
3. Install the required libraries:
```bash
pip install -r requirements.txt
```
4. Configure the data sources in config.yaml:
Update url for both economic_indicators and social_media_trends.

### Usage
Run the data collection script:
```bash
python data_collection.py
```

### Output
The collected data will be saved in the data directory as specified in config.yaml.

## File Structure
```plaintext
data_collection/
├── config.yaml # Configuration file for data sources and parameters
├── data_collection.py # Main script to initiate data collection
├── economic_indicators.py # Script to scrape economic indicators data from a website
├── social_media_trends.py # Script to scrape social media trends data from a website
├── utils.py # Utility functions for saving data and setting up logging
├── README.md # Project documentation
└── requirements.txt # List of project dependencies
```

### Extending The Tool
To add a new data source, create a new Python module and update data_collection.py to include the new data collection logic.

### Logging
Logs will be saved in data_collection.log file.

## License
This project is licensed under the GNU General Public License v3.0 License.

## Contact
If you have any questions or feedback, feel free to reach out to alexliu0121@gmail.com.
