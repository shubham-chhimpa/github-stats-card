import json
import os
from os import listdir
from os.path import isfile, join

from datetime import timezone
import datetime

import requests

DATA_DIR_PATH = os.path.join(os.getcwd(), 'data')
TIMESTAMP_DIR_PATH = os.path.join(os.getcwd(), 'timestamp')
REFRESH_TIME = 3600.000000


class DataBase:
    def __init__(self):
        pass

    @staticmethod
    def add_file(username, data):
        print(DATA_DIR_PATH)
        with open(os.path.join(DATA_DIR_PATH, f"{username}.json"), "w") as file:
            file.write(data)
            file.close()
        DataBase.add_time_stamp(username)
        print(f"added {username}.json file")

    @staticmethod
    def check_file_exists(username):
        file_name = f"{username}.json"
        print("in check_file_exists")
        files = [f for f in listdir(DATA_DIR_PATH) if isfile(join(DATA_DIR_PATH, f))]
        for f in files:
            print(file_name)
            print(f)
            print(f == file_name)
            if f == file_name:
                return True
        return False

    @staticmethod
    def get_data(username):
        print("inside : get_data")
        if DataBase.check_file_exists(username):
            with open(os.path.join(DATA_DIR_PATH, f"{username}.json"), "r+") as file:
                data = json.load(file)
                file.close()
                return data

    @staticmethod
    def add_time_stamp(username):
        dt = datetime.datetime.now()
        utc_time = dt.replace(tzinfo=timezone.utc)
        utc_timestamp = utc_time.timestamp()
        with open(os.path.join(TIMESTAMP_DIR_PATH, f"{username}.txt"), "w") as file:
            file.write(str(utc_timestamp))
            file.close()
        print(f"added {username}.txt timestamp file")

    @staticmethod
    def get_time_stamp(username):
        if DataBase.check_file_exists(username):
            with open(os.path.join(TIMESTAMP_DIR_PATH, f"{username}.txt"), "r+") as file:
                data = float(file.read())
                print(data)
                file.close()
                return data

    @staticmethod
    def refresh(username):
        if DataBase.check_file_exists(username):
            dt = datetime.datetime.now()
            utc_time = dt.replace(tzinfo=timezone.utc)
            utc_timestamp = utc_time.timestamp()
            print("checking timestamp...")
            print(DataBase.get_time_stamp(username) + REFRESH_TIME < utc_timestamp)
            if DataBase.get_time_stamp(username) + REFRESH_TIME < utc_timestamp:
                print("timestamp expired")
                DataBase.fetch_data(username)
            else:
                print("timestamp not expired")

        else:
            DataBase.fetch_data(username)

    @staticmethod
    def fetch_data(username):
        print("inside : fetch_data")
        response = requests.get(f'https://api.github.com/users/{username}/repos')
        if response.status_code == 200:
            DataBase.add_file(username, response.text)
