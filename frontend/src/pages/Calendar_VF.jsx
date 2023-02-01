import { Calendar, dateFnsLocalizer } from "react-big-calendar";
import React, { useEffect, useState } from 'react';
import getDay from 'date-fns/getDay';
import parse from 'date-fns/parse';
import startOfWeek from "date-fns/startOfWeek"
import format from "date-fns/format";
import "react-big-calendar/lib/css/react-big-calendar.css";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

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
    start: new Date(2023, 0, 1),
    end: new Date(2023, 0, 2)
  },
  {
    title: "Big ",
    allDay: true,
    start: new Date(2023, 0, 7),
    end: new Date(2023, 0, 10)
  }
]

export const Calendar_VF = () => {

  const [newEvent, setNewEvent] = useState({ title: "", start: "", end: "" })
  const [allEvents, setAllEvents] = useState(events)



  function handleAddEvent() {
  }







  return (
    <div className="App">
      <h1> Calendar </h1>
      <h2> Add new event</h2>

      <div>
        <input type="text" placeholder='Add title event'
          style={{ width: "20%", marginRight: "10px" }}
          value={newEvent.title} onChange={(e) => setNewEvent({ ...newEvent, title: e.target.value })} />
        <DatePicker placeholderText='Start Date' style={{ marginRight: "10px" }}
          selected={newEvent.start} onChange={(start) => setNewEvent(...newEvent, start)} />
        <DatePicker placeholderText='End Date' style={{ marginRight: "10px" }}
          selected={newEvent.end} onChange={(end) => setNewEvent(...newEvent, end)}
        />

        <button style={{ marginTop: "10px" }} onClick={handleAddEvent}>
          Add Event

        </button>

      </div>


      <Calendar

        localizer={localizer}
        events={events}
        startAccessor="start"
        endAccessor="end"
        style={{ height: 500, margin: "50px" }}

      />
    </div>
  );
}
