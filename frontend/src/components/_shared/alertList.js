import React from "react";
import Alert from "@mui/material/Alert";
import AlertTitle from "@mui/material/AlertTitle";

const AlertList = ({ severity = "error", itemsList }) => {
  return (
    <Alert severity={severity} style={{ margin: "50px 0" }}>
      <AlertTitle>Errors</AlertTitle>
      An error has occured — <strong>check it out!</strong>
      <ul>
        {itemsList.map((error, index) => (
          <li key={index}>{error}</li>
        ))}
      </ul>
    </Alert>
  );
};

export default AlertList;
