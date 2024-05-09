export default function handleResponseFromAPI(promise) {
  // Function takes promise as input and returns new promise
  return promise
    // Asynch handling for API response
    // Resolve with success response object
    .then(() => ({
      status: 200,
      body: 'success',
    }))
    // Reject with empty error object
    .catch(() => Error())
    // Regardless, log API response message
    .finally(() => console.warn('Got a response from the API'));
}
