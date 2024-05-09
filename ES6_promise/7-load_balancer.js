// Initiate downloads simultaneously from China/US
export default function loadBalancer(chinaDownload, USDownload) {
  // Return the result of the fastest one
  return Promise.race([chinaDownload, USDownload]);
}
