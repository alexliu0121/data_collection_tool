import os
import yaml
from economic_indicators import fetch_economic_indicators
from social_media_trends import fetch_social_media_trends
from utils import save_to_json, setup_logging

def load_config(config_path='config.yaml'):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def main():
    config = load_config()
    logger = setup_logging()

    # Create output directory if it doesn't exist
    os.makedirs(config['output']['directory'], exist_ok=True)

    # Fetch Economic Indicators
    try:
        economic_data = fetch_economic_indicators(config['economic_indicators'])
        save_to_json(economic_data, os.path.join(config['output']['directory'], config['output']['economic_indicators_file']))
        logger.info("Economic indicators data collected successfully.")
    except Exception as e:
        logger.error(f"Error collecting economic indicators data: {e}")

    # Fetch Social Media Trends
    try:
        social_media_data = fetch_social_media_trends(config['social_media_trends'])
        save_to_json(social_media_data, os.path.join(config['output']['directory'], config['output']['social_media_trends_file']))
        logger.info("Social media trends data collected successfully.")
    except Exception as e:
        logger.error(f"Error collecting social media trends data: {e}")

if __name__ == "__main__":
    main()
