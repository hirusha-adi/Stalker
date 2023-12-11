// react
import React from "react";

// mui
import Grid from "@mui/material/Grid";
import TextField from "@mui/material/TextField";
import IconButton from "@mui/material/IconButton";

// icons
import SearchIcon from "@mui/icons-material/Search";

// my components
import IntroInformation from "./introInfomation";
import SetSettings from "./setSettings";

const AccountCheck = () => {
  const phoneinfogaData = {
    status: {
      error: false,
      error_desc: "",
      show_information: true,
    },
    accountsList: {},
  };

  const SearchUsername = () => (
    <div style={{ textAlign: "center" }}>
      <h2>Search Username</h2>
      <Grid container spacing={1} alignItems="center" justifyContent="center">
        <Grid item xs={11}>
          <TextField
            id="USERNAME"
            label="Input Username"
            variant="standard"
            fullWidth
          />
        </Grid>
        <Grid item xs={1}>
          <IconButton aria-label="search" size="large">
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
          src="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png"
          alt="banner"
          style={{ alignSelf: "center", width: "20%" }}
        />
        <br></br>
      </div>
      <br></br>
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <h3>
          Hunt down social media accounts by username across social networks
        </h3>
      </div>
      <br></br>

      {/* Search Username */}

      <SearchUsername />
      <br />
      <SetSettings />

      {/* About sherlock */}
      <br></br>
      <br></br>
      <hr></hr>
      <IntroInformation />
      <br></br>
      <br></br>
    </div>
  );
};

export default AccountCheck;
