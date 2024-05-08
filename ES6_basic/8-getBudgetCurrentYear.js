// Function to get the current year
function getCurrentYear() {
  // Create a new Date object to get the current date and time
  const date = new Date();
  // Return the year using the getFullYear method
  return date.getFullYear();
}

// Export a function to get the budget for the current year
export default function getBudgetForCurrentYear(income, gdp, capita) {
  // Initialize an empty object to store the budget
  const budget = {
    // Use ES6 computed property names to dynamically generate property names
    [`income-${getCurrentYear()}`]: income,
    [`gdp-${getCurrentYear()}`]: gdp,
    [`capita-${getCurrentYear()}`]: capita,
  };

  // Return the budget object
  return budget;
}
