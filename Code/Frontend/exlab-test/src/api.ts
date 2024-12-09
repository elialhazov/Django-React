import axios from "axios";


export const addNumbers = async (num1: number, num2: number): Promise<number> => {
    const response = await axios.post<{ result: number }>("/api/add-numbers/", { num1, num2 });
    return response.data.result;
};
