# -*- coding: utf-8 -*-
"""
Constants used throughout the application.
"""
__author__ = 'Sohhla'


import os


# Globally Unique Identifier - Generated by https://www.guidgenerator.com/
# Used to allow only one instance of the application
GUID = "4B5806D7-7D6A-4DBD-A2A1-F2F1D4CCF585"


# Certificate used by the Requests API to validate HTTPS connections.
# As of Apr 06 2015, only Anime Tosho uses HTTPS.
# The file cacert.pem was copied from the "certifi" library.
CACERT_PATH = os.path.join(os.path.abspath("."),"cacert.pem")


# Path where all files generated by the application must be saved.
DATA_PATH =  "%s\\AnimeTorr" % (os.environ['APPDATA'])


# Path where the database must be saved and the name of the SQLite DB file.
DB_PATH =  DATA_PATH+"\\data.db"


# Path where the log files must be saved and the name of the log file.
LOG_PATH =  DATA_PATH+"\\atlog.log"


# Default folder where the .torrent files are saved.
DEFAULT_TORRENTS_PATH =  DATA_PATH+"\\torrents"


# Default path to be used in file/folder selectors (QFileDialog) when there's no previously selected path.
FILEDIALOG_DEFAULT_PATH = os.environ["USERPROFILE"]


# Text shown when the mouse is over the tray icon.
TRAY_MESSAGE_TITLE = "AnimeTorr"


# Shortcut created to automatically start this application on Windows startup.
AUTOSTART_SHORTCUT_NAME = "AnimeTorr (start minimized).lnk"
AUTOSTART_SHORTCUT_DESCRIPTION = "AnimeTorr (start minimized, with system tray icon)"