'use client';

import { GatewayProvider } from '@civic/ethereum-gateway-react';
import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Motivate Me',
  description: 'Your daily dose of inspiration, powered by words that move you.',
};

interface RootLayoutProps {
  children: React.ReactNode;
}

export default function RootLayout({ children }: RootLayoutProps) {
  const wallet = {
    address: process.env.NEXT_PUBLIC_WALLET_ADDRESS ,
    signer: undefined // Using undefined instead of null
  };

  const networkKey = process.env.NEXT_PUBLIC_CIVIC_NETWORK_KEY || '';

  return (
    <html lang="en">
      <body>
        <GatewayProvider
          wallet={wallet}
          gatekeeperNetwork={networkKey}
        >
          {children}
        </GatewayProvider>
      </body>
    </html>
  );
}
