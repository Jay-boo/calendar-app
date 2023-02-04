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
    if (tokenString) {
      const token = JSON.parse(tokenString);
      const decodeAccessToken = jwtDecode(token.access_token);
      if (JSON.stringify(token) !== JSON.stringify({ error: "invalid credentials" })) {
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

