import { createCivicAuthPlugin } from "@civic/auth/nextjs"
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
};

const withCivicAuth = createCivicAuthPlugin({
  clientId: "6dbc833d-8441-47c3-a2e3-9361723eb526"
});

export default withCivicAuth(nextConfig)