import ClassRoom from './0-classroom';

const initializeRooms = () => {
  /* Stores values in a new array */
  const classSize = [19, 20, 34];
  /* Creates new instances for each size in array! */
  return classSize.map((size) => new ClassRoom(size));
};

export default initializeRooms;
