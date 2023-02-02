import { Calendar, dateFnsLocalizer } from "react-big-calendar";
import config from "../config";
import FastAPIClient from '../client';
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

const client = new FastAPIClient(config);

const localizer = dateFnsLocalizer(
  {
    format,
    parse,
    startOfWeek,
    getDay,
    locales,
  }
)



export const Calendar_VF = ({ eventsCal, calendar_id }) => {
  const [newEvent, setNewEvent] = useState({ title: "", start: "", end: "" });
  const [events, setEvent] = useState([]);
  console.log("in calendar_VF");
  console.log(eventsCal);
  console.log(calendar_id);





  function ViewEvents() {
    console.log("handle add");
    setEvent(eventsCal);

  }
  function handleAddEvent() {
    console.log("in add elements")
    console.log(newEvent);
    const effective_times = client.addEvent(calendar_id, newEvent);
    console.log("effffective ");
    console.log(effective_times);
    setNewEvent({ ...newEvent, start: effective_times.start_time });
    setNewEvent({ ...newEvent, end: effective_times.end_time });
    console.log(newEvent);
    setEvent([...events, newEvent]);
  }







  return (
    <div >
      <h1> Calendar{calendar_id} </h1>
      <div>
        <button onClick={ViewEvents}>  INITIALIZE CALENDAR VIEW</button>
      </div>
      <h2> Add new event</h2>


      <div>
        <input type="text" placeholder='Add title event'
          style={{ width: "20%", marginRight: "10px" }}
          value={newEvent.title} onChange={(e) => setNewEvent({ ...newEvent, title: e.target.value })} />
        <DatePicker placeholderText='Start Date' style={{ marginRight: "10px" }}
          selected={newEvent.start} showTimeSelect
          timeFormat="HH:mm"
          timeIntervals={15} onChange={(start) => setNewEvent({ ...newEvent, start })} />
        <DatePicker placeholderText='End Date' style={{ marginRight: "10px" }}
          selected={newEvent.end} showTimeSelect
          timeFormat="HH:mm"
          timeIntervals={15}
          onChange={end => setNewEvent({ ...newEvent, end })}
        />

        <button style={{ marginTop: "10px" }} onClick={handleAddEvent}>
          Add event

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
