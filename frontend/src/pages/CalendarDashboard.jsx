import React, { useEffect, useState } from 'react';
import FastAPIClient from '../client';
import { Link, useNavigate } from "react-router-dom";
import config from "../config";
import { NotLoggedIn } from "./NotLoggedIn";
import axios from 'axios';
import jwtDecode from "jwt-decode";
import { Calendar_VF } from "./Calendar_VF";
import CalendarComponent from "./CalendarBis";

const client = new FastAPIClient(config);




const CalendarView = ({ calendar_id }) => {
  console.log("in calendarView");
  console.log(calendar_id)
  const [events, setEvents] = useState([]);
  const fetchEvents = () => {
    client.getEventsCalendar(calendar_id).then((data) => {
      const events_new = [];
      console.log(new Date());
      for (var i = 0; i < data.length; i++) {
        console.log("for");
        var start_date = new Date(data[i].start_date);
        var end_date = new Date(data[i].end_date);
        start_date.setTime(start_date.getTime() - 60 * 60 * 1000)
        end_date.setTime(end_date.getTime() - 60 * 60 * 1000)
        events_new.push({
          title: data[i].title,
          start: start_date,
          end: end_date
        });
      };
      setEvents(events_new);

    })
  }


  return (
    <div>
      <button onClick={fetchEvents}>See calendar {calendar_id}</button>
      {events.length > 0 &&
        <div>
          <CalendarComponent events={events} fetchEvents={fetchEvents} /></div>}
      {/* <Calendar_VF eventsCal={events} calendar_id={calendar_id} fetchEvents={fetchEvents} /> */}
    </div>
  )
};


const GlobalCalendarView = ({ calendars }) => {
  const [calendarView, setCalendarView] = useState();
  const haveCalendar = JSON.stringify(calendars) != JSON.stringify({ error: "no calendar" });


  if (haveCalendar) {
    const list_calendars = calendars.map((calendar) => <option value={calendar.calendar_id}> {calendar.calendar_id}</option >);
    console.log(list_calendars);

    const onChangeSelect = (e) => {
      var calendar_test = document.getElementById("select-calendar").value;
      setCalendarView(calendar_test);
    }


    return (
      <div>
        <h1> Your calendars</h1>
        <label> Choose calendar</label>
        <select onChange={(e) => onChangeSelect(e)} name="calendar-id" id="select-calendar" multiple>{list_calendars}</select>
        <CalendarView calendar_id={calendarView} />
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
  // const calendar_id = document.getElementById("select-calendar").value;


  const fetchUserCalendar = () => {
    client.getCalendar().then((data) => {
      setCalendars(data);

    });
  };

  // const fetchUserCalendarEvents = () => {
  //   if (document.getElementById("select-calendar") != null) {
  //     setCalendarView(document.getElementById("select-calendar").value);
  //   } else {
  //     setCalendarView("0");
  //   }
  // };
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
        <GlobalCalendarView calendars={calendars} fetchUserCalendar={fetchUserCalendar} />
      </div>
    </>
  )
}




export default CalendarDashboard;
