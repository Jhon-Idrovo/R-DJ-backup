import React from "react";
import "./styles/Expense.css";

function Expense({ exp }) {
  return (
    <>
      <tr>
        <td>{exp.date}</td>
        <td>{exp.exp_type}</td>
        <td>{exp.description}</td>
        <td>{exp.amount}</td>
      </tr>
    </>
  );
}

export default Expense;
