// react
import React from "react";

// mui
import CircularProgress from "@mui/material/CircularProgress";
import Dialog from "@mui/material/Dialog";
import DialogTitle from "@mui/material/DialogTitle";

const LoadingDialog = ({ open, text = "Please Wait" }) => (
  <Dialog
    open={open}
    aria-labelledby="loading-dialog-title"
    disableBackdropClick
    disableEscapeKeyDown
  >
    <DialogTitle id="loading-dialog-title">{text}</DialogTitle>
    <div style={{ textAlign: "center", padding: "16px" }}>
      <CircularProgress />
    </div>
  </Dialog>
);

export default LoadingDialog;
