/**
 * William Ikenna-Nwosu (wiknwo)
 *
 * interpret
 *
 * Write a simple interpreter which understands "+", "-", 
 * and "*" operations. Apply the operations in order using 
 * command/arg pairs starting with the initial value of 
 * "value". If you encounter an unknown command, return -1.
 *
 * interpret(1, ["+"], [1]) → 2
 * interpret(4, ["-"], [2]) → 2
 * interpret(1, ["+", "*"], [1, 3]) → 6
 **/
public int interpret(int value, String[] commands, int[] args) {
    int finalValue = value;
    
    // Processing tokens
    for(int i = 0;i < args.length;i++){
      if(commands[i].equals("+")) {
        finalValue += args[i];
      } else if (commands[i].equals("-")) {
        finalValue -= args[i];
      } else if(commands[i].equals("*")) {
        finalValue *= args[i];
      } else {
        return -1;
      }
    }
    
    return finalValue;
}