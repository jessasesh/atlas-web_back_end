export default function guardrail(mathFunction) {
  const queue = [];
  let valueReturned;
  try {
    // Execute mathFunction and store result
    valueReturned = mathFunction();
  } catch (error) {
    valueReturned = error.toString();
  }
  // Append value/message and return new array
  queue.push(valueReturned);
  queue.push('Guardrail was processed');
  return queue;
}
