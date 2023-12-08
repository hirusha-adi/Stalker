import React from "react";
// import React, { useState } from "react";
import { DataGrid } from "@mui/x-data-grid";

const columns = [
  { field: "id", headerName: "ID", width: 70 },
  { field: "firstName", headerName: "First name", width: 130 },
  { field: "lastName", headerName: "Last name", width: 130 },
  {
    field: "age",
    headerName: "Age",
    type: "number",
    width: 90,
  },
  {
    field: "fullName",
    headerName: "Full name",
    description: "This column has a value getter and is not sortable.",
    sortable: false,
    width: 160,
    valueGetter: (params) =>
      `${params.row.firstName || ""} ${params.row.lastName || ""}`,
  },
];

const GoogleDorksTable = ({ title, rows }) => {
  return (
    <>
      <h2>{title}</h2>
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
};

const ShowGoogleDorks = ({ data }) => {
  // Process Data and append them to the relevant
  return (
    <>
      <GoogleDorksTable title="Social Media" rows={data} />
      <GoogleDorksTable title="Disposable providers" rows={data} />
      <GoogleDorksTable title="Reputation" rows={data} />
      <GoogleDorksTable title="Individuals" rows={data} />
      <GoogleDorksTable title="General" rows={data} />
    </>
  );
};

export default ShowGoogleDorks;
