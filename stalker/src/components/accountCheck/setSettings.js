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
            <Grid item xs={12} md={2}>
              <h4>Numverify</h4>
            </Grid>
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
