import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from "react-router-dom";
import FastAPIClient from '../client';
import config from '../config';
import FormInput from '../components/FormInput';
import jwtDecode from "jwt-decode";

const client = new FastAPIClient(config);

const Login = () => {
  const [error, setError] = useState({ username: "", password: "" });
  const [loginForm, setLoginForm] = useState({ username: '', password: '' });

  const [loading, setLoading] = useState(false)
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const navigate = useNavigate()

  const onLogin = (e) => {
    console.log(" on loging -------------------")
    console.log(isLoggedIn)
    e.preventDefault();
    setError(false);
    setLoading(true)

    if (loginForm.username.length <= 0) {
      setLoading(false)
      return setError({ username: "Please Enter username Address" })
    }
    if (loginForm.password.length <= 0) {
      setLoading(false)
      return setError({ password: "Please Enter Password" })
    }

    client.login(loginForm.username, loginForm.password)
      .then(() => {
        navigate('/')
      })
      .catch((err) => {
        setLoading(false)
        setError(true);
        console.log(err);
        alert('Invalid credentials');
      });
    setIsLoggedIn(true);

  }
  useEffect(() => {
    const tokenString = localStorage.getItem("token");
    if (tokenString) {
      const token = JSON.parse(tokenString);
      const decodedAccessToken = jwtDecode(token.access_token);
      if (JSON.stringify(token) !== JSON.stringify({ error: "invalid credentials" })) {
        setIsLoggedIn(true);
      }
    }
  }, []);




  const handleLogout = () => {
    client.logout();
    setIsLoggedIn(false)
    navigate('/login')
  }

  const handleLogin = () => {
    navigate("/login");
  }

  let displayButton;
  const buttonStyle = "inline-block text-sm px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-teal-500 hover:bg-white mt-4 lg:mt-0"

  if (isLoggedIn) {
    displayButton = <button className={buttonStyle} onClick={() => handleLogout()}>Logout</button>;
  } else {
    displayButton = <button className={buttonStyle} onClick={() => handleLogin()}>Login</button>;
  }


  return (
    <section className="bg-black ">
      <Link to="/"
        className="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white mx-4">
        HOME
      </Link>
      {displayButton}

      {!isLoggedIn && <Link
        className="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white"
        to={`/sign-up`}>
        Create Account
      </Link>}

      <div className="flex items-center justify-center min-h-screen bg-gray-100 text-left ">
        <div className="w-full max-w-xs m-auto bg-indigo-100 rounded p-5 shadow-lg">
          <form >

            <FormInput
              type={"text"}
              name={"username"}
              label={"Username"}
              error={error.username}
              value={loginForm.username}
              onChange={(e) => {
                setLoginForm({ ...loginForm, username: e.target.value });
              }}
            />
            <FormInput
              type={"password"}
              name={"password"}
              label={"Password"}
              error={error.username}
              value={loginForm.password}
              onChange={(e_bis) => {
                setLoginForm({
                  ...loginForm, password: e_bis.target.value
                });
              }}
            />
          </form>
          {/* <footer> */}
          {/*   <Link className="text-teal-700 hover:text-blue-900 text-sm float-right" to="/sign-up">Create Account</Link> */}
          {/* </footer> */}
        </div>
        <button onClick={(e) => {
          onLogin(e);
        }}>Submit</button>
      </div>
    </section>
  )
}

export default Login;

