import { GatewayProvider } from "@civic/ethereum-gateway-react";
import "../styles/globals.css";

function MyApp({ Component, pageProps }) {
  const wallet = {
    address: WALLET_ADDRESS, // Replace with the user's wallet address
    signer: null, // Replace with an ethers.js signer instance
  };

  const networkKey = "your-network-key"; // Replace with your Civic network key

  return (
    <GatewayProvider wallet={wallet} gatekeeperNetwork={networkKey}>
      <Component {...pageProps} />
    </GatewayProvider>
  );
}

export default MyApp;