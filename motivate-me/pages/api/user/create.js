export default async function handler(req, res) {
  if (req.method === "POST") {
    const { username, email } = req.body;
    // Logic to create a new user
    res.status(201).json({ message: "User created successfully!" });
  } else {
    res.status(405).json({ error: "Method not allowed." });
  }
}
