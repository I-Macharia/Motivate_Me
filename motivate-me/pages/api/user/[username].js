export default async function handler(req, res) {
  if (req.method === "GET") {
    const { username } = req.query;
    // Logic to fetch user details by username
    res.status(200).json({ message: `User details for ${username}` });
  } else {
    res.status(405).json({ error: "Method not allowed." });
  }
}
