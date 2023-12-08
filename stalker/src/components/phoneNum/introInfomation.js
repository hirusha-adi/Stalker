import React, { useState } from "react";
import Collapse from "@mui/material/Collapse";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import IconButton from "@mui/material/IconButton";
import ExpandLessIcon from "@mui/icons-material/ExpandLess";
import Grid from "@mui/material/Grid";

const FeaturesList = ({ title, items }) => {
  const generateListItems = () => {
    return items.map((item, index) => <li>{item}</li>);
  };

  return (
    <>
      <h2>{title}</h2>
      <ul>{generateListItems()}</ul>
    </>
  );
};

const IntroInformation = () => {
  const [collapsed, setCollapsed] = useState(false);

  const handleToggleCollapse = () => {
    setCollapsed(!collapsed);
  };

  const IntoTitle = () => (
    <h2 onClick={handleToggleCollapse}>
      What is Phoneinfoga?
      <IconButton size="large" onClick={handleToggleCollapse}>
        {collapsed ? (
          <ExpandMoreIcon fontSize="inherit" />
        ) : (
          <ExpandLessIcon fontSize="inherit" />
        )}
      </IconButton>
    </h2>
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
              alignItems: "center",
              justifyContent: "center",
            }}
          >
            <FeaturesList title="Features" items={features} />
          </Grid>
          <Grid
            item
            xs={6}
            sx={{
              alignItems: "center",
              justifyContent: "center",
            }}
          >
            <FeaturesList title="Anti-features" items={anti_features} />
          </Grid>
        </Grid>
        <h3>
          <a
            href="https://github.com/sundowndev/phoneinfoga"
            target="_blank"
            rel="noreferrer"
          >
            Click here
          </a>{" "}
          to open the Github repository
        </h3>
      </Collapse>
    </>
  );
};

export default IntroInformation;
