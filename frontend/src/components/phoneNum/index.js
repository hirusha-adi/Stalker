// react
import React, { useState } from "react";

// mui
import Grid from "@mui/material/Grid";
import TextField from "@mui/material/TextField";
import IconButton from "@mui/material/IconButton";

// icons
import SearchIcon from "@mui/icons-material/Search";

// my components
import ShowSecitonHeader from "../_shared/sectionHeader";
import LoadingDialog from "../_shared/loadingDialog";
import AlertList from "../_shared/alertList";
import SetSettings from "./setSettings";
import IntroInformation from "./introInfomation";
import ScannerGoogleSearch from "./scannerGoogleSearch";
import ScannerLocal from "./scannerLocal";

const PhoneNum = () => {
  const [loading, setLoading] = useState(false);
  const [phoneNumber, setPhoneNumber] = useState("");
  const [phoneNumberData, setPhoneNumberData] = useState({
    status: {
      error: false,
      error_desc: [],
      show_information: false,
      show_scanner_googlesearch: false,
    },
    information: {
      is_valid_number: false,
      can_be_internationally_dialed: false,
      is_carrier_specific: false,
      is_geographical_number: false,
      info: "",
      country: "",
      e164: "",
      international: "",
      isp: "",
      local: "",
      raw_local: "",
      location: "",
      number_type: "",
      region_code: "",
      timezone: "",
    },
    scanner_googlesearch: {
      social_media: [],
      disposable_providers: [],
      reputation: [],
      individuals: [],
      general: [],
    },
  });

  const handleSearch = async () => {
    try {
      setLoading(true);

      const formData = new FormData();
      formData.append("PHONE_NUMBER", phoneNumber);

      const response = await fetch("/phone_num", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      setPhoneNumberData(data);
    } catch (error) {
      console.error("Error fetching data:", error);
    } finally {
      setLoading(false);
    }
  };

  const SearchNumber = () => (
    <div style={{ textAlign: "center" }}>
      <h2>Search Phone Number</h2>
      <Grid container spacing={1} alignItems="center" justifyContent="center">
        <Grid item xs={11}>
          <TextField
            id="PHONE_NUMBER"
            label="Input Phone Number"
            variant="standard"
            value={phoneNumber}
            onChange={(e) => setPhoneNumber(e.target.value)}
            fullWidth
          />
        </Grid>
        <Grid item xs={1}>
          <IconButton aria-label="delete" size="large" onClick={handleSearch}>
            <SearchIcon fontSize="inherit" />
          </IconButton>
        </Grid>
      </Grid>
    </div>
  );

  return (
    <>
      {/* Section Header */}
      <ShowSecitonHeader
        subtitle={
          <>
            Information gathering framework for phone numbers
            <br />
            <br />
            Powered by{" "}
            <a
              href="https://github.com/sundowndev/phoneinfoga"
              target="_blank"
              rel="noopener noreferrer"
            >
              Phoneinfoga
            </a>
            ,{" "}
            <a
              href="https://pypi.org/project/phonenumbers/"
              target="_blank"
              rel="noopener noreferrer"
            >
              libphonenumber
            </a>
          </>
        }
        width="70%"
        imgURL="/logo-with-text.png"
        // imgURL="https://raw.githubusercontent.com/sundowndev/phoneinfoga/master/docs/images/banner.png"
      />

      {/* Please Wait Message */}
      <LoadingDialog open={loading} text="Please Wait" />

      {/* Search Phone Number */}
      <SearchNumber />

      {/* SetSettings - Update API Keys */}
      <SetSettings />

      {/* Phone Number - Basic Information */}
      {phoneNumberData.status.show_information ? (
        <>
          <h2>Number Information</h2>
          <ScannerLocal dataList={phoneNumberData.information} />
        </>
      ) : null}

      {/* Google Dorks list */}
      {phoneNumberData.status.show_scanner_googlesearch ? (
        <>
          <br />
          <hr />
          <h2>Google Dorks</h2>
          <ScannerGoogleSearch data={phoneNumberData.scanner_googlesearch} />
        </>
      ) : null}

      {/* Before Searching and No Error */}
      {!phoneNumberData.status.error &&
        !phoneNumberData.status.show_information &&
        !phoneNumberData.status.show_scanner_googlesearch && (
          <div style={{ textAlign: "center", marginTop: "50px" }}>
            <p>Please search to show results</p>
          </div>
        )}

      {/* If an error occured */}
      {phoneNumberData.status.error ? (
        <AlertList
          severity="error"
          itemsList={phoneNumberData.status.error_desc}
        />
      ) : null}

      {/* About phoneinfoga */}
      <br />
      <br />
      <hr />
      <IntroInformation />
      <br />
      <br />
    </>
  );
};

export default PhoneNum;
