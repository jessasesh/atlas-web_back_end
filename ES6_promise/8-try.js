// Math machine
export default function divideFunction(numerator, denominator) {
  // Validator
  if (denominator === 0) {
    throw Error('cannot divide by 0');
  }
  return (numerator / denominator);
}
