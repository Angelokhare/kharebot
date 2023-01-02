import React from "react"
import ReactDOM from "react-dom";
import {BrowserRouter as Router, Routes, Route} from "react-router-dom"
// import './style.css';
import LoginPage from "./components/Login";
import SignupPage from "./components/Signup";
// import UserDetailsPage from "./components/UserDetails";
// import DashboardPage from "./components/Dashboard";
// import UserPage from "./components/User";


export default function App() {
  return (
    <Router>
      <Routes>
      <Route path="/" element={<LoginPage />} />
          <Route index element={<LoginPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/signup" element={<SignupPage />} />
          {/* <Route path="/dashboard" element={<Dashboard />} /> */}
          {/* <Route path="/user" element={<UserPage/>} /> */}
          {/* <Route path="*" element={<ErrorPage />} /> */}
        {/* </Route> */}
      </Routes>
    </Router>
  );
}

// const root = ReactDOM.createRoot(document.querySelector(".connection"));
// root.render(<App />);

ReactDOM.render(<App />, document.getElementById('root'));