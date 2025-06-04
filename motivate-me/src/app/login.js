import { useGateway } from "@civic/ethereum-gateway-react";
import { useState } from "react";

export default function Login() {
  const { requestGatewayToken, gatewayToken } = useGateway();
  const [status, setStatus] = useState("");

  const handleLogin = async () => {
    try {
      await requestGatewayToken();

      const response = await fetch("/api/saveUser", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          username: "testUser", // Replace with actual username input
          civicPassId: gatewayToken?.tokenId,
          email: "test@example.com", // Replace with actual email input
        }),
      });

      const data = await response.json();
      setStatus(data.message || "Civic Pass issued successfully!");
    } catch (error) {
      setStatus("Failed to issue Civic Pass.");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Login</h1>
      <button onClick={handleLogin}>Login with Civic Pass</button>
      {status && <p>{status}</p>}
    </div>
  );
}