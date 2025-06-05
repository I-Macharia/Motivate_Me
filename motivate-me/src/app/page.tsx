'use client';

import Link from "next/link";
import { useRouter } from 'next/navigation';
import { useEffect } from 'react';
import { useGateway } from '@civic/ethereum-gateway-react';
import "../app/globals.css"; // Correct relative path

// This is the main page of the Motivate Me app
// It serves as the entry point for users to navigate to login or profile pages
// The page includes a welcome message and links to the login and profile pages
// The styles are imported from the global CSS file
export default function Home() {
  const router = useRouter();
  const { gatewayToken } = useGateway();

  useEffect(() => {
    // If user has a valid Civic token, redirect to profile
    if (gatewayToken) {
      router.push('/profile');
    }
  }, [gatewayToken, router]);

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full space-y-8">
        <div>
          <h1 className="text-4xl font-bold text-center text-gray-900">
            Welcome to Motivate Me
          </h1>
          <p className="mt-4 text-center text-gray-600">
            Your daily dose of inspiration, powered by words that move you.
          </p>
        </div>
        <div className="mt-8">
          <button
            onClick={() => router.push('/login')}
            className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Get Started
          </button>
        </div>
      </div>
    </div>
  );
}