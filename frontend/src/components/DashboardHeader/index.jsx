import React, { useEffect, useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import FastAPIClient from '../../client';
import config from '../../config';
import jwtDecode from "jwt-decode";
import * as moment from "moment";

const client = new FastAPIClient(config);

function DashboardHeader() {
  console.log("Dashboard class")
  const navigate = useNavigate();
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // STATE WHICH WE WILL USE TO TOGGLE THE MENU ON HAMBURGER BUTTON PRESS
  const [toggleMenu, setToggleMenu] = useState(false);

  useEffect(() => {
    const tokenString = localStorage.getItem("token")
    if (tokenString) {
      const token = JSON.parse(tokenString)
      const decodedAccessToken = jwtDecode(token.access_token)
      if (moment.unix(decodedAccessToken.exp).toDate() > new Date()) {
        setIsLoggedIn(true)
      }
    }
  }, [])

  const handleLogout = () => {
    client.logout();
    setIsLoggedIn(false)
    navigate('/')
  }

  const handleLogin = () => {
    navigate("/");
  }

  let displayButton;
  const buttonStyle = "inline-block text-sm px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-teal-500 hover:bg-white mt-4 lg:mt-0"

  if (isLoggedIn) {
    displayButton = <button className={buttonStyle} onClick={() => handleLogout()}>Logout</button>;
  } else {
    displayButton = <button className={buttonStyle} onClick={() => handleLogin()}>Login</button>;
  }

  return (
    <nav className="flex items-center justify-between flex-wrap bg-teal-500 p-6">
      <div className="block lg:hidden">
        <button
          className="flex items-center px-3 py-2 border rounded text-teal-200 border-teal-400 hover:text-white hover:border-white"
          onClick={() => setToggleMenu(!toggleMenu)}>
        </button>
      </div>
      <div className={`animate-fade-in-down w-full ${toggleMenu ? "block" : "hidden"} flex-grow lg:flex lg:items-center lg:w-auto`}>
        <div className="text-sm lg:flex-grow">
          <Link to="/home"
            className="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white mx-4">
            Home
          </Link>
          {!isLoggedIn && <Link
            className="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white"
            to={`/sign-up`}>
            Create Account
          </Link>}
        </div>
        <div>
          {displayButton}
        </div>
      </div>
    </nav>
  );
}

export default DashboardHeader;
