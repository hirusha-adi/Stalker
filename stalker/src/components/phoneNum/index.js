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
      <IntroInformation />
      <SearchNumber />
      <SetSettings />
    </div>
  );
};

export default phoneNum;
