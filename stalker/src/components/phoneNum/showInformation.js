import React from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableRow from "@mui/material/TableRow";

const ShowInformation = ({ data }) => {
  return (
    <>
      <h2>Number Information</h2>
      <TableContainer sx={{ marginTop: 2 }}>
        <Table>
          <TableBody>
            <TableRow>
              <TableCell>Raw Local</TableCell>
              <TableCell>{data.rawLocal}</TableCell>
            </TableRow>
            <TableRow>
              <TableCell>Local</TableCell>
              <TableCell>{data.local}</TableCell>
            </TableRow>
            <TableRow>
              <TableCell>E164</TableCell>
              <TableCell>{data.e164}</TableCell>
            </TableRow>
            <TableRow>
              <TableCell>International</TableCell>
              <TableCell>{data.international}</TableCell>
            </TableRow>
            <TableRow>
              <TableCell>Country</TableCell>
              <TableCell>{data.country}</TableCell>
            </TableRow>
          </TableBody>
        </Table>
      </TableContainer>
    </>
  );
};

export default ShowInformation;
