// react
import React, { useState } from "react";

// mui
import TextField from "@mui/material/TextField";
import Grid from "@mui/material/Grid";
import Button from "@mui/material/Button";
import Stack from "@mui/material/Stack";
import SaveIcon from "@mui/icons-material/Save";
import Collapse from "@mui/material/Collapse";
import IconButton from "@mui/material/IconButton";

// mui icons
import DeleteIcon from "@mui/icons-material/Delete";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import ExpandLessIcon from "@mui/icons-material/ExpandLess";

import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import FormGroup from "@mui/material/FormGroup";
import Tooltip from '@mui/material/Tooltip';

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
    `
  }

  return (
    <React.Fragment>
      <Grid container spacing={1} justifyContent="flex-end">
        <Grid container item spacing={4}>
          <Grid item xs={12} md={4}>
            <h3>Choose Options</h3>
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
          </Grid>
          <Grid item xs={12} md={8}>
            <h3>Set Values</h3>
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
            <br />
          </Grid>
        </Grid>
      </Grid>
    </React.Fragment>
  );
};

const SetSettings = () => {
  const [collapsed, setCollapsed] = useState(true);

  const handleToggleCollapse = () => {
    setCollapsed(!collapsed);
  };

  const FormTitle = () => (
    <h2
      onClick={handleToggleCollapse}
      style={{ cursor: "pointer", display: "flex", alignItems: "center" }}
    >
      Advanced Options
      <IconButton size="large" onClick={handleToggleCollapse}>
        {collapsed ? (
          <ExpandMoreIcon fontSize="inherit" />
        ) : (
          <ExpandLessIcon fontSize="inherit" />
        )}
      </IconButton>
    </h2>
  );

  return (
    <div>
      <div>
        <FormTitle />
        <Collapse in={!collapsed}>
          <div>
            <FormItems />
            <br />
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
              <Button variant="contained" endIcon={<SaveIcon />}>
                Update
              </Button>
            </Stack>
            <br></br>
          </div>
        </Collapse>
      </div>
    </div>
  );
};

export default SetSettings;
