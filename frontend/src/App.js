import './App.css';
import { Calendar, dateFnsLocalizer } from "react-big-calendar";
import getDay from 'date-fns/getDay';
import parse from 'date-fns/parse';
import startOfWeek from "date-fns/startOfWeek"
import format from "date-fns/format";
import React, { useState } from "react";
import "react-big-calendar/lib/css/react-big-calendar.css";


const locales = {
  "en-US": require("date-fns/locale/en-US")
}

const localizer = dateFnsLocalizer(
  {
    format,
    parse,
    startOfWeek,
    getDay,
    locales,
  }
)


const events = [
  {
    title: "Big meeting",
    allDay: true,
    start: new Date(2023, 1, 29),
    end: new Date(2023, 1, 31)
  }
]

function App() {
  return (
    <div className="App">
      <h1>hello</h1>
      <Calendar localizer={localizer} events={events} startAccessor="start" endAccessor="end" style={{ height: 500, margin: "50px" }} />
    </div>
  );
}

export default App;
