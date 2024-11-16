import axios from "axios";

// פונקציה לקריאת API לחישוב סכום
export const addNumbers = async (num1, num2) => {
    const response = await axios.post("/api/add-numbers/", { num1, num2 });
    return response.data;
};
