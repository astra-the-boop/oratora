from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'includes': ['PySide6', 'PySide6.QtWidgets', 'PySide6.QtCore', 'PySide6.QtGui'],
    'packages': ['PySide6'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
