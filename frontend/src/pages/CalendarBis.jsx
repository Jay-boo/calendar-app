import React, { Component } from "react";
import config from "../config";
import { Calendar, dateFnsLocalizer, momentLocalizer } from "react-big-calendar";
import moment from "moment";
import FlatButton from "material-ui/FlatButton";
import FastAPIClient from "../client";


const localizer = momentLocalizer(moment);
const client = new FastAPIClient(config);



class CalendarComponent extends Component {
  constructor(props) {
    console.log("constructor()")
    super(props);
    console.log(this.props.events);
    this.state = {
      events: this.props.events,
      title: "",
      start: "",
      end: "",
      desc: "",
      openSlot: false,
      openEvent: false,
      clickedEevent: {}
    };
    this.handleClose = this.handleClose.bind(this);
  }



  handleClose() {
    this.setState({ openEvent: false, openSlot: false });
  }

  handleSlotSelected(slotInfo) {
    console.log("Real slotInfo", slotInfo);
    this.setState({
      title: "",
      desc: "",
      start: slotInfo.start,
      end: slotInfo.end,
      openSlot: true
    });
  }

  handleEventSelected(event) {
  }

  render() {
    console.log("render()");

    const eventActions = [
      <FlatButton
        label="Cancel"
        primary={false}
        keyboardFocused={true}
        onClick={this.handleClose}
      />
    ];

    return (
      <div id="Calendar">
        <Calendar
          localizer={localizer}
          events={this.state.events}
          views={["month", "week", "day", "agenda"]}
          timeslots={2}
          defaultView="month"
          defaultDate={new Date()}
          selectable={true}
          onSelectEvent={(event) => this.handleEventSelected(event)}
          onSelectSlot={(slotInfo) => this.handleSlotSelected(slotInfo)}


        />

      </div>
    )
  }

}
export default CalendarComponent;
