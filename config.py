import os
import codecs

try:
    import configparser as ConfigParser
except ImportError:
    import ConfigParser

# Directories
script_dir = os.path.dirname(os.path.abspath(__file__))


class Config:
    def __init__(self, filepath):
        # Read configuration file
        config = ConfigParser.ConfigParser()
        config.read_file(codecs.open(filepath, "r", "utf8"))

        # ChatGPT configuration info
        self.chatgpt_key = config.get('chatgpt', 'chatgpt_key')

        # Bing Configuration info
        self.bing_key = config.get('bing', 'bing_key')

        # Bard info
        self.bard_secure_1psid = config.get('bard', '1psid')
        self.bard_secure_1psidcc = config.get('bard', '1psidcc')
        self.bard_secure_1psidts = config.get('bard', '1psidts')
