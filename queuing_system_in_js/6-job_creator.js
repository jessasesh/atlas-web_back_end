import kue from 'kue';

// Create queue
const queue = kue.createQueue();

const jobData = {
  phoneNumber: '123-456-7890',
  message: 'Hello, this is a notification message!',
};

// Create job
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) {
      console.error('Error creating job:', err);
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });

  // Listeners
job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', (err) => {
  console.log('Notification job failed:', err);
});
