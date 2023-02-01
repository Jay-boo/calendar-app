import React from 'react';

function FormInput({ label, name, error, value, onChange, type = "text" }) {
  return <div>
    <label className="block mb-2 text-teal-500" htmlFor={name}>{label}</label>
    <input
      type={type}
      name={name}
      value={value}
      onChange={onChange}
    />
  </div>
}

export default FormInput;
