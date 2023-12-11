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
    {
      id: 2,
      username: "hirushaadi",
      name: "Chess",
      url_main: "https://www.chess.com/",
      url_user: "https://www.chess.com/member/hirushaadi",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "12.20299999999952",
    },
    {
      id: 3,
      username: "hirushaadi",
      name: "Codewars",
      url_main: "https://www.codewars.com",
      url_user: "https://www.codewars.com/users/hirushaadi",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "16.64099999999962",
    },
    {
      id: 4,
      username: "hirushaadi",
      name: "DEV Community",
      url_main: "https://dev.to/",
      url_user: "https://dev.to/hirushaadi",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "15.20299999999952",
    },
    {
      id: 5,
      username: "hirushaadi",
      name: "DeviantART",
      url_main: "https://deviantart.com",
      url_user: "https://hirushaadi.deviantart.com",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "18.17199999999866",
    },
    {
      id: 6,
      username: "hirushaadi",
      name: "Docker Hub",
      url_main: "https://hub.docker.com/",
      url_user: "https://hub.docker.com/u/hirushaadi/",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "16.59399999999914",
    },
    {
      id: 7,
      username: "hirushaadi",
      name: "G2G",
      url_main: "https://www.g2g.com/",
      url_user: "https://www.g2g.com/hirushaadi",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "20.936999999999898",
    },
    {
      id: 8,
      username: "hirushaadi",
      name: "Imgur",
      url_main: "https://imgur.com/",
      url_user: "https://imgur.com/user/hirushaadi",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "31.53099999999904",
    },
    {
      id: 9,
      username: "hirushaadi",
      name: "LeetCode",
      url_main: "https://leetcode.com/",
      url_user: "https://leetcode.com/hirushaadi",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "34.76599999999962",
    },
    {
      id: 10,
      username: "hirushaadi",
      name: "Lichess",
      url_main: "https://lichess.org",
      url_user: "https://lichess.org/@/hirushaadi",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "34.48400000000038",
    },
    {
      id: 11,
      username: "hirushaadi",
      name: "Lolchess",
      url_main: "https://lolchess.gg/",
      url_user: "https://lolchess.gg/profile/na/hirushaadi",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "36.60900000000038",
    },
    {
      id: 12,
      username: "hirushaadi",
      name: "Medium",
      url_main: "https://medium.com/",
      url_user: "https://medium.com/@hirushaadi",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "48.75",
    },
    {
      id: 13,
      username: "hirushaadi",
      name: "Reddit",
      url_main: "https://www.reddit.com/",
      url_user: "https://www.reddit.com/user/hirushaadi",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "55.26599999999962",
    },
    {
      id: 14,
      username: "hirushaadi",
      name: "Snapchat",
      url_main: "https://www.snapchat.com",
      url_user: "https://www.snapchat.com/add/hirushaadi",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "60.23400000000038",
    },
    {
      id: 15,
      username: "hirushaadi",
      name: "Telegram",
      url_main: "https://t.me/",
      url_user: "https://t.me/hirushaadi",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "65.375",
    },
    {
      id: 16,
      username: "hirushaadi",
      name: "Tenor",
      url_main: "https://tenor.com/",
      url_user: "https://tenor.com/users/hirushaadi",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "65.95299999999952",
    },
    {
      id: 17,
      username: "hirushaadi",
      name: "TikTok",
      url_main: "https://tiktok.com/",
      url_user: "https://tiktok.com/@hirushaadi",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "68.40599999999904",
    },
    {
      id: 18,
      username: "hirushaadi",
      name: "TryHackMe",
      url_main: "https://tryhackme.com/",
      url_user: "https://tryhackme.com/p/hirushaadi",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "82.32799999999952",
    },
    {
      id: 19,
      username: "hirushaadi",
      name: "Twitter",
      url_main: "https://twitter.com/",
      url_user: "https://twitter.com/hirushaadi",
      exists: "Claimed",
      http_status: "403",
      response_time_s: "110.21899999999914",
    },
    {
      id: 20,
      username: "hirushaadi",
      name: "Unsplash",
      url_main: "https://unsplash.com/",
      url_user: "https://unsplash.com/@hirushaadi",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "70.75",
    },
    {
      id: 21,
      username: "hirushaadi",
      name: "Virgool",
      url_main: "https://virgool.io/",
      url_user: "https://virgool.io/@hirushaadi",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "76.0619999999999",
    },
    {
      id: 22,
      username: "hirushaadi",
      name: "VirusTotal",
      url_main: "https://www.virustotal.com/",
      url_user: "https://www.virustotal.com/gui/user/hirushaadi",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "72.65599999999904",
    },
    {
      id: 23,
      username: "hirushaadi",
      name: "Whonix Forum",
      url_main: "https://forums.whonix.org/",
      url_user: "https://forums.whonix.org/u/hirushaadi/summary",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "75.07799999999952",
    },
    {
      id: 24,
      username: "hirushaadi",
      name: "mastodon.social",
      url_main: "https://chaos.social/",
      url_user: "https://mastodon.social/@hirushaadi",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "88.17200000000048",
    },
    {
      id: 25,
      username: "hirushaadi",
      name: "metacritic",
      url_main: "https://www.metacritic.com/",
      url_user: "https://www.metacritic.com/user/hirushaadi",
      exists: "Claimed",
      http_status: "200",
      response_time_s: "89.6869999999999",
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
