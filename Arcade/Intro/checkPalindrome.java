boolean checkPalindrome(String inputString) {
    int counter = 0;
    int counter_final = inputString.length() - 1;
    
    while (counter < counter_final){
        if (inputString.charAt(counter) == inputString.charAt(counter_final)){
            counter++;
            counter_final--;
        } else {
            return false;
        }
        
    }
    return true;
}