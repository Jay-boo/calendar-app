import CalendarDashboard from "../components/CalendarDashBoard";
import React from "react";
import { Link } from "react-router-dom";

const DashBoard = () => {
  return (
    <div>
      <Link to="/login"> To login page</Link>

      <CalendarDashboard />
    </div>
  )
}
export default DashBoard;

