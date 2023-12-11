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


import Button from "@mui/material/Button";
import DeleteIcon from "@mui/icons-material/Delete";
import Stack from "@mui/material/Stack";

const ShowSecitonHeader = () => (
  <>
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
  </>
);

const AccountCheck = () => {
  // const phoneinfogaData = {
  //   status: {
  //     error: false,
  //     error_desc: "",
  //     show_information: true,
  //   },
  //   accountsList: {},
  // };

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

  const ButtonsSubmitClear = () => (
    <Stack
      direction="row"
      spacing={2}
      sx={{
        p: 2,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <Button
        variant="outlined"
        color="error"
        startIcon={<DeleteIcon />}
      >
        Clear
      </Button>
      <Button variant="contained" endIcon={<SearchIcon />}>
        Search
      </Button>
    </Stack>
  );

  return (
    <div>
      {/* Section Header */}
      <ShowSecitonHeader />

      {/* Search Bar (also includes the search button) */}
      <SearchUsername />

      {/* Advanced Settings */}
      <SetSettings />

      {/* Clear + Update Buttons */}
      <ButtonsSubmitClear />

      {/* About sherlock */}
      <br /><br /><hr />
      <IntroInformation />
      <br /><br />
    </div>
  );
};

export default AccountCheck;
