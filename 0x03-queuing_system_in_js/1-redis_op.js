import { createClient, print } from "redis";

const client = createClient()
  .on("error", (error) =>
    console.log(`Redis client not connected to the server: ${error}`)
  )
  .on("ready", () => console.log("Redis client connected to the server"));

function setNewSchool(schoolName, value) {
  client.SET(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  client.GET(schoolName, (err, value) => console.log(value));
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
