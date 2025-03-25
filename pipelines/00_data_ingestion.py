from pathlib import Path
import yaml
import gdown

CONFIG_PATH = Path('config/config.yaml')

def main():
    
    with open(CONFIG_PATH) as f:
        config = yaml.safe_load(f)

    gdown.download(config['data_ingestion']['source_url'], config['data_ingestion']['path'])

if __name__ == '__main__':
    main()