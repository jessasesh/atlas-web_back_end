// Importing the getBudgetObject function from an external module
import getBudgetObject from './7-getBudgetObject.js';

// Defining a function to get the full budget object
export default function getFullBudgetObject(income, gdp, capita) {
  // Getting the budget object using the imported function
  const budget = getBudgetObject(income, gdp, capita);

  // Creating the fullBudget object with additional methods
  const fullBudget = {
    // Spread operator to include properties from the budget object
    ...budget,

    // Method to convert income to dollars
    getIncomeInDollars(income) {
      return `$${income}`;
    },

    // Method to append "euros" to income
    getIncomeInEuros(income) {
      return `${income} euros`;
    },
  };

  // Returning the full budget object
  return fullBudget;
}
