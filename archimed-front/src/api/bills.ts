import { IInvestor } from "./investors";

const API_URL = import.meta.env.VITE_API_URL;

export interface IBill {
  amount: number | null;
  name: string;
  investment_date: any;
  bill_type: string;
  investor: number | null;
  fee_percentage: number;
  id: number;
}

export async function getAllBills() {
  const response = await fetch(API_URL + "/bills/");
  return (await response.json()) as IBill[];
}

export async function addBill(bill: IBill) {
  console.log(bill);
  await fetch(API_URL + "/bills/generate_bills/", {
    method: "POST",
    body: JSON.stringify({
      ...bill,
      investment_date: bill.investment_date.format("YYYY-MM-DD"),
      fee_percentage: bill.fee_percentage / 100,
      amount: Number(bill.amount),
    }),
    headers: {
      "Content-Type": "application/json",
    },
  });
}
