import { MuiThemeProvider } from "material-ui/styles";
import React from "react";
import FastAPIClient from "../client";
import config from "../config";
import CalendarComponent from "./CalendarComponent";

const client = new FastAPIClient(config);

class CalendarDashboard extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      calendars_id: [],
      selected_id: 0,
    };
    this.create = this.create.bind(this);
  }

  componentDidMount() {
    console.log("componentDidMount()");
    // get all entities - GET
    client.getCalendar()
      .then(response => {
        this.setState({
          calendars_id: response.map((cal) => cal.calendar_id)
        })
      })
      .catch(err => {
        console.log(err);
      });

  }
  async create(e) {
    console.log("create()");
    // const calendars_id = this.state.calendars_id.slice();
    let previous_state = this.state.calendars_id;
    // const new_cal = client.addCalendar().then((response) => { return (response) });
    await client.apiClient.post("/create_calendar").then((resp) => {
      return (resp.data.calendar_id);
    }).then(
      (data) => {
        previous_state.push(data)
      })
    this.setState({ calendars_id: previous_state });

  }


  // get_calendars() {
  //   console.log("getCalendar");
  //
  //   // const calendars = client.getCalendar().then((resp) => { return resp.data; });
  //   // this.state.calendars_id = calendars;
  //   client.getCalendar().then((data) => { this.setState({ calendars_id: data }); });
  //
  //   // this.setState({ calendars_id: calendars });
  //   console.log(this.state);
  //
  //
  //   // this.state.calendars_id = [1, 2, 3];
  // }

  handleChange(e) {
    console.log("handleChange");
    console.log(e.target.value);

    this.setState({ selected_id: e.target.value });
  }

  render() {
    console.log("render()");
    console.log("props", this.props);
    console.log("state", this.state);

    const buttonGrp = this.state.calendars_id.map((cal_id) => {
      return <option value={cal_id}>{cal_id}</option>;
    });

    return (
      <div>
        <h1>CalendarDashBoard</h1>
        <button onClick={(e) => this.create(e)}> Add Calendar</button>
        {this.state.calendars_id.length > 0 && (
          <select onChange={(e) => this.handleChange(e)} name="calendar_id">
            <option value="0"> Select calendar </option>
            {buttonGrp}
          </select>
        )}
        {this.state.calendars_id.length == 0 && (<span> No calendars</span>)}
        {this.state.selected_id > 0 && (
          <MuiThemeProvider>
            <CalendarComponent calendar_id={this.state.selected_id} />
          </MuiThemeProvider>
        )}
      </div>
    );
  }
}

export default CalendarDashboard;

