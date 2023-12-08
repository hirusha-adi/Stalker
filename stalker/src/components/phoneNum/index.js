import React from "react";
import SetSettings from "./setSettings";
import IntroInformation from "./introInfomation";
import ShowGoogleDorks from "./showGoogleDorks";
import Grid from "@mui/material/Grid";
import TextField from "@mui/material/TextField";
import SearchIcon from "@mui/icons-material/Search";
import IconButton from "@mui/material/IconButton";

const phoneNum = () => {
  const googleDorksList = [
    { id: 1, lastName: "Hirusha", firstName: "Jon", age: 35 },
    { id: 2, lastName: "Lannister", firstName: "Cersei", age: 42 },
    { id: 3, lastName: "Lannister", firstName: "Jaime", age: 45 },
    { id: 4, lastName: "Stark", firstName: "Arya", age: 16 },
    { id: 5, lastName: "Targaryen", firstName: "Daenerys", age: null },
    { id: 6, lastName: "Melisandre", firstName: null, age: 150 },
    { id: 7, lastName: "Clifford", firstName: "Ferrara", age: 44 },
    { id: 8, lastName: "Frances", firstName: "Rossini", age: 36 },
    { id: 9, lastName: "Roxie", firstName: "Harvey", age: 65 },
  ];

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
      <hr></hr>
      <br></br>
      <ShowGoogleDorks data={googleDorksList} />
      <br></br>
      <br></br>
      <hr></hr>
      <IntroInformation />
    </div>
  );
};

export default phoneNum;
