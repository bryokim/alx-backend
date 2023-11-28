import kue from "kue";

const push_notification_code = kue.createQueue();

const job = push_notification_code
  .createJob("push_notification_code", {
    phoneNumber: "4153518780",
    message: "This is the code to verify your account",
  })
  .save((err) => {
    if (err) console.log("Notification job failed");
    else console.log(`Notification job created: ${job.id}`);
  });

job.on("complete", (result) => console.log("Notification job completed"));
