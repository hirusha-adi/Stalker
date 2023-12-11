import React from "react";
import Typography from "@mui/material/Typography";
import { DataGrid } from "@mui/x-data-grid";

const columns = [
  { field: "username", headerName: "Username", flex: 1 },
  { field: "name", headerName: "Name", flex: 1 },
  { field: "url_main", headerName: "Main URL", flex: 1 },
  { field: "url_user", headerName: "User URL", flex: 1 },
  { field: "exists", headerName: "Exists", flex: 1 },
  { field: "http_status", headerName: "HTTP Status", flex: 1 },
  { field: "response_time_s", headerName: "Response Time (s)", flex: 1 },
];

// const AvailableAccountsTable = ({ title, rows }) =>
const AvailableAccountsTable = ({ title, rows }) =>
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

export default AvailableAccountsTable;
