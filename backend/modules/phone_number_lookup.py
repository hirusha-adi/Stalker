import os
import re
import subprocess

import phonenumbers as pnumb
from phonenumbers import parse
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

from utils.errors import PhoneinfogaNotFoundError

class Libphonenumber:
    def __init__(self, phone_number: str = ""):
        self.phone_number = phone_number

    def get_number_info(self, phone_number: str = ""):
        
        num_to_use = phone_number
        if phone_number == "":
            num_to_use = self.phone_number
        
        parsing = parse(num_to_use)
        loc = geocoder.description_for_number(parsing, "en")
        isp = carrier.name_for_number(parsing, "en")
        tz = timezone.time_zones_for_number(parsing)

        info = {
            "info": parsing,
            "is_valid_number": pnumb.is_valid_number(parsing),
            "can_be_internationally_dialed": pnumb.can_be_internationally_dialled(parsing),
            "location": loc,
            "region_code": pnumb.region_code_for_number(parsing),
            "number_type": pnumb.number_type(parsing),
            "is_carrier_specific": pnumb.is_carrier_specific(parsing),
            "isp": isp,
            "timezone": tz,
            "is_geographical_number": pnumb.is_number_geographical(parsing),
        }
        
        return info

class Phoneinfoga:
    def __init__(self, phone_number: str = ""):
        self.phone_number = phone_number
        self.command_output = ""
    
    def run_command(self, phone_number: str = ""):
        
        phoneinfoga_bin = os.path.join('bin', 'phoneinfoga.exe')
        command = f'{phoneinfoga_bin} scan -n "{phone_number or self.phone_number}"'

        if not os.path.isfile(phoneinfoga_bin):
            raise PhoneinfogaNotFoundError("Error: phoneinfoga.exe not found.")
        
        self.command_output = subprocess.check_output(command, shell=True, text=True)
        return self.command_output
    
    def extract_scanner_googlesearch(self, command_output: str = ""):
        categories = {
            "social_media": [],
            "disposable_providers": [],
            "reputation": [],
            "individuals": [],
            "general": []
        }
        current_category = ""
        
        output_to_use = command_output
        if command_output == "":
            output_to_use = self.command_output

        lines = output_to_use.split('\n')

        for line in lines:
            line = line.strip()
            if line.startswith("Social media:"):
                current_category = "social_media"
            elif line.startswith("Disposable providers:"):
                current_category = "disposable_providers"
            elif line.startswith("Reputation:"):
                current_category = "reputation"
            elif line.startswith("Individuals:"):
                current_category = "individuals"
            elif line.startswith("General:"):
                current_category = "general"
            elif line.startswith("URL:"):
                url_match = re.search(r'URL:\s+(.*)', line)
                if url_match:
                    categories[current_category].append({
                        "id": len(categories[current_category]) + 1,
                        "url": url_match.group(1).strip()
                    })

        return categories
    
    def extract_basic_info(self, command_output: str = ""):
        basic_info = {}
        
        output_to_use = command_output
        if command_output == "":
            output_to_use = self.command_output
            
        lines = output_to_use.split('\n')

        for line in lines:
            line = line.strip()
            if line.startswith("Raw local:"):
                basic_info["raw_local"] = line.split(":")[1].strip()
            elif line.startswith("Local:"):
                basic_info["local"] = line.split(":")[1].strip()
            elif line.startswith("E164:"):
                basic_info["e164"] = line.split(":")[1].strip()
            elif line.startswith("International:"):
                basic_info["international"] = line.split(":")[1].strip()
            elif line.startswith("Country:"):
                basic_info["country"] = line.split(":")[1].strip()

        return basic_info

class PhoneNumberLookup:
    def __init__(self, phone_number: str = None) -> None:
        self.phone_number = phone_number
        
        """
        self.final_data = {
            'status': {
                'error': False,
                'error_desc': [],
                'show_information': True,
                'show_scanner_googlesearch': True,
            },
            'information': {
                "can_be_internationally_dialed": "True",
                "country": "",
                "e164": "",
                "info": "Country Code: ' National Number: ''",
                "international": "",
                "is_carrier_specific": "False",
                "is_geographical_number": "False",
                "is_valid_number": "True",
                "isp": "",
                "local": ",
                "location": "",
                "number_type": "",
                "raw_local": "",
                "region_code": "",
                "timezone": ""
            },
            'scanner_googlesearch': {
                "social_media": [],
                "disposable_providers": [],
                "reputation": [],
                "individuals": [],
                "general": []
            }
        }
        """
        
        self.final_data = {}
        
        self.final_data['status'] = {}
        self.final_data['status']['error'] = False
        self.final_data['status']['error_desc'] = []
        
        self.final_data['information'] = {}
        self.final_data['scanner_googlesearch'] = {}
        
        self.info_libphonenumber = {}
        
    
    def phoneinfoga(self):
        obj = Phoneinfoga(self.phone_number)

        self.final_data['status']['show_scanner_googlesearch'] = False
        try:
            obj.run_command()
            self.final_data['scanner_googlesearch'] = obj.extract_scanner_googlesearch()
            self.final_data['status']['show_scanner_googlesearch'] = True
        except subprocess.CalledProcessError as e:
            self.final_data['status']['error'] = True
            self.final_data['status']['error_desc'].append(f'{e}')
        except PhoneinfogaNotFoundError as e:
            self.final_data['status']['error'] = True
            self.final_data['status']['error_desc'].append(f'{e}')
        
        self.final_data['status']['show_information'] = False
        try:
            self.final_data['information'] = obj.extract_basic_info()
            self.final_data['status']['show_information'] = True
            self.final_data['status']['error_desc'].append('Not showing information from "local" scanner of Phoneinfoga')
        except Exception as e:
            self.final_data['status']['error'] = True
            self.final_data['status']['error_desc'].append(f'{e}')
    
    def libphonenumber(self):
        obj = Libphonenumber(self.phone_number)
        
        try:
            self.info_libphonenumber = obj.get_number_info()
            return self.info_libphonenumber
        except Exception as e:
            self.final_data['status']['error'] = True
            self.final_data['status']['error_desc'].append(f'{e}')
            self.final_data['status']['show_information'] = False
    
    def merge_results(self):
        for key, value in self.info_libphonenumber.items():
            if isinstance(value, bool):
                self.final_data['information'][key] = value
            else:
                self.final_data['information'][key] = str(value)

    def run(self):
        self.phoneinfoga()
        self.libphonenumber()
        self.merge_results()
        return self.final_data
    