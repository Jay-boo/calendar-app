import { MuiThemeProvider } from "material-ui/styles";
import React from "react";
import CalendarComponent from "./CalendarComponent";



class CalendarDashboard extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      calendars_id: [],
      selected_id: 0
    };
  }
  get_calendars() {
    this.state.calendars_id = [1, 2, 3];
  }

  handleChange(e) {
    console.log("handleChange");
    console.log(e.target.value);

    this.setState({ selected_id: e.target.value });
  }

  render() {
    console.log("render()");
    this.get_calendars();
    console.log("calendars", this.state.calendars_id);

    const buttonGrp = this.state.calendars_id.map((cal_id) => {
      return <option value={cal_id}>{cal_id}</option>;
    });

    return (
      <div>
        <h1>CalendarDashBoard</h1>
        {this.state.calendars_id.length > 0 && (
          <select onChange={(e) => this.handleChange(e)} name="calendar_id">
            <option value="0"> Select calendar </option>
            {buttonGrp}
          </select>
        )}
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

