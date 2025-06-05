import type { NextApiRequest, NextApiResponse } from 'next';
import { CreateUserRequest, UserResponse, ErrorResponse } from '@/types/user';
import { createUser } from "../../../utils/database";

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<UserResponse | ErrorResponse>
) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const userData: CreateUserRequest = req.body;
    const user = await createUser(userData);
    
    return res.status(201).json({
      user,
      message: 'User created successfully'
    });
  } catch (error) {
    console.error('Error creating user:', error);
    return res.status(500).json({
      error: 'Failed to create user'
    });
  }
}
