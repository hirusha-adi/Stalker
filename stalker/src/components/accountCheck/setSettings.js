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

import {
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Typography,
} from "@mui/material";

const EnvironmentTable = ({ title, title_href, environmentVariables }) => {
  return (
    <Paper elevation={3} style={{ padding: "16px" }}>
      <a href={title_href}>
        <Typography variant="h6" gutterBottom>
          {title}
        </Typography>
      </a>
      <TableContainer>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Variable</TableCell>
              <TableCell>Default</TableCell>
              <TableCell>Description</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {environmentVariables.map((variable) => (
              <TableRow key={variable.name}>
                <TableCell>{variable.name}</TableCell>
                <TableCell>{variable.default || "-"}</TableCell>
                <TableCell>{variable.description || "-"}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
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

  const environmentVariables_Numverify = [
    {
      name: "NUMVERIFY_API_KEY	",
      default: "",
      description: "API key to authenticate to the Numverify API.",
    },
  ];

  const environmentVariables_GoogleCS = [
    { name: "GOOGLECSE_CX", default: "", description: "Search engine ID." },
    {
      name: "GOOGLE_API_KEY",
      default: "",
      description: "API key to authenticate to the Google API.",
    },
    {
      name: "GOOGLECSE_MAX_RESULTS",
      default: "10",
      description: "Maximum results for each request.",
    },
  ];

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
            <EnvironmentTable
              title="Environment Variables for Numverify"
              title_href="https://apilayer.com/marketplace/number_verification-api"
              environmentVariables={environmentVariables_Numverify}
            />
            <br></br>
            <EnvironmentTable
              title="Environment Variables for Google Custom Search"
              title_href="https://console.cloud.google.com/apis/api/customsearch.googleapis.com/metrics"
              environmentVariables={environmentVariables_GoogleCS}
            />
          </div>
        </Collapse>
      </div>
    </div>
  );
};

export default SetSettings;
