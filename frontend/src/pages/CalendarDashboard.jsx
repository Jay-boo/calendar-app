import React, { useEffect, useState } from 'react';
import FastAPIClient from '../client';
import { Link, useNavigate } from "react-router-dom";
import config from "../config";
import { NotLoggedIn } from "./NotLoggedIn";
import axios from 'axios';
import jwtDecode from "jwt-decode";

const client = new FastAPIClient(config);

const CalendarView = ({ calendars }) => {
  console.log(calendars);
  if (JSON.stringify(calendars) != JSON.stringify({ error: "no calendar" })) {
    const list_calendars = calendars.map((calendar) => <li> {calendar.calendar_id}</li>)

    return (
      <div>
        <h1> Your calendars</h1>
        <ul>{list_calendars}</ul>
      </div>
    );
  } else {
    return (
      <div>
        <h1> Your calendars</h1>
        <ul> <li> Not any calendars</li></ul>
      </div>
    );
  }


};

const CalendarDashboard = () => {
  const [calendars, setCalendars] = useState([]);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  useEffect(() => {
    fetchUserCalendar()
  }, []);


  const fetchUserCalendar = () => {
    client.getCalendar().then((data) => {
      setCalendars(data);
    })
  };
  useEffect(() => {
    const tokenString = localStorage.getItem("token");
    if (tokenString) {
      const token = JSON.parse(tokenString);
      const decodedAccessToken = jwtDecode(token.access_token);
      if (JSON.stringify(token) !== JSON.stringify({ error: "invalid credentials" })) {
        setIsLoggedIn(true);
      }
    }
  }, []);


  if (!isLoggedIn) return <NotLoggedIn />

  return (
    <>
      <div>

        <Link to="/login"
          className="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white mx-4">
          login
        </Link>
        <CalendarView calendars={calendars} fetchUserCalendar={fetchUserCalendar} />
      </div>
    </>
  )
}




export default CalendarDashboard;
