import React from "react";

export default function Notification(props) {
  let classString = "";

  // Replace string below
  if ("replace with isRead prop" == false) {
    classString = "not-read";
  }
  return <div className={classString}>{/* message here 💖*/}</div>;
}
