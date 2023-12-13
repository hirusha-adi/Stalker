import re
import subprocess
import os
import typing as t

class Phoneinfoga:
    def __init__(self, phone_number: str = "") -> None:
        self.phone_number = phone_number
    
    def run_command(self):
        print("\n\n")
        phoneinfoga_bin = os.path.join('bin', 'phoneinfoga.exe')
        print(phoneinfoga_bin)
        command = f'{phoneinfoga_bin} scan -n "{self.phone_number}"'
        print(command)
        print(os.path.isfile(phoneinfoga_bin))
        try:
            output = subprocess.check_output(command, shell=True, text=True)
            print(output)
        except subprocess.CalledProcessError as e:
            print(f"Error running the command: {e}")
        print("\n\n")
    
    def extract_urls(self, command_output: str) -> t.Dict[str, t.List[t.Dict[str, t.Union[int, str]]]]:
        categories = {
            "social_media": [],
            "disposable_providers": [],
            "reputation": [],
            "individuals": [],
            "general": []
        }
        current_category = ""

        lines = command_output.split('\n')

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
    
    def extract_basic_info(self):
        pass

class PhoneNumberLookup:
    def test(number) -> None:
        obj = Phoneinfoga(number)
        obj.run_command()

if __name__ == "__main__":
    obj = Phoneinfoga("+94713395547")
    obj.run_command()