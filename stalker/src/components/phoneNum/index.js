import React from "react";
import SetSettings from "./setSettings";
import IntroInformation from "./introInfomation";
import Grid from "@mui/material/Grid";
import TextField from "@mui/material/TextField";
import SearchIcon from "@mui/icons-material/Search";
import IconButton from "@mui/material/IconButton";

const phoneNum = () => {
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
      <SearchNumber />
      <SetSettings />
      <br></br>
      <br></br>
      <hr></hr>
      <IntroInformation />
    </div>
  );
};

export default phoneNum;
