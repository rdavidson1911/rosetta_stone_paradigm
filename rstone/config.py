import configparser
import os

class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config_file = 'rstone/config.ini' # Looks good here. 
        
        if not os.path.exists(self.config_file):
            self.create_default_config()
        else:
            self.config.read(self.config_file)
    
    def create_default_config(self):
        self.config['DEFAULT'] = {
            'LogLevel': 'INFO',
            'OutputDirectory': 'rstone/output' # Looks good here.  
        }
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)
    
    def get(self, section, key):
        return self.config.get(section, key)
    
    def set(self, section, key, value):
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, key, value)
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)
