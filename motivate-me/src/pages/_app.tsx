import type { AppProps } from 'next/app';
import { GatewayProvider } from '@civic/ethereum-gateway-react';
import '../styles/globals.css';

function MyApp({ Component, pageProps }: AppProps) {
  // You should replace these with actual values from your environment variables
  const wallet = {
    address: process.env.NEXT_PUBLIC_WALLET_ADDRESS || '',
    signer: undefined,
  };

  const networkKey = process.env.NEXT_PUBLIC_CIVIC_NETWORK_KEY || '';

  return (
    <GatewayProvider wallet={wallet} gatekeeperNetwork={networkKey}>
      <Component {...pageProps} />
    </GatewayProvider>
  );
}

export default MyApp;
