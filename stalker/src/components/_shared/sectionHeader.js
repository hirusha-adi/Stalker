import React from "react";

const ShowSectionHeader = ({ width, imgURL, subtitle }) => {
  const centeredStyle = {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    textAlign: "center",
  };

  return (
    <>
      <br />
      {/* Center the image */}
      <div style={centeredStyle}>
        {/* Image (logo) */}
        <img src={imgURL} alt="banner" style={{ alignSelf: "center", width }} />
        <br />
      </div>
      <br />
      <div style={centeredStyle}>{subtitle && <h3>{subtitle}</h3>}</div>
      <br />
    </>
  );
};

export default ShowSectionHeader;
