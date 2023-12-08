import React, { useState } from "react";
import Collapse from "@mui/material/Collapse";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import IconButton from "@mui/material/IconButton";
import ExpandLessIcon from "@mui/icons-material/ExpandLess";
import Grid from "@mui/material/Grid";
// import List from "@mui/material/List";
// import ListItem from "@mui/material/ListItem";
// import ListItemText from "@mui/material/ListItemText";

const ListDense = ({ title, items }) => {
  const generateListItems = () => {
    return items.map((item, index) => (
      //   <ListItem key={index}>
      //     <ListItemText primary={item} />
      //   </ListItem>
      <li>{item}</li>
    ));
  };

  return (
    //   <ListItem>
    //     <ListItemText primary={title} />
    //   </ListItem>
    //   {generateListItems()}
    // </List>
    <ul>{generateListItems()}</ul>
  );
};

const IntroInformation = () => {
  const [collapsed, setCollapsed] = useState(false);

  const handleToggleCollapse = () => {
    setCollapsed(!collapsed);
  };

  const IntoTitle = () => (
    <h1
      onClick={handleToggleCollapse}
      // style={{ cursor: "pointer", display: "flex", alignItems: "center" }}
    >
      Phoneinfoga
      <IconButton size="large" onClick={handleToggleCollapse}>
        {collapsed ? (
          <ExpandMoreIcon fontSize="inherit" />
        ) : (
          <ExpandLessIcon fontSize="inherit" />
        )}
      </IconButton>
    </h1>
  );

  const features = [
    "Check if phone number exists",
    "Gather basic information such as country, line type, and carrier",
    "OSINT footprinting using external APIs, phone books & search engines",
    "Check for reputation reports, social media, disposable numbers, and more",
  ];

  const anti_features = [
    "Does not claim to provide relevant or verified data, it's just a tool!",
    "Does not allow to 'track' a phone or its owner in real time",
    "Does not allow to get the precise phone location",
    "Does not allow to hack a phone",
  ];

  return (
    <>
      <br></br>
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
          style={{ alignSelf: "center" }}
        />
      </div>
      <IntoTitle />
      <Collapse in={!collapsed}>
        <div>
          <h2>About</h2>
          <p>
            PhoneInfoga is one of the most advanced tools to scan international
            phone numbers. It allows you to first gather basic information such
            as country, area, carrier and line type, then use various techniques
            to try to find the VoIP provider or identify the owner. It works
            with a collection of scanners that must be configured in order for
            the tool to be effective. PhoneInfoga doesn't automate everything,
            it's just there to help investigating on phone numbers.
          </p>
        </div>
        <Grid container spacing={2}>
          <Grid
            item
            xs={6}
            sx={{
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
            }}
          >
            <h2>Features</h2>
            <br></br>
            <ListDense title="Features" items={features} />
          </Grid>
          <Grid
            item
            xs={6}
            sx={{
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
            }}
          >
            <h2>Anti-features</h2>
            <br></br>
            <ListDense title="Anti-features" items={anti_features} />
          </Grid>
        </Grid>
      </Collapse>
    </>
  );
};

export default IntroInformation;
