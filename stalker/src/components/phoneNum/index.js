import React from "react";
import SetSettings from "./setSettings";
import IntroInformation from "./introInfomation";
import ShowGoogleDorks from "./showGoogleDorks";
import Grid from "@mui/material/Grid";
import TextField from "@mui/material/TextField";
import SearchIcon from "@mui/icons-material/Search";
import IconButton from "@mui/material/IconButton";

const phoneNum = () => {
  const googleDorksData = {
    isAllEmpty: true,
    socialMedia: [
      // { id: 1, lastName: "Hirusha", firstName: "Jon", age: 35 },
    ],
    disposableProviders: [
      // { id: 5, lastName: "Targaryen", firstName: "Daenerys", age: null },
    ],
    reputation: [
      // { id: 2, lastName: "Lannister", firstName: "Cersei", age: 42 },
    ],
    individuals: [
      // { id: 1, lastName: "Hirusha", firstName: "Jon", age: 35 },
    ],
    general: [
      // { id: 4, lastName: "Stark", firstName: "Arya", age: 16 },
    ],
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
      {!googleDorksData.isAllEmpty ? (
        <>
          <br></br>
          <hr></hr>
          <h2>Google Dorks</h2>
          <br></br>
          <ShowGoogleDorks data={googleDorksData} />
        </>
      ) : null}
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
