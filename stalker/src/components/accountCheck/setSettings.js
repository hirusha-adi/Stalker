// react
import React, { useState } from "react";

// mui
import TextField from "@mui/material/TextField";
import Grid from "@mui/material/Grid";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import FormGroup from "@mui/material/FormGroup";
import Tooltip from "@mui/material/Tooltip";

// mui icons

// my components
import CollapsibleSection from "../_shared/collapsibleSection";

const FormItems = () => {
  const [useTor, setUseTor] = useState(false);
  const [uniqueTor, setUniqueTor] = useState(false);
  const [nsfw, setNsfw] = useState(false);
  const [proxyUrl, setProxyUrl] = useState("");
  const [timeoutValue, setTimeoutValue] = useState("");
  const [siteName, setSiteName] = useState("");

  const handleCheckboxChange = (event) => {
    const { name, checked } = event.target;

    // If "Site" checkbox is unchecked, hide SITE_NAME input field
    if (name === "useSite" && !checked) {
      setSiteName("");
    }

    switch (name) {
      case "useTor":
        setUseTor(checked);
        break;
      case "uniqueTor":
        setUniqueTor(checked);
        break;
      case "nsfw":
        setNsfw(checked);
        break;
      default:
        break;
    }
  };

  // Details to show on hover on ChooseOptions checkboxes
  const detailsOnHover = {
    useTor: `
Make requests over Tor; increases runtime;
requires Tor to be installed and in system path.
    `,
    uniqueTor: `
Make requests over Tor with new Tor circuit after each request;
increases runtime; requires Tor to be installed and in system
path.
    `,
    nsfw: `
Include checking of NSFW sites from default list.
    `,
  };

  // check boxes
  const ChooseOptions = () => (
    <FormGroup>
      <Tooltip title={detailsOnHover.useTor}>
        <FormControlLabel
          control={
            <Checkbox
              checked={useTor}
              onChange={handleCheckboxChange}
              name="useTor"
            />
          }
          label="Use Tor"
        />
      </Tooltip>
      <Tooltip title={detailsOnHover.uniqueTor}>
        <FormControlLabel
          control={
            <Checkbox
              checked={uniqueTor}
              onChange={handleCheckboxChange}
              name="uniqueTor"
            />
          }
          label="Unique Tor"
        />
      </Tooltip>
      <Tooltip title={detailsOnHover.nsfw}>
        <FormControlLabel
          control={
            <Checkbox
              checked={nsfw}
              onChange={handleCheckboxChange}
              name="nsfw"
            />
          }
          label="NSFW"
        />
      </Tooltip>
    </FormGroup>
  );

  // input boxes
  const SetValues = () => (
    <>
      <TextField
        id="SITE_NAME"
        label="Site Name"
        type="text"
        variant="standard"
        value={siteName}
        onChange={(e) => setSiteName(e.target.value)}
        fullWidth
      />
      <TextField
        id="PROXY_URL"
        label="Proxy URL"
        variant="standard"
        value={proxyUrl}
        onChange={(e) => setProxyUrl(e.target.value)}
        style={{ marginTop: "16px" }}
        fullWidth
      />
      <br />
      <TextField
        id="TIMEOUT"
        label="Timeout"
        variant="standard"
        type="number"
        value={timeoutValue}
        onChange={(e) => setTimeoutValue(e.target.value)}
        style={{ marginTop: "16px" }}
        fullWidth
      />
    </>
  );

  return (
    <React.Fragment>
      <Grid container spacing={1} justifyContent="flex-end">
        <Grid container item spacing={4}>
          <Grid item xs={12} md={4}>
            <h3>Choose Options</h3>
            <ChooseOptions />
          </Grid>
          <Grid item xs={12} md={8}>
            <h3>Set Values</h3>
            <SetValues />
          </Grid>
        </Grid>
      </Grid>
    </React.Fragment>
  );
};

const SetSettings = () => {
  return (
    <div>
      <div>
        <CollapsibleSection
          title="Advanced Options"
          headerSize={2}
          isCollapsed={true}
        >
          <div>
            <FormItems />
            <br></br>
            <br></br>
          </div>
        </CollapsibleSection>
      </div>
    </div>
  );
};

export default SetSettings;
