// react
import React, { useState } from "react";

// mui
import Collapse from "@mui/material/Collapse";
import IconButton from "@mui/material/IconButton";

// mui icons
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import ExpandLessIcon from "@mui/icons-material/ExpandLess";

const IntroInformation = () => {
  const [collapsed, setCollapsed] = useState(false);

  const handleToggleCollapse = () => {
    setCollapsed(!collapsed);
  };

  const IntoTitle = () => (
    <h2 onClick={handleToggleCollapse}>
      What is Sherlock?
      <IconButton size="large" onClick={handleToggleCollapse}>
        {collapsed ? (
          <ExpandMoreIcon fontSize="inherit" />
        ) : (
          <ExpandLessIcon fontSize="inherit" />
        )}
      </IconButton>
    </h2>
  );

  const ScannerNumverify = () => (
    <>
      <p>
        Sherlock is a free and open-source tool available on GitHub. This tool
        is free you can download it from Github and can use it for free of cost.
        Sherlock is used to finding usernames on social media on 300 sites. As
        you know many users register themselves on social media platforms using
        their own name. Suppose we need to find someone on any social media
        website such as Facebook, Instagram etc. To do so we need to go on
        different websites along and have to search for individually again and
        again. Sherlock makes it easy for us to find someone’s online presence
        on social media. Sherlock searches for usernames between 300 websites of
        social media and provides the related link of that social media
        platform. Sherlock is written in python language.
        <br />
        <br />
        Features of Sherlock:
        <br />
      </p>
      <ol>
        <li> Sherlock is a free and open-source tool.</li>
        <li>Sherlock is written in python language.</li>
        <li>Sherlock is used to hunt usernames.</li>
        <li>Sherlock searches on 300 social media websites.</li>
        <li>
          Sherlock uses python script to search for usernames among 300
          websites.
        </li>
        <li>
          Sherlock asks for username and then search online presence of it on
          other social media.
        </li>
      </ol>
    </>
  );

  return (
    <>
      <br></br>
      <IntoTitle />
      <Collapse in={!collapsed}>
        <ScannerNumverify />
      </Collapse>
    </>
  );
};

export default IntroInformation;
