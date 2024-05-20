import { IInvestor } from "./investors";

const API_URL = import.meta.env.VITE_API_URL;

export interface IBill {
  id: number;
  bill_type: string;
  amount: number;
  due_date: any;
  investor: IInvestor;
}

export async function getAllBills() {
  const response = await fetch(API_URL + "/bills/");
  return (await response.json()) as IBill[];
}

export async function addBill(bill: IBill) {
  console.log(bill);
  await fetch(API_URL + "/bills/", {
    method: "POST",
    body: JSON.stringify({ ...bill, due_date: bill.due_date.format("YYYY-MM-DD") }),
    headers: {
      "Content-Type": "application/json",
    },
  });
}
