import { create } from "ipfs-http-client";

const client = create({ url: "https://ipfs.infura.io:5001" });

export async function uploadToIPFS(data) {
  try {
    const result = await client.add(JSON.stringify(data));
    return result.path; // IPFS hash
  } catch (error) {
    console.error("Failed to upload to IPFS:", error);
    return null;
  }
}
