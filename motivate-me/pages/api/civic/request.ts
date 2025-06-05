import type { NextApiRequest, NextApiResponse } from 'next';

interface CivicRequestResponse {
  message: string;
}

interface ErrorResponse {
  error: string;
}

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<CivicRequestResponse | ErrorResponse>
) {
  if (req.method === "POST") {
    const { userId } = req.body;
    // Logic to request Civic Pass
    res.status(200).json({ message: "Civic Pass requested successfully!" });
  } else {
    res.status(405).json({ error: "Method not allowed." });
  }
}
