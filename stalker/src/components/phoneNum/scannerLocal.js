// react
import React from "react";

// mui
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableRow from "@mui/material/TableRow";

const ScannerLocal = ({ data }) => {
  const informationItems = [
    { label: "Raw Local", value: data.rawLocal },
    { label: "Local", value: data.local },
    { label: "E164", value: data.e164 },
    { label: "International", value: data.international },
    { label: "Country", value: data.country },
  ];

  return (
    <TableContainer sx={{ marginTop: 2 }}>
      <Table>
        <TableBody>
          {informationItems.map((item, index) => (
            <TableRow key={index}>
              <TableCell>{item.label}</TableCell>
              <TableCell>{item.value}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default ScannerLocal;
