import re
import subprocess
import os
import typing as t

class Phoneinfoga:
    def __init__(self, phone_number: str = ""):
        self.phone_number = phone_number
        self.command_output = ""
    
    def run_command(self, phone_number: str = ""):
        
        phoneinfoga_bin = os.path.join('bin', 'phoneinfoga.exe')
        command = f'{phoneinfoga_bin} scan -n "{phone_number or self.phone_number}"'

        if not os.path.isfile(phoneinfoga_bin):
            print("Error: phoneinfoga.exe not found.")
            return None
        
        try:
            self.command_output = subprocess.check_output(command, shell=True, text=True)
            print(self.command_output)
            return self.command_output
        except subprocess.CalledProcessError as e:
            print(f"Error running the command: {e}")
            return None
    
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
        
        self.final_data = {
        'status': {
        'error': False,
        'error_desc': "",
        'show_information': True,
        'show_GoogleDorks': True,
      },
    #   'information': {
    #     'raw_local': "",
    #     'local': "",
    #     'e164': "",
    #     'international': "",
    #     'country': ""
    #   },
    #   'scanner_googlesearch': {
    #         "social_media": [],
    #         "disposable_providers": [],
    #         "reputation": [],
    #         "individuals": [],
    #         "general": []
    #     }
    }
    
    def phoneinfoga(self):
        obj = Phoneinfoga(self.phone_number)
        obj.run_command()
        self.final_data['scanner_googlesearch'] = obj.extract_scanner_googlesearch()
        self.final_data['information'] = obj.extract_basic_info()
    
    def run(self):
        self.phoneinfoga()
        return self.final_data
    