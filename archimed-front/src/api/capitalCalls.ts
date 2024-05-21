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
  investor: number;
  bills: number[];
  due_date: any;
}

export async function getAllCapitalBills() {
  const response = await fetch(API_URL + "/capital_calls");
  return (await response.json()) as ICapitalCalls[];
}

export async function addCapitalCall(capitalCall: ICapitalCalls) {
  await fetch(API_URL + "/capital_calls/generate_capital_call/", {
    method: "POST",
    body: JSON.stringify({ ...capitalCall, due_date: capitalCall.due_date.format("YYYY-MM-DD") }),
    headers: {
      "Content-Type": "application/json",
    },
  });
}
