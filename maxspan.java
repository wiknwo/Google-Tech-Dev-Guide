public int maxSpan(int[] nums) {
  int maxspan = 0; // Sentinel

  if(nums.length == 1) return 1; // Quick return

  for(int i = 0;i < nums.length - 1;i++){
    
    int count = nums.length - 1;
    
    // Counting number of elements between the two inclusive
    while(nums[i] != nums[count])
      count--;
      
    // Calculating span
    int span = count - i + 1; // Adding 1 to prevent double counting
    if(span > maxspan) maxspan = span;
  }
  
  return maxspan;
}
