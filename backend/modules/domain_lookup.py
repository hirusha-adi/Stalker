import whois
import tldextract

class DomainLookup:
    def __init__(self, user_input, alternatives: bool = False):
        self.COMMON_TLDS = [
            "com", "net", "org", "info", "biz",
            "us", "uk", "ca", "au", "de",
            "fr", "it", "es", "nl", "eu",
            "be", "ch", "at", "dk", "se",
            "no", "fi", "jp", "cn", "in", 
            "lk"
        ]
        
        self.alternatives = alternatives
        tld_extract_result = tldextract.extract(user_input)
        self.domain = tld_extract_result.domain
        self.subdomain = tld_extract_result.subdomain 
        self.tld = tld_extract_result.suffix    
        self.is_private = tld_extract_result.is_private

        self.all_domain_list = []
        self.generate_all_domain_list()
    
    def generate_all_domain_list(self):
        if self.tld:
            if self.subdomain:
                self.all_domain_list.append(f"{self.subdomain}.{self.domain}.{self.tld}")
            else:
                self.all_domain_list.append(f"{self.domain}.{self.tld}")

        if self.alternatives:
            for tld in self.COMMON_TLDS:
                self.all_domain_list.append(f"{self.domain}.{tld}")
                if self.subdomain:
                    self.all_domain_list.append(f"{self.subdomain}.{self.domain}.{tld}")
                    try:
                        full_subdomain = str(self.subdomain)
                        if '.' in full_subdomain:
                            subdomains = full_subdomain.split('.')
                            for subdomain in subdomains:
                                self.all_domain_list.append(f"{subdomain}.{self.domain}.{tld}")
                    except:
                        pass
   
    def check_whois(self, domain):
        try:
            whois_info = whois.whois(domain)
            return whois_info
        except whois.parser.PywhoisError:
            return None

    def lookup_all_domains(self):
        for domain in self.all_domain_list:
            whois_info = self.check_whois(domain=domain)
            if whois_info:
                print(f"Domain {domain} exists with the following details:")
                print(whois_info)
            else:
                print(f"Domain {domain} does not exist.")
        
# Example usage:
if __name__ == "__main__":
    domain_lookup = DomainLookup("hirusha.xyz", alternatives=False)
    domain_lookup.lookup_all_domains()
