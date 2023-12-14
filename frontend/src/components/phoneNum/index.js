// react
import React, { useState } from "react";

// mui
import Grid from "@mui/material/Grid";
import TextField from "@mui/material/TextField";
import IconButton from "@mui/material/IconButton";
import CircularProgress from "@mui/material/CircularProgress";
import Dialog from "@mui/material/Dialog";
import DialogTitle from "@mui/material/DialogTitle";

// icons
import SearchIcon from "@mui/icons-material/Search";

// my components
import ShowSecitonHeader from "../_shared/sectionHeader";
import SetSettings from "./setSettings";
import IntroInformation from "./introInfomation";
import ScannerGoogleSearch from "./scannerGoogleSearch";
import ScannerLocal from "./scannerLocal";

const PhoneNum = () => {
  const [loadingDialogOpen, setLoadingDialogOpen] = useState(false);
  const [phoneNumber, setPhoneNumber] = useState("");
  const [phoneinfogaData, setPhoneinfogaData] = useState({
    status: {
      error: false,
      error_desc: "",
      show_information: true,
      show_scanner_googlesearch: true,
    },
    information: {
      raw_local: "",
      local: "",
      e164: "",
      international: "",
      country: "",
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
      setLoadingDialogOpen(true); // Open the dialog when starting the API request

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
      setPhoneinfogaData(data);
    } catch (error) {
      console.error("Error fetching data:", error);
    } finally {
      setLoadingDialogOpen(false); // Close the dialog when API request is complete
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
        imgURL="https://raw.githubusercontent.com/sundowndev/phoneinfoga/master/docs/images/banner.png"
      />

      {/* Please Wait Message */}
      <Dialog
        open={loadingDialogOpen}
        aria-labelledby="loading-dialog-title"
        disableBackdropClick
        disableEscapeKeyDown
      >
        <DialogTitle id="loading-dialog-title">Please Wait</DialogTitle>
        <div style={{ textAlign: "center", padding: "16px" }}>
          <CircularProgress />
        </div>
      </Dialog>

      {/* Search Phone Number */}
      <SearchNumber />

      {/* SetSettings - Update API Keys */}
      <SetSettings />

      {/* Phone Number - Basic Information */}
      {phoneinfogaData.status.show_information ? (
        <>
          <h2>Number Information</h2>
          <ScannerLocal data={phoneinfogaData.information} />
        </>
      ) : null}

      {/* Google Dorks list */}
      {phoneinfogaData.status.show_scanner_googlesearch ? (
        <>
          <br />
          <hr />
          <h2>Google Dorks</h2>
          <ScannerGoogleSearch data={phoneinfogaData.scanner_googlesearch} />
        </>
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
