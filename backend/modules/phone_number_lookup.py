import os
import re
import subprocess
from urllib.parse import urlparse
from urllib.parse import parse_qs

import phonenumbers as pnumb
from phonenumbers import parse
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

from utils.errors import PhoneinfogaNotFoundError
from utils.log import log

def sanitize(phone_number):
    """
    Validate and sanitize the input phone number.

    Parameters:
    - phone_number (str): The phone number to validate and sanitize.

    Returns:
    - str: Validated and sanitized phone number.
    """
    sanitized = re.sub(r'[^0-9+]', '', phone_number)
    log("DEBUG", "Hirusha")
    return sanitized

class Libphonenumber:
    def __init__(self, phone_number: str = ""):
        """
        Initialize Libphonenumber instance with an optional phone number.

        Parameters:
        - phone_number (str): The phone number to analyze.
        """
        
        self.phone_number = phone_number

    def get_number_info(self, phone_number: str = ""):
        """
        Get information about a phone number using the libphonenumber library.

        Parameters:
        - phone_number (str): The phone number to analyze.

        Returns:
        - dict: Information about the phone number.
        """
        
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
        """
        Initialize Phoneinfoga instance with an optional phone number.

        Parameters:
        - phone_number (str): The phone number to perform scans on.
        """
        
        self.phone_number = phone_number
        self.command_output = ""
    
    def run_command(self, phone_number: str = ""):
        """
        Run the Phoneinfoga command to perform scans on a phone number.

        Parameters:
        - phone_number (str): The phone number to perform scans on.

        Returns:
        - str: The output of the Phoneinfoga command.
        """
        
        phoneinfoga_bin = os.path.join('support', 'phoneinfoga.exe')
        command = f'{phoneinfoga_bin} scan -n "{phone_number or self.phone_number}"'

        if not os.path.isfile(phoneinfoga_bin):
            raise PhoneinfogaNotFoundError("Error: phoneinfoga.exe not found.")
        
        self.command_output = subprocess.check_output(command, shell=True, text=True)
        return self.command_output

    def get_google_query(self, google_search_url: str):
        """
        Extract the Google query from a Google search URL.

        Parameters:
        - google_search_url (str): The Google search URL.

        Returns:
        - str: The extracted Google query.
        """
        
        parsed_url = urlparse(google_search_url)
        query_params = parse_qs(parsed_url.query)
        
        if 'q' in query_params:
            return query_params['q'][0]
        else:
            return google_search_url
    
    def extract_scanner_googlesearch(self, command_output: str = ""):
        """
        Extract information from the output of Phoneinfoga's Google search scanner.

        Parameters:
        - command_output (str): The output of the Phoneinfoga command.

        Returns:
        - dict: Categorized information from the Google search scanner.
        """
        
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
                url_final = url_match.group(1).strip()
                google_query = self.get_google_query(url_final)
                if url_match:
                    categories[current_category].append({
                        "id": len(categories[current_category]) + 1,
                        "url": url_final,
                        "google_query": google_query
                    })

        return categories
    
    def extract_basic_info(self, command_output: str = ""):
        """
        Extract basic information from the output of Phoneinfoga.

        Parameters:
        - command_output (str): The output of the Phoneinfoga command.

        Returns:
        - dict: Basic information about the phone number.
        """
        
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
    def __init__(self, phone_number: str = None):
        """
        Initialize PhoneNumberLookup instance with an optional phone number.

        Parameters:
        - phone_number (str): The phone number to perform lookups on.
        """
        
        self.phone_number = sanitize(phone_number)
        
        """
        self.final_data = {
            'status': {
                'error': False,
                'error_desc': [],
                'show_information': True,
                'show_scanner_googlesearch': True,
            },
            'information': {
                "is_valid_number": "True",
                "can_be_internationally_dialed": "True",
                "is_carrier_specific": "False",
                "is_geographical_number": "False",
                "info": "",
                "country": "",
                "e164": "",
                "international": "",
                "isp": "",
                "local": "",
                "raw_local": "",
                "location": "",
                "number_type": "",
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
        
        self.phone_number = phone_number
        self.final_data = {
            'status': {
                'error': False,
                'error_desc': [],
                'show_information': True,
                'show_scanner_googlesearch': True,
            },
            'information': {},
            'scanner_googlesearch': {},
        }
        self.info_libphonenumber = {}
        
    
    def phoneinfoga(self):
        """
        Run Phoneinfoga scans and populate the final_data dictionary.
        """
        
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
        """
        Run Libphonenumber scan and populate the info_libphonenumber dictionary.
        """
        
        obj = Libphonenumber(self.phone_number)
        
        try:
            self.info_libphonenumber = obj.get_number_info()
            return self.info_libphonenumber
        except Exception as e:
            self.final_data['status']['error'] = True
            self.final_data['status']['error_desc'].append(f'Not showing information from "libphonenumber" scan: {e}')
            self.final_data['status']['show_information'] = False
    
    def merge_results(self):
        """
        Merge results from Phoneinfoga and Libphonenumber scans into final_data.
        """
        
        if not self.info_libphonenumber:
            self.libphonenumber()
            
        for key, value in self.info_libphonenumber.items():
            if isinstance(value, bool):
                self.final_data['information'][key] = value
            else:
                self.final_data['information'][key] = str(value)

    def run(self):
        """
        Run the complete phone number lookup process.

        Returns:
        - dict: Final data containing information from Phoneinfoga and Libphonenumber scans.
        """
        self.phoneinfoga()
        self.libphonenumber()
        self.merge_results()
        return self.final_data
    