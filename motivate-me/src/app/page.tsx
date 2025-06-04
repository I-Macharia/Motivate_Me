import Link from "next/link";

export default function Home() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>Welcome to Motivate Me!</h1>
      <nav>
        <ul>
          <li>
            <Link href="/my-streamlit-app/motivate-me/src/app/login.js">Login</Link>
          </li>
          <li>
            <Link href="/my-streamlit-app/motivate-me/src/app/profile.js">Profile</Link>
          </li>
        </ul>
      </nav>
    </div>
  );
}