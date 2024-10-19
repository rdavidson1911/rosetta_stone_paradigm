import logging
from rstone.config import Config

class LoggingSetup:
    def __init__(self):
        self.config = Config()
        self.setup_logging()
    
    def setup_logging(self):
        log_level = self.config.get('DEFAULT', 'LogLevel')
        logging.basicConfig(
            level=getattr(logging, log_level),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            filename='rstone/rosetta_stone.log'
        )
        
        # Create a console handler
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)
