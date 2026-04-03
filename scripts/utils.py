# utils.py

import logging
import os
import shutil
import requests
import json
from datetime import datetime

def get_user_id_from_token(token: str) -> int:
    """Get user ID from authentication token."""
    url = "https://api.example.com/auth/token"
    response = requests.get(url, headers={"Authorization": f"Bearer {token}"})
    if response.status_code == 200:
        data = json.loads(response.content)
        return data["user_id"]
    else:
        logging.error(f"Failed to get user ID, status code: {response.status_code}")
        raise Exception("Failed to get user ID")

def get_user_data(user_id: int) -> dict:
    """Get user data by user ID."""
    url = f"https://api.example.com/users/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        logging.error(f"Failed to get user data, status code: {response.status_code}")
        raise Exception("Failed to get user data")

def format_date(date: datetime) -> str:
    """Format date to string in YYYY-MM-DD format."""
    return date.strftime("%Y-%m-%d")

def move_file(src: str, dst: str) -> None:
    """Move file from source to destination."""
    try:
        shutil.move(src, dst)
    except FileNotFoundError:
        logging.error(f"Source file not found: {src}")
    except Exception as e:
        logging.error(f"Failed to move file: {str(e)}")

def get_directory_size(directory: str) -> int:
    """Get size of directory in bytes."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size