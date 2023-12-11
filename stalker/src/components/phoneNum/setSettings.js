// react
import React from "react";

// mui
import TextField from "@mui/material/TextField";
import Grid from "@mui/material/Grid";
import Button from "@mui/material/Button";
import Stack from "@mui/material/Stack";
import SaveIcon from "@mui/icons-material/Save";
import Paper from "@mui/material/Paper";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Typography from "@mui/material/Typography";

// mui icons
import DeleteIcon from "@mui/icons-material/Delete";

// my components
import CollapsibleSection from "../_shared/collapsibleSection";

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

  const FormActionButtons = () => (
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
      <Button variant="outlined" color="error" startIcon={<DeleteIcon />}>
        Clear
      </Button>
      <Button variant="contained" endIcon={<SaveIcon />}>
        Update
      </Button>
    </Stack>
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
        <CollapsibleSection
          title="What is Phoneinfoga?"
          headerSize={2}
          isCollapsed={true}
        >
          <div>
            <FormItems />
            <br />
            <FormActionButtons />
            <br />
            <br />
            <EnvironmentTable
              title="Environment Variables for Numverify"
              title_href="https://apilayer.com/marketplace/number_verification-api"
              environmentVariables={environmentVariables_Numverify}
            />
            <br />
            <EnvironmentTable
              title="Environment Variables for Google Custom Search"
              title_href="https://console.cloud.google.com/apis/api/customsearch.googleapis.com/metrics"
              environmentVariables={environmentVariables_GoogleCS}
            />
          </div>
        </CollapsibleSection>
      </div>
    </div>
  );
};

export default SetSettings;
