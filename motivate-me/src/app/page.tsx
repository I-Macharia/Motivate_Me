import Link from "next/link";
import "../app/globals.css"; // Correct relative path

// This is the main page of the Motivate Me app
// It serves as the entry point for users to navigate to login or profile pages
// The page includes a welcome message and links to the login and profile pages
// The styles are imported from the global CSS file
export default function Home() {
  return (
    <div className="container">
      <h1>Welcome to Motivate Me!</h1>
      <nav>
        <ul>
          <li>
            <Link href="/login">Login</Link>
          </li>
          <li>
            <Link href="/profile">Profile</Link>
          </li>
        </ul>
      </nav>
    </div>
  );
}