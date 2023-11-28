import { createClient } from "redis";

const sub = createClient()
  .on("error", (error) =>
    console.log(`Redis client not connected to the server: ${error}`)
  )
  .on("ready", () => console.log("Redis client connected to the server"));

sub.subscribe("holberton school channel");

sub.on("message", (channel, message) => {
  if (channel === "holberton school channel") {
    console.log(message);
    if (message === "KILL_SERVER") {
      sub.unsubscribe("holberton school channel");
      sub.quit();
    }
  }
});
