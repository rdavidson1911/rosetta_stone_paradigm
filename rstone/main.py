import tkinter as tk
from rstone.gui import RosettaStoneGUI
from rstone.logging_setup import LoggingSetup
from rstone.config import Config
import logging

def main():
    # Initialize logging and config
    LoggingSetup()
    config = Config()
    
    logging.info("Starting Rosetta Stone Paradigm application")
    
    # Create the main window
    root = tk.Tk()
    app = RosettaStoneGUI(root)
    
    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()
