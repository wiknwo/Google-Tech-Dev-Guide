public int sumNumbers(String str) {
  int sum = 0;
  String valueString = "";
  for (int i = 0; i < str.length(); i++){
    char c = str.charAt(i);        
    //Process char
    if(Character.isDigit(c) && (i == str.length() - 1)){
      valueString += c;
      sum += Integer.parseInt(valueString);
      valueString = "";
    }
    
    else if(Character.isDigit(c)){
      valueString += c;
    } 
    
    else if(!Character.isDigit(c) && valueString.isEmpty()){
      sum = sum + 0;
    }
    
    else if(!Character.isDigit(c) && !valueString.isEmpty()){
      sum += Integer.parseInt(valueString);
      valueString = "";
    }
  }
  return sum;
}