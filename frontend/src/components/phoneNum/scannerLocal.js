// react
import React from "react";

// mui
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableRow from "@mui/material/TableRow";

const ScannerLocal = ({ dataList }) => {
  return (
    <TableContainer sx={{ marginTop: 2 }}>
      <Table>
        <TableBody>
          {Object.entries(dataList).map(([key, value], index) => (
            <TableRow key={index}>
              <TableCell>{key}</TableCell>
              <TableCell>
                {typeof value === "boolean" ? (value ? "Yes" : "No") : value}
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default ScannerLocal;
