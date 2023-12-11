import React, { useState } from "react";
import IconButton from "@mui/material/IconButton";
import Collapse from "@mui/material/Collapse";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import ExpandLessIcon from "@mui/icons-material/ExpandLess";

const CollapsibleSection = ({
  title,
  children,
  headerSize = 2,
  isCollapsed = true,
}) => {
  const [collapsed, setCollapsed] = useState(isCollapsed);

  const handleToggleCollapse = () => {
    setCollapsed(!collapsed);
  };

  const HeaderTag = `h${headerSize}`;

  return (
    <>
      <HeaderTag
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
      </HeaderTag>
      <Collapse in={!collapsed}>
        <div>
          {children}
          <br />
          <br />
        </div>
      </Collapse>
    </>
  );
};

export default CollapsibleSection;
