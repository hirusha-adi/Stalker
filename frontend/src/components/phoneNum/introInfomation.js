// react
import React from "react";

// mui
import Grid from "@mui/material/Grid";
import { Paper, Typography } from "@mui/material";

// my components
import CollapsibleSection from "../_shared/collapsibleSection";

const FeaturesList = ({ title, items }) => {
  const generateListItems = () => {
    return items.map((item, index) => <li>{item}</li>);
  };

  return (
    <>
      <h3>{title}</h3>
      <ul>{generateListItems()}</ul>
    </>
  );
};

const ScannersInformation = () => {
  const ScannerLocal = () => (
    <Paper elevation={3} style={{ padding: "16px" }}>
      <Typography variant="h6" gutterBottom>
        Local
      </Typography>
      <p>
        The local scan is probably the simplest scan of PhoneInfoga. By default,
        the tool statically parse the phone number and convert it to several
        formats, it also tries to recognize the country and the carrier. This
        information are passed to all scanners in order to provide further
        analysis. The local scanner simply return those information to the end
        user, so they can exploit it as well.
        <br />
        <br />
        Example output:
      </p>
      <Paper
        style={{ backgroundColor: "#f5f5f5", padding: "16px" }}
        elevation={3}
      >
        $ phoneinfoga scan -n +4176418xxxx
        <br />
        <br />
        Raw local: 076418xxxx
        <br />
        Local: 076 418 xx xx
        <br />
        E164: +4176418xxxx
        <br />
        International: 4176418xxxx
        <br />
        Country: CH
      </Paper>
    </Paper>
  );

  const ScannerNumverify = () => (
    <Paper elevation={3} style={{ padding: "16px" }}>
      <Typography variant="h6" gutterBottom>
        Numverify
      </Typography>
      <p>
        Numverify provide standard but useful information such as country code,
        location, line type and carrier. This scanners requires an API-key which
        you can get on their website after creating an account. You can use a
        free API key as long as you don't exceed the monthly quota. This is an{" "}
        <a href="https://apilayer.com/marketplace/number_verification-api">
          apilayer key
        </a>
        , not numverify itself.
        <br />
        <br />
        Example output:
      </p>
      <ol>
        <li>
          Go to the <a href="https://apilayer.com/">Api layer website</a> and
          create an account
        </li>
        <li>
          Go to "Number Verification API" in the marketplace, click on
          "Subscribe for free", then choose whatever plan you want
        </li>
        <li>Copy the new API token and update it using this webpage</li>
      </ol>
      <Paper
        style={{ backgroundColor: "#f5f5f5", padding: "16px" }}
        elevation={3}
      >
        $ NUMVERIFY_API_KEY={"<key>"} phoneinfoga scan -n +4176418xxxx
        <br />
        <br />
        Results for numverify
        <br />
        Valid: true
        <br />
        Number: 4176418xxxx
        <br />
        Local format: 076418xxxx
        <br />
        International format: +4176418xxxx
        <br />
        Country prefix: +41
        <br />
        Country code: CH
        <br />
        Country name: Switzerland (Confederation of)
        <br />
        Carrier: Sunrise Communications AG
        <br />
        Line type: mobile
        <br />
      </Paper>
    </Paper>
  );

  const Googlesearch = () => (
    <Paper elevation={3} style={{ padding: "16px" }}>
      <Typography variant="h6" gutterBottom>
        Googlesearch
      </Typography>
      <p>
        Googlesearch uses the Google search engine and{" "}
        <a href="https://en.wikipedia.org/wiki/Google_hacking">Google Dorks</a>{" "}
        to search phone number's footprints everywhere on the web. It allows you
        to search for scam reports, social media profiles, documents and more.
        This scanner does only one thing: generating several Google search links
        from a given phone number. You then have to manually open them in your
        browser to see results. So the tool may generate links that do not
        return any result. This is a design choice we made to avoid technical
        limitation around{" "}
        <a href="https://en.wikipedia.org/wiki/Search_engine_scraping">
          Google scraping
        </a>{" "}
        .
        <br />
        <br />
        Output Example: a list of categorized google dorks urls
        <br />
      </p>
    </Paper>
  );

  const Googlecse = () => (
    <Paper elevation={3} style={{ padding: "16px" }}>
      <Typography variant="h6" gutterBottom>
        Googlecse
      </Typography>
      <p>
        Google custom search is a Google product allowing users to create
        Programmable Search Engines for programmatic usage. This scanner takes
        an existing search engine you created to perform search queries on a
        given phone number. Custom Search JSON API provides 100 search queries
        (~50 scans) per day for free. If you need more, you may sign up for
        billing in the API Console. Additional requests cost $5 per 1000 queries
        (~500 scans), up to 10k queries per day (~5000 scans).
        <br />
        <br />
        Follow the steps below to create a new search engine :
      </p>
      <ol>
        <li>
          Go to{" "}
          <a href="https://console.cloud.google.com/apis/api/customsearch.googleapis.com/metrics">
            GCP Console
          </a>{" "}
          and enable the custom search API.
        </li>
        <li>
          Go to the{" "}
          <a href="https://console.cloud.google.com/apis/credentials">
            credentials page
          </a>{" "}
          and create a new API token. You can restrict this token to the Custom
          Search API.
        </li>
        <li>
          <a href="https://programmablesearchengine.google.com/controlpanel/all">
            Follow this link
          </a>{" "}
          and click on "Add" to create a new search engine.
        </li>
        <li>Fill the form and make sure you select "Search the entire web".</li>
        <li>
          Use the Search Engine ID and the API token to configure the scanner as
          per the configuration tab below.
        </li>
      </ol>
      <Paper
        style={{ backgroundColor: "#f5f5f5", padding: "16px" }}
        elevation={3}
      >
        $ phoneinfoga scan -n +1241325xxxx
        <br />
        <br />
        Results for googlecse
        <br />
        Homepage: https://cse.google.com/cse?cx={"<redacted>"}
        <br />
        Result count: 1
        <br />
        Items:
        <br />
        Title: Info about +1241325xxxx
        <br />
        URL: https://example.com/1241325xxxx
        <br />
      </Paper>
    </Paper>
  );

  const OVH = () => (
    <Paper elevation={3} style={{ padding: "16px" }}>
      <Typography variant="h6" gutterBottom>
        OVH
      </Typography>
      <p>
        OVH, besides being a web and cloud hosting company, is a telecom
        provider with several VoIP numbers in Europe. Thanks to their API-key
        free REST API, we are able to tell if a number is owned by OVH Telecom
        or not.
      </p>
      <Paper
        style={{ backgroundColor: "#f5f5f5", padding: "16px" }}
        elevation={3}
      >
        $ phoneinfoga scan -n +3336517xxxx
        <br />
        <br />
        Results for ovh
        <br />
        Found: true
        <br />
        Number range: 036517xxxx
        <br />
        City: Abbeville
        <br />
      </Paper>
    </Paper>
  );

  return (
    <>
      <ScannerLocal />
      <br />
      <ScannerNumverify />
      <br />
      <Googlesearch />
      <br />
      <Googlecse />
      <br />
      <OVH />
    </>
  );
};

