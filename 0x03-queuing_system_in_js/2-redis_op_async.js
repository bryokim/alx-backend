import { createClient, print } from "redis";
import util from "node:util";

const client = createClient()
  .on("error", (error) =>
    console.log(`Redis client not connected to the server: ${error}`)
  )
  .on("ready", () => console.log("Redis client connected to the server"));

function setNewSchool(schoolName, value) {
  client.SET(schoolName, value, print);
}

client.get = util.promisify(client.get);

async function displaySchoolValue(schoolName) {
  await client.get(schoolName).then((value) => console.log(value));
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
