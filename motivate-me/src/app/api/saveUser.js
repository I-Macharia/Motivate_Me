import sqlite3 from "sqlite3";
import { open } from "sqlite";
import { uploadToIPFS } from "../../utils/ipfs";

export default async function handler(req, res) {
  if (req.method === "POST") {
    const { username, civicPassId, email } = req.body;

    try {
      const ipfsHash = await uploadToIPFS({ username, civicPassId, email });

      const db = await open({
        filename: "./src/data/motivate_me.db",
        driver: sqlite3.Database,
      });

      await db.run(
        `INSERT INTO users (username, civic_pass_id, email, ipfs_hash) VALUES (?, ?, ?, ?)`,
        [username, civicPassId, email, ipfsHash]
      );

      res.status(200).json({ message: "User saved successfully!", ipfsHash });
    } catch (error) {
      res.status(500).json({ error: "Failed to save user." });
    }
  } else {
    res.status(405).json({ error: "Method not allowed." });
  }
}