import { useGateway } from "@civic/ethereum-gateway-react";

export default function Profile() {
  const { gatewayToken } = useGateway();

  return (
    <div style={{ padding: "20px" }}>
      <h1>User Profile</h1>
      {gatewayToken ? (
        <p>Your Civic Pass is active!</p>
      ) : (
        <p>Your Civic Pass is not active. Please issue a new one.</p>
      )}
    </div>
  );
}