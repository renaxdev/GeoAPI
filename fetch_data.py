#https://github.com/porimol/countryinfo < check for original repo and library
from glob import glob
from os.path import isfile, realpath, dirname
import json


class FetchData:

    def __init__(self, country_name=None):
        self.__country_name = country_name.lower() if country_name else ''
        __file_dir_path = dirname(realpath(__file__))
        __country_files = __file_dir_path + '/data/'
        __files_path = [files for files in glob(__country_files + '*.json')]
        self.__countries = {}
        for file_path in __files_path:
            if isfile(file_path):
                with open(file_path, encoding='utf-8') as file:
                    country_info = json.load(file)
                    if country_info.get('name', None):
                        self.__countries[country_info['name'].lower()] = country_info
                        if self.__country_name in map(lambda an: an.lower(), country_info.get('altSpellings', [])):
                            self.__country_name = country_info['name'].lower()

    def info(self):
        if self.__country_name:
            _all = self.__countries[self.__country_name]
            return _all

    def iso(self, alpha=None):
        if self.__country_name:
            _iso = self.__countries[self.__country_name]['ISO']

            if alpha == 2:
                return _iso.get('alpha2')
            elif alpha == 3:
                return _iso.get('alpha3')

            return _iso

    def currencies(self):
        if self.__country_name:
            _currencies = self.__countries[self.__country_name]['currencies']

            return _currencies

    def population(self):
        if self.__country_name:
            _population = self.__countries[self.__country_name]['population']

            return _population

    def timezones(self):
        if self.__country_name:
            _timezones = self.__countries[self.__country_name]['timezones']


            return _timezones

    def area(self):
        if self.__country_name:
            _area = self.__countries[self.__country_name]['area']
            return _area