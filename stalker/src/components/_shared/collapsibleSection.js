import React, { useState } from "react";
import IconButton from "@mui/material/IconButton";
import Collapse from "@mui/material/Collapse";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import ExpandLessIcon from "@mui/icons-material/ExpandLess";

const CollapsibleSection = ({ title, children }) => {
  const [collapsed, setCollapsed] = useState(true);

  const handleToggleCollapse = () => {
    setCollapsed(!collapsed);
  };

  return (
    <>
      <h2
        onClick={handleToggleCollapse}
        style={{ cursor: "pointer", display: "flex", alignItems: "center" }}
      >
        {title}
        <IconButton size="large" onClick={handleToggleCollapse}>
          {collapsed ? (
            <ExpandMoreIcon fontSize="inherit" />
          ) : (
            <ExpandLessIcon fontSize="inherit" />
          )}
        </IconButton>
      </h2>
      <Collapse in={!collapsed}>
        <div>
          {children}
          <br />
        </div>
      </Collapse>
    </>
  );
};

export default CollapsibleSection;
