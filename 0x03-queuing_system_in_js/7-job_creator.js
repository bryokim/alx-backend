import kue from "kue";

const jobs = [
  {
    phoneNumber: "4153518780",
    message: "This is the code 1234 to verify your account",
  },
  {
    phoneNumber: "4153518781",
    message: "This is the code 4562 to verify your account",
  },
  {
    phoneNumber: "4153518743",
    message: "This is the code 4321 to verify your account",
  },
  {
    phoneNumber: "4153538781",
    message: "This is the code 4562 to verify your account",
  },
  {
    phoneNumber: "4153118782",
    message: "This is the code 4321 to verify your account",
  },
  {
    phoneNumber: "4153718781",
    message: "This is the code 4562 to verify your account",
  },
  {
    phoneNumber: "4159518782",
    message: "This is the code 4321 to verify your account",
  },
  {
    phoneNumber: "4158718781",
    message: "This is the code 4562 to verify your account",
  },
  {
    phoneNumber: "4153818782",
    message: "This is the code 4321 to verify your account",
  },
  {
    phoneNumber: "4154318781",
    message: "This is the code 4562 to verify your account",
  },
  {
    phoneNumber: "4151218782",
    message: "This is the code 4321 to verify your account",
  },
];

const queue = kue.createQueue();

jobs.forEach((job) => {
  const j = queue.createJob("push_notification_code_2", job).save((err) => {
    if (err) console.log(err);
    else console.log(`Notification job created: ${j.id}`);
  });

  j.on("complete", (result) => {
    console.log(`Notification job ${j.id} completed`);
  })
    .on("failed", (errorMessage) => {
      console.log(`Notification job ${j.id} failed: ${errorMessage}`);
    })
    .on("progress", (progress, data) => {
      console.log(`Notification job ${j.id} ${progress}% complete`);
    });
});
