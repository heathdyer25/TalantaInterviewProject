"""
run.py

Starts and runs the Flask web application on your local machine at port 5000

Author: Heath Dyer
Created: 2025-05-22
"""

from app import app

if __name__ == "__main__":
    app.run(debug=True)