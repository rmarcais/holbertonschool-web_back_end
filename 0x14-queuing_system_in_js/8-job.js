import kue from 'kue';

export default function createPushNotificationsJobs(jobs, queue) {
  if (!(jobs instanceof(Array))) {
    throw Error('Jobs is not an array');
  }
  for (const item of jobs) {
    const job = queue.create('push_notification_code_3', item).save((error) => {
      if (!error) console.log(`Notification job created: ${job.id}`);
    });
    job.on('complete', () => {
      console.log(`Notification job #${job.id} completed`);
    });
    
    job.on('failed', (error) => {
      console.log(`Notification job #${job.id} failed: ${error.toString()}`);
    });
  
    job.on('progress', (progress) => {
        console.log(`Notification job #${job.id} ${progress}% complete`);  
    });
  }
}
