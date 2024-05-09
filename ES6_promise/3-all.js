import { uploadPhoto, createUser } from './utils';

// Asynch handling for profile signup process
export default function handleProfileSignup() {
  // Concurrently execute the uploadPhoto() and createUser() functions
  return Promise.all([uploadPhoto(), createUser()])
    // Breakdown response objects
    .then((response) => {
      // Extract the body from photo upload response
      const { body } = response[0];
      // Extract first/last names from user response
      const { firstName, lastName } = response[1];
      console.log(`${body} ${firstName} ${lastName}`);
    })
    // Log error message if any promise rejects
    .catch(() => console.log('Signup system offline'));
}
