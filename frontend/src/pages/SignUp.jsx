import React, { useState, useEffect } from 'react';
import DashboardHeader from "../components/DashboardHeader";
import { Link, useNavigate } from "react-router-dom";
import FastAPIClient from '../client';
import config from '../config';
import Button from '../components/Button/Button';
import FormInput from '../components/FormInput/FormInput';

const client = new FastAPIClient(config);

const SignUp = () => {
  const [error, setError] = useState({ username: '', password: '' });
  const [registerForm, setRegisterForm] = useState({ username: '', password: '' });

  const [loading, setLoading] = useState(false)

  const navigate = useNavigate()

  const onRegister = (e) => {
    e.preventDefault();
    setLoading(true)
    setError(false);

    if (registerForm.username.length <= 0) {
      setLoading(false)
      return setError({ username: "Please Enter username" })
    }
    if (registerForm.password.length <= 0) {
      setLoading(false)
      return setError({ password: "Please Enter Password" })
    }
    console.log(registerForm);

    client.register(registerForm.username, registerForm.password)
      .then(() => {
        navigate('/login')
      })
      .catch((err) => {
        setLoading(false)
        setError(true);
        alert(err)
      });
  }

  return (
    <>
      <section className="bg-black ">
        <div className="flex items-center justify-center min-h-screen bg-gray-100 text-left ">
          <div className="w-full max-w-xs m-auto bg-indigo-100 rounded p-5 shadow-lg">
            <header>
              {/* <img className="w-20 mx-auto mb-5" src="https://img.icons8.com/fluent/344/year-of-tiger.png" /> */}
              <div className="flex items-center justify-center w-20 h-20 mx-auto mb-5 bg-teal-500 rounded-full ">
                <svg className=" h-8 w-8" width="54" height="54" viewBox="0 0 54 54" fill='white' xmlns="http://www.w3.org/2000/svg" >
                  <path d="M13.5 22.1c1.8-7.2 6.3-10.8 13.5-10.8 10.8 0 12.15 8.1 17.55 9.45 3.6.9 6.75-.45 9.45-4.05-1.8 7.2-6.3 10.8-13.5 10.8-10.8 0-12.15-8.1-17.55-9.45-3.6-.9-6.75.45-9.45 4.05zM0 38.3c1.8-7.2 6.3-10.8 13.5-10.8 10.8 0 12.15 8.1 17.55 9.45 3.6.9 6.75-.45 9.45-4.05-1.8 7.2-6.3 10.8-13.5 10.8-10.8 0-12.15-8.1-17.55-9.45-3.6-.9-6.75.45-9.45 4.05z" />
                </svg>
              </div>
            </header>
            <form onSubmit={(e) => onRegister(e)}>
              <FormInput
                type={"username"}
                name={"username"}
                label={"username"}
                error={error.username}
                value={registerForm.username}
                onChange={(e) => setRegisterForm({ ...registerForm, username: e.target.value })}
              />
              <FormInput
                type={"password"}
                name={"password"}
                label={"Password"}
                error={error.password}
                value={registerForm.password}
                onChange={(e) => setRegisterForm({ ...registerForm, password: e.target.value })}
              />
              <Button title={"Create Account"} onClick={(e) => onRegister(e)} error={error.password} loading={loading} />
            </form>

            <footer>
              <Link className="text-teal-700 hover:text-blue-900 text-sm float-right" to="/login">Already Have an account ?</Link>
            </footer>
          </div>
        </div>
      </section>
    </>
  )
}

export default SignUp;

