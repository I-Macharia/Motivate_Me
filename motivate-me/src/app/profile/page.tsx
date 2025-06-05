"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useGateway } from "@civic/ethereum-gateway-react";
import "@/app/globals.css";
import type { User } from "@/types/user";

export default function Profile() {
  const router = useRouter();
  const { gatewayToken } = useGateway();
  const [profile, setProfile] = useState<User | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchProfile = async () => {
      if (!gatewayToken) {
        router.push("/login");
        return;
      }

      try {
        const response = await fetch(`/api/user/${gatewayToken.identifier}`);
        if (!response.ok) {
          throw new Error("Failed to fetch profile");
        }
        const data = await response.json();
        setProfile(data.user);
      } catch (err) {
        setError(err instanceof Error ? err.message : "An error occurred");
      } finally {
        setLoading(false);
      }
    };

    fetchProfile();
  }, [gatewayToken, router]);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <p>Loading...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <p className="text-red-600">Error: {error}</p>
      </div>
    );
  }

  if (!profile) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <p>No profile found</p>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md mx-auto">
        <h1 className="text-3xl font-bold mb-8">Profile</h1>
        <div className="bg-white shadow rounded-lg p-6">
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700">
                Username
              </label>
              <p className="mt-1 text-sm text-gray-900">{profile.username}</p>
            </div>
            {profile.email && (
              <div>
                <label className="block text-sm font-medium text-gray-700">
                  Email
                </label>
                <p className="mt-1 text-sm text-gray-900">{profile.email}</p>
              </div>
            )}
            {profile.civicPassId && (
              <div>
                <label className="block text-sm font-medium text-gray-700">
                  Civic Pass ID
                </label>
                <p className="mt-1 text-sm text-gray-900">
                  {profile.civicPassId}
                </p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}