function checkThreeAndTwo(array) {
    // Create a store storing keys as array items and values as number of occurances
    // Iterate over the array
    // For every value in the array, increment it's value in the store
    //  Check if the values in the store have three and two present
    
    let store = {};
    
    for(val of array) 
    {
      store[val] = 0
    }
    
    for (val of array) 
    {
      store[val] = store[val] + 1;
  
    }
    
    return (Object.values(store).includes(3) && Object.values(store).includes(2) );
  }