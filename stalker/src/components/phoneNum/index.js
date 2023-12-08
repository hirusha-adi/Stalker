import React from "react";
import SetSettings from "./setSettings";
import IntroInformation from "./introInfomation";

const phoneNum = () => {
  const SearchNumber = () => (
    <div>
      <h2>Search phone number</h2>
    </div>
  );

  return (
    <div>
      <br></br>
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <img
          src="https://raw.githubusercontent.com/sundowndev/phoneinfoga/master/docs/images/banner.png"
          alt="banner"
          style={{ alignSelf: "center", width: "70%" }}
        />
      </div>
      <br></br>
      <SearchNumber />
      <SetSettings />
      <br></br>
      <br></br>
      <br></br>
      <hr></hr>
      <IntroInformation />
    </div>
  );
};

export default phoneNum;
