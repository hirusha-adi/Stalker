import React, { useState } from "react";
import TextField from "@mui/material/TextField";
import Grid from "@mui/material/Grid";
import Button from "@mui/material/Button";
import DeleteIcon from "@mui/icons-material/Delete";
import Stack from "@mui/material/Stack";
import SaveIcon from "@mui/icons-material/Save";
import Collapse from "@mui/material/Collapse";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import IconButton from "@mui/material/IconButton";
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
      <Grid container spacing={1} justifyContent="flex-end">
        <Grid container item spacing={4}>
          <Grid item xs={12} md={4}>
            <TextField
              id="NUMVERIFY_API_KEY"
              label="NUMVERIFY_API_KEY"
              variant="standard"
              fullWidth
            />
          </Grid>
          <Grid item xs={12} md={4}>
            <TextField
              id="GOOGLECSE_CX"
              label="GOOGLECSE_CX"
              variant="standard"
              fullWidth
            />
          </Grid>
          <Grid item xs={12} md={4}>
            <TextField
              id="GOOGLE_API_KEY"
              label="GOOGLE_API_KEY"
              variant="standard"
              fullWidth
            />
          </Grid>
        </Grid>
      </Grid>
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
          </div>
        </Collapse>
      </div>
    </div>
  );
};

export default SetSettings;
