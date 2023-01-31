import React from 'react';
import ReactDOM from 'react-dom';
import App from "./App";


import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./pages/Layout";
import Home from "./pages/home";
import Calendar_bis from './pages/Calendar';


// export default function App() {
//   return (
//     <BrowserRouter>
//       <Routes>
//         <Route path="/" element={<Layout />}>
//           <Route index element={<Home />} />
//           <Route path="calendar" element={<Calendar_bis />} />
//         </Route>
//       </Routes>
//     </BrowserRouter>
//   );
// }
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);