const IntroInformation = () => {
  const features = [
    "Check if phone number exists",
    "Gather basic information such as country, line type, and carrier",
    "OSINT footprinting using external APIs, phone books & search engines",
    "Check for reputation reports, social media, disposable numbers, and more",
  ];

  const anti_features = [
    "Does not claim to provide relevant or verified data, it's just a tool!",
    "Does not allow to 'track' a phone or its owner in real time",
    "Does not allow to get the precise phone location",
    "Does not allow to hack a phone",
  ];

  const AboutBasic = () => (
    <div>
      <h2>Phoneinfoga</h2>
      <p>
        PhoneInfoga is one of the most advanced tools to scan international
        phone numbers. It allows you to first gather basic information such as
        country, area, carrier and line type, then use various techniques to try
        to find the VoIP provider or identify the owner. It works with a
        collection of scanners that must be configured in order for the tool to
        be effective. PhoneInfoga doesn't automate everything, it's just there
        to help investigating on phone numbers.
      </p>
    </div>
  );

  const AboutLibphonenumber = () => (
    <>
      <h2>libphonenumber</h2>
      <p>
        PhoneInfoga is one of the most advanced tools to scan international
        phone numbers. It allows you to first gather basic information such as
        country, area, carrier and line type, then use various techniques to try
        to find the VoIP provider or identify the owner. It works with a
        collection of scanners that must be configured in order for the tool to
        be effective. PhoneInfoga doesn't automate everything, it's just there
        to help investigating on phone numbers.
        <br />
        What i use here is is the{" "}
        <a href="https://pypi.org/project/phonenumbers/">Python version</a> of
        Google's common library for parsing, formatting, storing and validating
        international phone numbers.
      </p>
    </>
  );

  const FeaturesAntiFeatures = () => (
    <Grid container spacing={2}>
      <Grid
        item
        xs={6}
        sx={{
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <FeaturesList title="Features" items={features} />
      </Grid>
      <Grid
        item
        xs={6}
        sx={{
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <FeaturesList title="Anti-features" items={anti_features} />
      </Grid>
    </Grid>
  );

  const CreditsBasic = () => (
    <>
      <h3>
        <a
          href="https://github.com/sundowndev/phoneinfoga"
          target="_blank"
          rel="noreferrer"
        >
          Click here
        </a>{" "}
        to open the Github repository
      </h3>
      <br></br>
    </>
  );

  return (
    <>
      <br />
      <CollapsibleSection title="About" headerSize={2} isCollapsed={true}>
        <AboutBasic />
        <FeaturesAntiFeatures />
        <CreditsBasic />
        <h3>Available Scanners</h3>
        <ScannersInformation />
        <br />
        <AboutLibphonenumber />
        <br />
      </CollapsibleSection>
    </>
  );
};

export default IntroInformation;
