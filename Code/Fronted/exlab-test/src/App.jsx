import React, { useState } from "react";
import { addNumbers } from "./api";
import "bootstrap/dist/css/bootstrap.min.css";
import './App.css';

function App() {
    const [num1, setNum1] = useState("");
    const [num2, setNum2] = useState("");
    const [result, setResult] = useState(null);
    const [error, setError] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            setError(null);
            const data = await addNumbers(Number(num1), Number(num2));
            setResult(data.result);
        } catch (err) {
            setError("Failed to calculate. Please try again.");
        }
    };

    return (
        <div className="container mt-5">
            <div className="card shadow p-4">
                <h1 className="text-center text-primary">Sum Calculator</h1>
                <form onSubmit={handleSubmit} className="mt-4">
                    <div className="mb-3">
                        <label htmlFor="num1" className="form-label">First Number</label>
                        <input
                            type="number"
                            className="form-control"
                            id="num1"
                            value={num1}
                            onChange={(e) => setNum1(e.target.value)}
                            placeholder="Enter first number"
                            required
                        />
                    </div>
                    <div className="mb-3">
                        <label htmlFor="num2" className="form-label">Second Number</label>
                        <input
                            type="number"
                            className="form-control"
                            id="num2"
                            value={num2}
                            onChange={(e) => setNum2(e.target.value)}
                            placeholder="Enter second number"
                            required
                        />
                    </div>
                    <button type="submit" className="btn btn-primary w-100">Calculate</button>
                </form>
                {error && <p className="alert alert-danger mt-4">{error}</p>}
                {result !== null && <p className="alert alert-success mt-4">Result: {result}</p>}
            </div>
        </div>
    );
}

export default App;
