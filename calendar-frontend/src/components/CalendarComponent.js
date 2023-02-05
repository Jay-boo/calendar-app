import React from "react";
import BigCalendar from "react-big-calendar";
import moment from "moment";
import FlatButton from "material-ui/FlatButton";
import defaultEvents from "./defaultEvents";
import defaultEventsBis from "./defaultEventsBis";
import Dialog from "material-ui/Dialog";
import TimePicker from "material-ui/TimePicker";
import TextField from "material-ui/TextField";
import FastAPIClient from "../client";
import config from "../config";
require("react-big-calendar/lib/css/react-big-calendar.css");

BigCalendar.momentLocalizer(moment);
const client = new FastAPIClient(config)

class CalendarComponent extends React.Component {
        constructor(props) {
                super(props);
                this.state = {
                        events: [],
                        id: "",
                        title: "",
                        start: "",
                        end: "",
                        desc: "",
                        type: "",
                        property: "",
                        openSlot: false,
                        openEvent: false,
                        clickedEvent: {},
                        isInitialized: false,
                };
                this.handleClose = this.handleClose.bind(this);
        }


        componentDidMount() {
                console.log("componentDidMount -CalendarComponnent", this.props.calendar_id);
                client.getEventsCalendar(this.props.calendar_id).then(response => {
                        console.log("response", response);
                        response = response.map(
                                ({ start_date, created_at, type, property, description, event_id, end_date, calendar_id, title }) => {
                                        return {
                                                id: event_id,
                                                title: title,
                                                start: start_date,
                                                end: end_date,
                                                desc: description,
                                                type: type,
                                                property: property
                                        };
                                });
                        this.setState({ events: response });
                })
                        .catch((err => {
                                console.log("error");
                                console.log(err);
                        }));

        }
        componentWillReceiveProps(nextProps) {
                console.log("component", nextProps);
                client.getEventsCalendar(nextProps.calendar_id).then(response => {
                        response = response.map(
                                ({ start_date, created_at, type, property, description, event_id, end_date, calendar_id, title }) => {
                                        return {
                                                id: event_id,
                                                title: title,
                                                start: start_date,
                                                end: end_date,
                                                desc: description,
                                                type: type,
                                                property: property
                                        };
                                });
                        this.setState({ events: response });
                })
                        .catch((err => {
                                console.log(err);
                        }));

        }






        handleClose() {
                this.setState({ openEvent: false, openSlot: false });
        }


        handleSlotSelected(slotInfo) {
                console.log("handleslotSelected()");
                console.log("Real slotInfo", slotInfo);
                this.setState({
                        id: "",
                        title: "",
                        desc: "",
                        type: "",
                        property: "",
                        start: slotInfo.start,
                        end: slotInfo.end,
                        openSlot: true
                });
        }

        handleEventSelected(event) {
                console.log("handleEventSelected()");
                console.log("event", event);

                this.setState({
                        openEvent: true,
                        clickedEvent: event,
                        id: event.id,
                        start: event.start,
                        end: event.end,
                        title: event.title,
                        desc: event.desc,
                        type: event.type,
                        property: event.property

                });
        }



        setTitle(e) {
                this.setState({ title: e });
        };

        setDescription(e) {
                this.setState({ desc: e });
        };

        setType(e) {
                this.setState({ type: e });
        };
        setID(e) {
                this.setState({ id: parseInt(e) });
        };

        setProperty(e) {
                this.setState({ property: e });
        }

        handleStartTime = (event, date) => {
                this.setState({ start: date });
        };

        handleEndTime = (event, date) => {
                this.setState({ end: date });
        };

        // Onclick callback function that pushes new appointment into events array.
        async setNewAppointment() {
                console.log("setNewAppointment()");

                const { id, start, end, title, desc, type, property } = this.state;




                const previous_state = this.state.events;
                let appointment = { id, title, start, end, desc, type, property };
                const form_data = {
                        title: title,
                        description: desc,
                        start_date: start.toISOString(),
                        end_date: end.toISOString(),
                        property: property,
                        type: type,
                }
                //POST ADD REQUEST TO GET EFFECTIVE TIMES
                await client.apiClient.post(`/calendar/${this.props.calendar_id}/event`, form_data).then((resp) => {
                        return (resp.data);
                }).then(
                        (data) => {
                                const new_state = [];
                                for (var i = 0; i < data.length; i++) {
                                        new_state.push({
                                                title: data[i].title,
                                                desc: data[i].description,
                                                id: data[i].id_event,
                                                property: data[i].property,
                                                start: data[i].start_date,
                                                end: data[i].end_date,
                                                type: data[i].type,

                                        });
                                };
                                this.setState({ events: new_state });
                        }).catch((err => {
                                console.log(err);
                        }));

        }






        //  Updates Existing Appointments Title and/or Description
        updateEvent() {
                console.log("updateEvent()", this.state);
                const { id, title, desc, start, end, events, type, property, clickedEvent } = this.state;
                const index = events.findIndex(event => event === clickedEvent);
                console.log("POST request with event_id", this.state.id);
                console.log("POST remove event then add_event to calendar", this.state);

                const updatedEvent = events.slice();
                updatedEvent[index].id = id;
                updatedEvent[index].title = title;
                updatedEvent[index].desc = desc;
                updatedEvent[index].start = start;
                updatedEvent[index].end = end;
                updatedEvent[index].type = type;
                updatedEvent[index].property = property;

                // localStorage.setItem("cachedEvents", JSON.stringify(updatedEvent));
                this.setState({
                        events: updatedEvent
                });
        }








