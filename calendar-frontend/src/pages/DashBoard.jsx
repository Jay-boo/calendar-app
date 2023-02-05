import CalendarDashboard from "../components/CalendarDashBoard";
import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import FastAPIClient from "../client";
import { NotLoggedIn } from "./NotLoggedIn";
import jwtDecode from "jwt-decode";
import { config } from "dotenv";


const client = new FastAPIClient(config);

const DashBoard = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    const tokenString = localStorage.getItem("token");
    console.log("In Login useEffect items", localStorage);
    if (tokenString) {
      console.log("Is valid");
      const token = JSON.parse(tokenString);
      const isAccessTokenValid =
        JSON.stringify(token) != JSON.stringify({ error: "invalid credentials" })
      console.log("is Access", isAccessTokenValid);
      if (isAccessTokenValid) {
        const decodedAccessToken = jwtDecode(token.access_token);
        setIsLoggedIn(true);

      }

    }
  }, []);
  if (!isLoggedIn) return <NotLoggedIn />



  return (
    <div>
      <Link to="/login"> To login page</Link>

      <CalendarDashboard />
    </div>
  )
}
export default DashBoard;

