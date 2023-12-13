import re

phoneinfoga_output  = """
Running scan for phone number +94713395547...

Results for googlesearch
Social media:
        URL: https://www.google.com/search?q=site%3Afacebook.com+intext%3A%2294713395547%22+%7C+intext%3A%22%2B94713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Atwitter.com+intext%3A%2294713395547%22+%7C+intext%3A%22%2B94713395547%22+%7C+intext%3A%220713395547%22 

        URL: https://www.google.com/search?q=site%3Alinkedin.com+intext%3A%2294713395547%22+%7C+intext%3A%22%2B94713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Ainstagram.com+intext%3A%2294713395547%22+%7C+intext%3A%22%2B94713395547%22+%7C+intext%3A%220713395547%22      

        URL: https://www.google.com/search?q=site%3Avk.com+intext%3A%2294713395547%22+%7C+intext%3A%22%2B94713395547%22+%7C+intext%3A%220713395547%22
Disposable providers:
        URL: https://www.google.com/search?q=site%3Ahs3x.com+intext%3A%2294713395547%22

        URL: https://www.google.com/search?q=site%3Areceive-sms-now.com+intext%3A%2294713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Asmslisten.com+intext%3A%2294713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Asmsnumbersonline.com+intext%3A%2294713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Afreesmscode.com+intext%3A%2294713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Acatchsms.com+intext%3A%2294713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Asmstibo.com+intext%3A%2294713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Asmsreceiving.com+intext%3A%2294713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Agetfreesmsnumber.com+intext%3A%2294713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Asellaite.com+intext%3A%2294713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Areceive-sms-online.info+intext%3A%2294713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Areceivesmsonline.com+intext%3A%2294713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Areceive-a-sms.com+intext%3A%2294713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Asms-receive.net+intext%3A%2294713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Areceivefreesms.com+intext%3A%2294713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Areceive-sms.com+intext%3A%2294713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Areceivetxt.com+intext%3A%2294713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Afreephonenum.com+intext%3A%2294713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Afreesmsverification.com+intext%3A%2294713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Areceive-sms-online.com+intext%3A%2294713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Asmslive.co+intext%3A%2294713395547%22+%7C+intext%3A%220713395547%22
Reputation:
        URL: https://www.google.com/search?q=site%3Awhosenumber.info+intext%3A%22%2B94713395547%22+intitle%3A%22who+called%22

        URL: https://www.google.com/search?q=intitle%3A%22Phone+Fraud%22+intext%3A%2294713395547%22+%7C+intext%3A%22%2B94713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Afindwhocallsme.com+intext%3A%22%2B94713395547%22+%7C+intext%3A%2294713395547%22

        URL: https://www.google.com/search?q=site%3Ayellowpages.ca+intext%3A%22%2B94713395547%22

        URL: https://www.google.com/search?q=site%3Aphonenumbers.ie+intext%3A%22%2B94713395547%22

        URL: https://www.google.com/search?q=site%3Awho-calledme.com+intext%3A%22%2B94713395547%22

        URL: https://www.google.com/search?q=site%3Ausphonesearch.net+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Awhocalled.us+inurl%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Aquinumero.info+intext%3A%220713395547%22+%7C+intext%3A%2294713395547%22

        URL: https://www.google.com/search?q=site%3Auk.popularphotolook.com+inurl%3A%220713395547%22
Individuals:
        URL: https://www.google.com/search?q=site%3Anuminfo.net+intext%3A%2294713395547%22+%7C+intext%3A%22%2B94713395547%22+%7C+intext%3A%220713395547%22        

        URL: https://www.google.com/search?q=site%3Async.me+intext%3A%2294713395547%22+%7C+intext%3A%22%2B94713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Awhocallsyou.de+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Apastebin.com+intext%3A%2294713395547%22+%7C+intext%3A%22%2B94713395547%22+%7C+intext%3A%220713395547%22       

        URL: https://www.google.com/search?q=site%3Awhycall.me+intext%3A%2294713395547%22+%7C+intext%3A%22%2B94713395547%22+%7C+intext%3A%220713395547%22

        URL: https://www.google.com/search?q=site%3Alocatefamily.com+intext%3A%2294713395547%22+%7C+intext%3A%22%2B94713395547%22+%7C+intext%3A%220713395547%22   

        URL: https://www.google.com/search?q=site%3Aspytox.com+intext%3A%220713395547%22
General:
        URL: https://www.google.com/search?q=intext%3A%2294713395547%22+%7C+intext%3A%22%2B94713395547%22+%7C+intext%3A%220713395547%22+%7C+intext%3A%22071+339+5547%22

        URL: https://www.google.com/search?q=%28ext%3Adoc+%7C+ext%3Adocx+%7C+ext%3Aodt+%7C+ext%3Apdf+%7C+ext%3Artf+%7C+ext%3Asxw+%7C+ext%3Apsw+%7C+ext%3Appt+%7C+ext%3Apptx+%7C+ext%3Apps+%7C+ext%3Acsv+%7C+ext%3Atxt+%7C+ext%3Axls%29+intext%3A%2294713395547%22+%7C+intext%3A%22%2B94713395547%22+%7C+intext%3A%220713395547%22   

Results for local
Raw local: 0713395547
Local: 071 339 5547
E164: +94713395547
International: 94713395547
Country: LK

2 scanner(s) succeeded
"""

def categorize_urls(input_string):
    categories = {
        "social_media": [],
        "disposable_providers": [],
        "reputation": [],
        "individuals": [],
        "general": []
    }
    current_category = None

    lines = input_string.split('\n')
    for line in lines:
        if line.strip().startswith("Social media:"):
            current_category = "social_media"
        elif line.strip().startswith("Disposable providers:"):
            current_category = "disposable_providers"
        elif line.strip().startswith("Reputation:"):
            current_category = "reputation"
        elif line.strip().startswith("Individuals:"):
            current_category = "individuals"
        elif line.strip().startswith("General:"):
            current_category = "general"
        elif line.strip().startswith("URL:"):
            url_match = re.search(r'URL:\s+(.*)', line)
            if url_match:
                categories[current_category].append(url_match.group(1).strip())

    return categories

result = categorize_urls(phoneinfoga_output)
print(result)