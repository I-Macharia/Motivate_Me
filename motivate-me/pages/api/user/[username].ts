import type { NextApiRequest, NextApiResponse } from 'next';
import { User, UpdateUserRequest, UserResponse, ErrorResponse } from '@/types/user';
import { getUser, updateUser, deleteUser } from '@/utils/database';

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<UserResponse | ErrorResponse>
) {
  const { username } = req.query;

  if (!username || Array.isArray(username)) {
    return res.status(400).json({ error: 'Invalid username parameter' });
  }

  switch (req.method) {
    case 'GET':
      try {
        const user = await getUser(username);
        if (!user) {
          return res.status(404).json({ error: 'User not found' });
        }
        return res.status(200).json({ user, message: 'User found' });
      } catch (error) {
        console.error('Error fetching user:', error);
        return res.status(500).json({ error: 'Failed to fetch user' });
      }

    case 'PUT':
      try {
        const updates: UpdateUserRequest = req.body;
        const updatedUser = await updateUser(username, updates);
        if (!updatedUser) {
          return res.status(404).json({ error: 'User not found' });
        }
        return res.status(200).json({ user: updatedUser, message: 'User updated successfully' });
      } catch (error) {
        console.error('Error updating user:', error);
        return res.status(500).json({ error: 'Failed to update user' });
      }

    case 'DELETE':
      try {
        const success = await deleteUser(username);
        if (!success) {
          return res.status(404).json({ error: 'User not found' });
        }
        return res.status(200).json({ message: 'User deleted successfully' } as UserResponse);
      } catch (error) {
        console.error('Error deleting user:', error);
        return res.status(500).json({ error: 'Failed to delete user' });
      }

    default:
      return res.status(405).json({ error: 'Method not allowed' });
  }
}
