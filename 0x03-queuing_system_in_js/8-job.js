export default function createPushNotificationsJobs(jobs, queue) {
  if (!(jobs instanceof Array)) {
    throw new Error("Jobs is not an array");
  }

  jobs.forEach((job) => {
    const j = queue.createJob("push_notification_code_3", job);

    j.on("enqueue", () => {
      console.log(`Notification job created: ${j.id}`);
    })
      .on("complete", () => {
        console.log(`Notification job ${j.id} completed`);
      })
      .on("failed", (errorMessage) => {
        console.log(`Notification job ${j.id} failed: ${errorMessage}`);
      })
      .on("progress", (progress, _data) => {
        console.log(`Notification job ${j.id} ${progress}% complete`);
      });

    j.save();
  });
}
