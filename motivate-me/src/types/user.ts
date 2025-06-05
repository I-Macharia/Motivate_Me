// Types for user-related data
export interface User {
  id: string;
  username: string;
  email?: string;
  civicPassId?: string;
  createdAt: Date;
  updatedAt: Date;
}

export interface CreateUserRequest {
  username: string;
  email?: string;
  civicPassId?: string;
}

export interface UpdateUserRequest {
  email?: string;
  civicPassId?: string;
}

export interface UserResponse {
  user: User;
  message: string;
}

export interface ErrorResponse {
  error: string;
}