        //  filters out specific event that is to be deleted and set that variable to state
        deleteEvent() {
                console.log("deleteEvent()");
                console.log(this.state);
                console.log("POST request /removeEvent/event_id", this.state.id);

                let updatedEvents = this.state.events.filter(
                        event => event["id"] !== this.state.id
                );
                // localStorage.setItem("cachedEvents", JSON.stringify(updatedEvents));
                this.setState({ events: updatedEvents });
        }







        render() {
                console.log("render()- CalendarComponent");
                console.log("state calendar componenent", this.state);
                console.log("props", this.props);



                const eventActions = [
                        <FlatButton
                                label="Cancel"
                                primary={false}
                                keyboardFocused={true}
                                onClick={this.handleClose}
                        />,
                        <FlatButton
                                label="Delete"
                                secondary={true}
                                keyboardFocused={true}
                                onClick={() => {
                                        this.deleteEvent(), this.handleClose();
                                }}
                        />,
                        <FlatButton
                                label="Confirm Edit"
                                primary={true}
                                keyboardFocused={true}
                                onClick={() => {
                                        this.updateEvent(), this.handleClose()
                                }}
                        />
                ];

                const appointmentActions = [
                        <FlatButton label="Cancel" secondary={true} onClick={this.handleClose} />,
                        <FlatButton
                                label="Submit"
                                primary={true}
                                keyboardFocused={true}
                                onClick={() => {
                                        this.setNewAppointment(), this.handleClose();
                                }}
                        />
                ];
                console.log("this.state.events", this.state.events);



                return (
                        <div id="Calendar">
                                {/* react-big-calendar library utilized to render calendar*/}
                                <BigCalendar
                                        events={this.state.events}
                                        views={["month"]}
                                        timeslots={2}
                                        defaultView="month"
                                        defaultDate={new Date()}
                                        selectable={true}
                                        onSelectEvent={event => this.handleEventSelected(event)}
                                        onSelectSlot={slotInfo => this.handleSlotSelected(slotInfo)}
                                />

                                {/* Material-ui Modal for booking new appointment */}
                                <Dialog
                                        title={`Book an appointment on ${moment(this.state.start).format(
                                                "MMMM Do YYYY"
                                        )}`}
                                        actions={appointmentActions}
                                        modal={false}
                                        open={this.state.openSlot}
                                        onRequestClose={this.handleClose}
                                >
                                        <TextField
                                                floatingLabelText="Title"
                                                onChange={e => {
                                                        this.setTitle(e.target.value);
                                                }}
                                        />
                                        <br />
                                        <TextField
                                                floatingLabelText="Description"
                                                onChange={e => {
                                                        this.setDescription(e.target.value);
                                                }}
                                        />
                                        <br />
                                        <TextField
                                                floatingLabelText="Type"
                                                onChange={e => {
                                                        this.setType(e.target.value);
                                                }}
                                        />
                                        <br />
                                        <TextField
                                                floatingLabelText="Property"
                                                onChange={e => {
                                                        this.setProperty(e.target.value);
                                                }}
                                        />
                                        <TextField
                                                floatingLabelText="id (tmp)"
                                                onChange={e => {
                                                        this.setID(e.target.value);
                                                }}
                                        />
                                        <TimePicker
                                                format="ampm"
                                                floatingLabelText="Start Time"
                                                minutesStep={5}
                                                value={this.state.start}
                                                onChange={this.handleStartTime}
                                        />
                                        <TimePicker
                                                format="ampm"
                                                floatingLabelText="End Time"
                                                minutesStep={5}
                                                value={this.state.end}
                                                onChange={this.handleEndTime}
                                        />
                                </Dialog>

                                {/* Material-ui Modal for Existing Event */}
                                <Dialog
                                        title={`View/Edit Appointment of ${moment(this.state.start).format(
                                                "MMMM Do YYYY"
                                        )}`}
                                        actions={eventActions}
                                        modal={false}
                                        open={this.state.openEvent}
                                        onRequestClose={this.handleClose}
                                >
                                        <TextField
                                                defaultValue={this.state.title}
                                                floatingLabelText="Title"
                                                onChange={e => {
                                                        this.setTitle(e.target.value);
                                                }}
                                        />
                                        <br />
                                        <TextField
                                                floatingLabelText="Description"
                                                multiLine={true}
                                                defaultValue={this.state.desc}
                                                onChange={e => {
                                                        this.setDescription(e.target.value);
                                                }}
                                        />
                                        <TimePicker
                                                format="ampm"
                                                floatingLabelText="Start Time"
                                                minutesStep={5}
                                                value={this.state.start}
                                                onChange={this.handleStartTime}
                                        />
                                        <TimePicker
                                                format="ampm"
                                                floatingLabelText="End Time"
                                                minutesStep={5}
                                                value={this.state.end}
                                                onChange={this.handleEndTime}
                                        />
                                </Dialog>
                        </div>
                );
        }

}

export default CalendarComponent;

