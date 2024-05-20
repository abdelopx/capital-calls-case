import { IInvestor } from "./investors";

const API_URL = import.meta.env.VITE_API_URL;

export interface IBill {
  id: number;
  bill_type: string;
  amount: number;
  due_date: string;
  investor: IInvestor;
}

export interface ICapitalCalls {
  total_amount: string;
  status: string;
  investor: number
  bills: number[];
}

export async function getAllCapitalBills() {
  const response = await fetch(API_URL + "/capital_calls");
  return (await response.json()) as ICapitalCalls[];
}

export async function addCapitalCall(capitalCall: ICapitalCalls) {
  await fetch(API_URL + "/capital_calls/", {
    method: "POST",
    body: JSON.stringify(capitalCall),
    headers: {
      "Content-Type": "application/json",
    },
  });
}
