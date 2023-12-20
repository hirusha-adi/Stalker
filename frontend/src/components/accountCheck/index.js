// react
import React, { useState } from "react";

// mui
import Grid from "@mui/material/Grid";
import TextField from "@mui/material/TextField";
import IconButton from "@mui/material/IconButton";
import Button from "@mui/material/Button";
import DeleteIcon from "@mui/icons-material/Delete";
import Stack from "@mui/material/Stack";

// icons
import SearchIcon from "@mui/icons-material/Search";

// my components
import IntroInformation from "./introInfomation";
import SetSettings from "./setSettings";
import AvailableAccountsTable from "./listAccounts";
import ShowSecitonHeader from "../_shared/sectionHeader";
import LoadingDialog from "../_shared/loadingDialog";
import AlertList from "../_shared/alertList";

const AccountCheck = () => {
  const [loading, setLoading] = useState(false);
  const [userName, setuserName] = useState("");
  const [dataAccounts, setdataAccounts] = useState({
    status: {
      error: false,
      error_desc: [],
      show_accounts_custom: false,
      total_accounts: 0,
    },
    found_accounts: [
      // {
      //   id: 1,
      //   username: "hirushaadi",
      //   name: "Anilist",
      //   url_main: "https://anilist.co/",
      //   url_user: "https://anilist.co/user/hirushaadi/",
      //   exists: "Claimed",
      //   http_status: "200",
      //   response_time_s: "4.281000000000859",
      // },
    ],
  });

  const handleSearch = async () => {
    try {
      setLoading(true);

      const formData = new FormData();
      formData.append("USERNAME", userName);

      const response = await fetch("/account_lookup", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      setdataAccounts(data);
    } catch (error) {
      console.error("Error fetching data:", error);
    } finally {
      setLoading(false);
    }
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
            value={userName}
            onChange={(e) => setuserName(e.target.value)}
            fullWidth
          />
        </Grid>
        <Grid item xs={1}>
          <IconButton aria-label="search" size="large" onClick={handleSearch}>
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
        subtitle={
          <>
            Hunt down social media accounts by username across social networks
            <br />
            <br />
            Powered by{" "}
            <a
              href="https://github.com/sherlock-project/sherlock"
              target="_blank"
              rel="noopener noreferrer"
            >
              Sherlock
            </a>
          </>
        }
        width="70%"
        imgURL="/logo-with-text.png"
        // imgURL="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png"
      />

      {/* Please Wait Message */}
      <LoadingDialog open={loading} text="Please Wait" />

      {/* Search Bar (also includes the search button) */}
      <SearchUsername />

      {/* Advanced Settings */}
      <SetSettings />

      {/* Clear + Update Buttons */}
      <ButtonsSubmitClear />

      {/* Custom Search Results */}
      {dataAccounts.status.show_accounts_custom ? (
        <>
          <br />
          <br />
          <hr />
          <h2>Available Accounts</h2>
          <AvailableAccountsTable
            title="Sherlock"
            rows={dataAccounts.found_accounts}
          />
        </>
      ) : null}

      {/* Before Searching and No Error */}
      {!dataAccounts.status.error &&
        !dataAccounts.status.show_accounts_custom && (
          <div style={{ textAlign: "center", marginTop: "50px" }}>
            <p>Please search to show results</p>
          </div>
        )}

      {/* If an error occured */}
      {dataAccounts.status.error ? (
        <AlertList
          severity="error"
          itemsList={dataAccounts.status.error_desc}
        />
      ) : null}

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
