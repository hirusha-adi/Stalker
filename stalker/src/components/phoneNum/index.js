// react
import React from "react";

// mui
import Grid from "@mui/material/Grid";
import TextField from "@mui/material/TextField";
import IconButton from "@mui/material/IconButton";

// icons
import SearchIcon from "@mui/icons-material/Search";

// my components
import SetSettings from "./setSettings";
import IntroInformation from "./introInfomation";
import ScannerGoogleSearch from "./scannerGoogleSearch";
import ScannerLocal from "./scannerLocal";

const phoneNum = () => {
  const phoneinfogaData = {
    status: {
      error: false,
      error_desc: "",
      show_information: true,
      show_GoogleDorks: true,
    },
    information: {
      rawLocal: "0713395547",
      local: "071 339 5547",
      e164: "+94713395547",
      international: "94713395547",
      country: "LK",
    },
    googleDorks: {
      socialMedia: [
        { id: 1, lastName: "Hirusha", firstName: "Jon", age: 35 },
        { id: 2, lastName: "Hirusha", firstName: "Jon", age: 35 },
      ],
      disposableProviders: [
        { id: 5, lastName: "Targaryen", firstName: "Daenerys", age: null },
        { id: 6, lastName: "Targaryen", firstName: "Daenerys", age: null },
      ],
      reputation: [
        { id: 2, lastName: "Lannister", firstName: "Cersei", age: 42 },
        { id: 3, lastName: "Lannister", firstName: "Cersei", age: 42 },
      ],
      individuals: [
        { id: 4, lastName: "Hirusha", firstName: "Jon", age: 35 },
        { id: 5, lastName: "Hirusha", firstName: "Jon", age: 35 },
      ],
      general: [
        { id: 8, lastName: "Stark", firstName: "Arya", age: 16 },
        { id: 9, lastName: "Stark", firstName: "Arya", age: 16 },
      ],
    },
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
            fullWidth
          />
        </Grid>
        <Grid item xs={1}>
          <IconButton aria-label="delete" size="large">
            <SearchIcon fontSize="inherit" />
          </IconButton>
        </Grid>
      </Grid>
    </div>
  );

  return (
    <div>
      <br></br>

      {/* Phoneinfoga logo */}
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <img
          src="https://raw.githubusercontent.com/sundowndev/phoneinfoga/master/docs/images/banner.png"
          alt="banner"
          style={{ alignSelf: "center", width: "70%" }}
        />
      </div>
      <br></br>

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
      {phoneinfogaData.status.show_GoogleDorks ? (
        <>
          <br></br>
          <hr></hr>
          <h2>Google Dorks</h2>
          <ScannerGoogleSearch data={phoneinfogaData.googleDorks} />
        </>
      ) : null}

      {/* About phoneinfoga */}
      <br></br>
      <br></br>
      <hr></hr>
      <IntroInformation />
      <br></br>
      <br></br>
    </div>
  );
};

export default phoneNum;
