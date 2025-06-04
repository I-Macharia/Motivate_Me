import Link from "next/link";

export default function Home() {
  return (
    <div style={{ padding: "20px" }}>
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