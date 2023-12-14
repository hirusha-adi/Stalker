import phonenumbers as pnumb
from phonenumbers import parse
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

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
            "international_format": pnumb.normalize_digits_only(parsing),
            "national_format": pnumb.national_significant_number(parsing),
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

x = Libphonenumber("+94713395547")
phone_info = x.get_number_info()
for key, value in phone_info.items():
    print(f"{key}: {value}")