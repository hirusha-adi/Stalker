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
import Paper from "@mui/material/Paper";

const PhoneInfoConfig = () => {
  const [useTor, setUseTor] = useState(false);
  const [uniqueTor, setUniqueTor] = useState(false);
  const [nsfw, setNsfw] = useState(false);
  const [useSite, setUseSite] = useState(false);
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
      case "useSite":
        setUseSite(checked);
        break;
      default:
        break;
    }
  };

  return (
    <Paper
      style={{ backgroundColor: "#f5f5f5", padding: "16px" }}
      elevation={3}
    >
      <FormGroup>
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
        <FormControlLabel
          control={
            <Checkbox
              checked={useSite}
              onChange={handleCheckboxChange}
              name="useSite"
            />
          }
          label="Site"
        />
      </FormGroup>

      <TextField
        label="PROXY_URL"
        type="text"
        value={proxyUrl}
        onChange={(e) => setProxyUrl(e.target.value)}
        style={{ marginTop: "16px" }}
      />

      <TextField
        label="TIMEOUT"
        type="number"
        value={timeoutValue}
        onChange={(e) => setTimeoutValue(e.target.value)}
        style={{ marginTop: "16px" }}
      />

      {useSite && (
        <TextField
          label="SITE_NAME"
          type="text"
          value={siteName}
          onChange={(e) => setSiteName(e.target.value)}
          style={{ marginTop: "16px" }}
        />
      )}
    </Paper>
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
      Update Settings
      <IconButton size="large" onClick={handleToggleCollapse}>
        {collapsed ? (
          <ExpandMoreIcon fontSize="inherit" />
        ) : (
          <ExpandLessIcon fontSize="inherit" />
        )}
      </IconButton>
    </h2>
  );

  const FormItems = () => (
    <React.Fragment>
      <>
        <Grid container spacing={1} justifyContent="flex-end">
          <Grid container item spacing={4}>
            <Grid item xs={12} md={3}>
              <h4>NUMVERIFY_API_KEY</h4>
            </Grid>
            <Grid item xs={12} md={7}>
              <TextField
                id="NUMVERIFY_API_KEY"
                label="NUMVERIFY_API_KEY"
                variant="standard"
                fullWidth
              />
            </Grid>
          </Grid>
        </Grid>
        <Grid container spacing={1} justifyContent="flex-end">
          <Grid container item spacing={4}>
            <Grid item xs={12} md={2}>
              <h4>Googlecse</h4>
            </Grid>
            <Grid item xs={12} md={3}>
              <h4>GOOGLECSE_CX</h4>
            </Grid>
            <Grid item xs={12} md={7}>
              <TextField
                id="GOOGLECSE_CX"
                label="GOOGLECSE_CX"
                variant="standard"
                fullWidth
              />
            </Grid>
          </Grid>
        </Grid>
        <Grid container spacing={1} justifyContent="flex-end">
          <Grid container item spacing={4}>
            <Grid item xs={12} md={2}></Grid>
            <Grid item xs={12} md={3}>
              <h4>GOOGLE_API_KEY</h4>
            </Grid>
            <Grid item xs={12} md={7}>
              <TextField
                id="GOOGLE_API_KEY"
                label="GOOGLE_API_KEY"
                variant="standard"
                fullWidth
              />
            </Grid>
          </Grid>
        </Grid>
        <Grid container spacing={1} justifyContent="flex-end">
          <Grid container item spacing={4}>
            <Grid item xs={12} md={2}></Grid>
            <Grid item xs={12} md={3}>
              <h4>GOOGLECSE_MAX_RESULTS</h4>
            </Grid>
            <Grid item xs={12} md={7}>
              <TextField
                id="GOOGLECSE_MAX_RESULTS"
                label="GOOGLECSE_MAX_RESULTS"
                variant="standard"
                placeholder="defaults to: 10"
                fullWidth
              />
            </Grid>
          </Grid>
        </Grid>
      </>
    </React.Fragment>
  );

  return (
    <div>
      <div>
        <FormTitle />
        <Collapse in={!collapsed}>
          <div>
            <FormItems />
            <PhoneInfoConfig />
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
