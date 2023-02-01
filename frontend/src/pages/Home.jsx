import React, { useEffect, useState } from 'react';
import FastAPIClient from '../client';
import { Link, useNavigate } from "react-router-dom";
import config from "../config"
import axios from 'axios';

const client = new FastAPIClient(config);

const CalendarView = ({ calendars }) => {
  console.log(calendars);
  const list_calendars = calendars.map((calendar) => <li> {calendar.calendar_id}</li>)

  return (
    <div>
      <h1> Your calendars</h1>
      <ul>{list_calendars}</ul>
    </div>
  );
};

const Home = () => {
  const [calendars, setCalendars] = useState([]);
  useEffect(() => {
    fetchUserCalendar()
  }, []);


  const fetchUserCalendar = () => {
    client.getCalendar().then((data) => {
      setCalendars(data);
    })
  };

  return (
    <>
      <div>

        <Link to="/"
          className="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white mx-4">
          login
        </Link>
        <CalendarView calendars={calendars} fetchUserCalendar={fetchUserCalendar} />
      </div>
    </>
  )
}




export default Home;
