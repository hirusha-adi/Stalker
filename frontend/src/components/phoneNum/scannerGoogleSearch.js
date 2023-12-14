// react
import React from "react";
// import React, { useState } from "react";

// mui
import { DataGrid } from "@mui/x-data-grid";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";

const openInNewTab = (url) => {
  const newWindow = window.open(url, "_blank");
  if (newWindow) newWindow.opener = null;
};

const columns = [
  { field: "id", headerName: "ID" },
  { field: "google_query", headerName: "Google Dork Query", flex: 4 },
  {
    field: "openInNewTab",
    headerName: "Open",
    flex: 1,
    renderCell: (params) => (
      <Button
        variant="contained"
        color="primary"
        onClick={() => openInNewTab(params.row.url)}
      >
        Open
      </Button>
    ),
  },
];

const GoogleDorksTable = ({ title, rows }) =>
  rows.length === 0 ? null : (
    <>
      <Typography variant="h5" sx={{ marginTop: 3, marginBottom: 2 }}>
        {title}
      </Typography>
      <div style={{ height: 400, width: "100%" }}>
        <DataGrid
          rows={rows}
          columns={columns}
          initialState={{
            pagination: {
              paginationModel: { page: 0, pageSize: 5 },
            },
          }}
          pageSizeOptions={[5, 10]}
          checkboxSelection
        />
      </div>
    </>
  );

const ScannerGoogleSearch = ({ data }) => {
  return (
    <>
      <GoogleDorksTable title="Social Media" rows={data.social_media} />
      <GoogleDorksTable
        title="Disposable providers"
        rows={data.disposable_providers}
      />
      <GoogleDorksTable title="Reputation" rows={data.reputation} />
      <GoogleDorksTable title="Individuals" rows={data.individuals} />
      <GoogleDorksTable title="General" rows={data.general} />
    </>
  );
};

export default ScannerGoogleSearch;
