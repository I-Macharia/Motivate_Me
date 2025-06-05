// app/profile/page.tsx
"use client";


import { useGateway } from "@civic/ethereum-gateway-react";
import "@/app/globals.css"; // Adjust the path as necessary


export default function Profile() {
    const { gatewayToken } = useGateway();

        <div className="profile-container">
            <h1>User Profile</h1>
            {gatewayToken ? (
                <p>Your Civic Pass is active!</p>
            ) : (
                <p>Your Civic Pass is not active. Please issue a new one.</p>
            )}
        </div>
}