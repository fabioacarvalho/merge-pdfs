#!/bin/bash

# Check if PySide6 is installed
if ! python3 -c "import PySide6" &> /dev/null; then
    echo "PySide6 is not installed. Installing..."
    pip install PySide6
else
    echo "PySide6 is already installed."
fi