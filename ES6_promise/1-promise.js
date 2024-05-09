export default function getFullResponseFromAPI(success) {
  // Returns a promise
  return new Promise((resolve, reject) => {
    if (success === true) {
      // If successful, resolve promise with success response object
      resolve({
        status: 200,
        body: 'Success',
      });
    } else {
      // If unsuccessful, reject promise with error object
      reject(new Error('The fake API is not working currently'));
    }
  });
}
