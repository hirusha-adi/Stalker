import requests
from urllib.parse import urlencode, quote_plus

class TestAPI:
    base_url = "http://127.0.0.1:5000"

    def check_account_lookup(self, USERNAME=None):
        url = f"{self.base_url}/account_lookup"
        data = {"USERNAME": USERNAME or "hirushaadi"}
        headers = {
            "accept": "application/json", 
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.post(
            url, 
            headers=headers, 
            data=urlencode(
                data, 
                quote_via=quote_plus
            )
        )

        print("Account Lookup Response:")
        print(response.status_code)
        print(response.text)

    def check_phone_number_information(self, PHONE_NUMBER=None):
        url = f"{self.base_url}/phone_num"
        data = {"PHONE_NUMBER": PHONE_NUMBER or "+94782386009"}
        headers = {
            "accept": "application/json", 
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.post(
            url, 
            headers=headers, 
            data=urlencode(
                data, 
                quote_via=quote_plus
            )
        )

        print("Phone Number Information Response:")
        print(response.status_code)
        print(response.text)

def main():
    tester = TestAPI()
    tester.check_account_lookup()
    tester.check_phone_number_information()

if __name__ == '__main__':
    main()
