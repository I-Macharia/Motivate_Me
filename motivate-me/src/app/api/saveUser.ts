"use client";

import { NextApiRequest, NextApiResponse } from 'next';
import { IPFSService } from '@/utils/ipfsService';
import sqlite3 from 'sqlite3';
import { open } from 'sqlite';

interface SaveUserRequest {
  username: string;
  civicPassId: string;
  email?: string;
}

interface SaveUserResponse {
  message: string;
  ipfsHash: string;
}

interface ErrorResponse {
  error: string;
}

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<SaveUserResponse | ErrorResponse>
) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed.' });
  }

  try {
    const { username, civicPassId, email } = req.body as SaveUserRequest;

    const ipfsService = new IPFSService();

    // Generate metadata for IPFS
    const metadata = ipfsService.generateQuoteMetadata(
      `User: ${username}`,
      'Motivate Me App',
      ['Civic Pass', 'User Data'],
      undefined
    );

    // Upload metadata to IPFS
    const ipfsHash = await ipfsService.uploadQuoteMetadata(metadata);

    // Open database connection
    const db = await open({
      filename: process.env.DATABASE_PATH || './src/data/motivate_me.db',
      driver: sqlite3.Database,
    });

    // Save user data
    await db.run(
      `INSERT INTO users (username, civic_pass_id, email, ipfs_hash) 
       VALUES (?, ?, ?, ?)`,
      [username, civicPassId, email, ipfsHash]
    );

    return res.status(200).json({ 
      message: 'User saved successfully!',
      ipfsHash 
    });
  } catch (error) {
    console.error('Error saving user:', error);
    return res.status(500).json({ error: 'Failed to save user.' });
  }
}
