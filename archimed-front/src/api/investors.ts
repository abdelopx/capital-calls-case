const API_URL = import.meta.env.VITE_API_URL;

export interface IInvestor {
  id: number;
  iban: string;
  name: string;
  email: string;
  joined_on: string;
}

export default async function addInvestor(investor: IInvestor) {
  await fetch(API_URL + "/investors/", {
    method: "POST",
    body: JSON.stringify(investor),
    headers: {
      "Content-Type": "application/json",
    },
  });
}

export async function getAllInvestors() {
  const response = await fetch(API_URL + "/investors/");
  return (await response.json()) as IInvestor[];
}

