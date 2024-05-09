export default function createInt8TypedArray(length, position, value) {
  // Create new ArrayBuffer with specified length
  const buffer = new ArrayBuffer(length);
  // Create a new DataView to access and manipulate the ArrayBuffer
  const view = new DataView(buffer);
  // Range postion validator, error if outside range
  if (position > length - 1) {
    throw Error('Position outside range');
  }

  // Set Int8 value at specific postition
  view.setInt8(position, value);
  return view;
}
