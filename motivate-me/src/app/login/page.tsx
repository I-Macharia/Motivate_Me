"use client"

import { useGateway } from "@civic/ethereum-gateway-react";
import { useState } from "react";
import "@/app/globals.css";

export default function Login() {
    const { requestGatewayToken, gatewayToken } = useGateway();
    const [status, setStatus] = useState("");
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");

    const handleLogin = async () => {
        try {
            if (requestGatewayToken) {
                await requestGatewayToken();
            } else {
                setStatus("Gateway token request function is unavailable.");
                return;
            }

            const response = await fetch("../api/saveUser", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    username,
                    civicPassId: gatewayToken?.identifier,
                    email,
                }),
            });

            const data = await response.json();
            setStatus(data.message || "Civic Pass issued successfully!");
        } catch {
            setStatus("Failed to issue Civic Pass.");
        }
    };

    return (
        <div className="login-container">
            <h1>Login</h1>
            <input
                type="text"
                placeholder="Username"
                value={username}
                onChange={e => setUsername(e.target.value)}
            />
            <input
                type="email"
                placeholder="Email"
                value={email}
                onChange={e => setEmail(e.target.value)}
            />
            <button onClick={handleLogin}>Login with Civic Pass</button>
            {status && <p>{status}</p>}
        </div>
    );
}