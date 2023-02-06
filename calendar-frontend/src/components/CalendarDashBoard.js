import TextField from "material-ui/TextField";
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
      calendars: [],
      selected_id: 0,
      name_new_cal: ""
    };
    this.create = this.create.bind(this);
  }
  setName(e) {
    this.setState({ name_new_cal: e })
  }

  componentDidMount() {
    console.log("componentDidMount()");
    // get all entities - GET
    client.getCalendar()
      .then(response => {
        console.log("response", response);

        this.setState({
          calendars: response
        })
      })
      .catch(err => {
        console.log(err);
      });

  }
  async create(e) {
    console.log("create()");
    console.log("actual state", this.state);
    // const calendars_id = this.state.calendars_id.slice();
    let previous_state = this.state.calendars;
    // const new_cal = client.addCalendar().then((response) => { return (response) });
    await client.apiClient.post(`/calendar/${this.state.name_new_cal}`).then((resp) => {
      console.log("creast POST data", resp.data);
      return (resp.data);
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
    console.log(e.target.value);

    this.setState({ selected_id: e.target.value });
  }

  render() {
    console.log("render()");
    console.log("props", this.props);
    console.log("state", this.state);

    const buttonGrp = this.state.calendars.map((cal_id) => {
      return <option value={cal_id.id_calendar}>{cal_id.name_calendar}</option>;
    });

    return (
      <div>
        <h1>CalendarDashBoard</h1>

        <MuiThemeProvider>
          <TextField
            floatingLabelText="calendar name"
            onChange={e => { this.setName(e.target.value); }} />
        </MuiThemeProvider>


        <button onClick={(e) => this.create(e)}> Add Calendar</button>

        <hr />
        {this.state.calendars.length > 0 && (
          <select onChange={(e) => this.handleChange(e)} name="calendar_id">
            <option value="0"> Select calendar </option>
            {buttonGrp}
          </select>
        )}
        {this.state.calendars.length == 0 && (<span> No calendars</span>)}
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

