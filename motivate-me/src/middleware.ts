import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

// Array of paths that require authentication
const protectedPaths = ['/profile'];

// Array of paths that are public
const publicPaths = ['/', '/login'];

export function middleware(request: NextRequest) {
  const path = request.nextUrl.pathname;
  const token = request.cookies.get('civic_token');

  // Allow access to public paths
  if (publicPaths.includes(path)) {
    return NextResponse.next();
  }

  // Check if path requires authentication
  if (protectedPaths.includes(path)) {
    // If no token exists, redirect to login
    if (!token) {
      return NextResponse.redirect(new URL('/login', request.url));
    }
  }

  // API routes protection
  if (path.startsWith('/api/') && !path.includes('/auth/')) {
    if (!token) {
      return NextResponse.json(
        { error: 'Authentication required' },
        { status: 401 }
      );
    }
  }

  return NextResponse.next();
}

export const config = {
  matcher: [
    /*
     * Match all request paths except:
     * - _next/static (static files)
     * - _next/image (image optimization files)
     * - favicon.ico (favicon file)
     * - public folder
     */
    '/((?!_next/static|_next/image|favicon.ico|public/).*)',
  ],
};
