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
import AvailableAccountsTable from "./listAccounts";
import ShowSecitonHeader from "../_shared/sectionHeader";

import Button from "@mui/material/Button";
import DeleteIcon from "@mui/icons-material/Delete";
import Stack from "@mui/material/Stack";

const AccountCheck = () => {
  const dataSherlock = [
    {
      id: 1,
      username: "hirushaadi",
      name: "Anilist",
      url_main: "https://anilist.co/",
      url_user: "https://anilist.co/user/hirushaadi/",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "4.281000000000859",
    },
  ];

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
      <Button variant="outlined" color="error" startIcon={<DeleteIcon />}>
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
      <ShowSecitonHeader
        subtitle="Hunt down social media accounts by username across social networks"
        width="20%"
        imgURL="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png"
      />

      {/* Search Bar (also includes the search button) */}
      <SearchUsername />

      {/* Advanced Settings */}
      <SetSettings />

      {/* Clear + Update Buttons */}
      <ButtonsSubmitClear />

      {/* Sherlock Results */}
      <br />
      <br />
      <hr />
      <h2>Available Accounts</h2>
      <AvailableAccountsTable title="Sherlock" rows={dataSherlock} />

      {/* About sherlock */}
      <br />
      <br />
      <hr />
      <IntroInformation />
      <br />
      <br />
    </div>
  );
};

export default AccountCheck;
