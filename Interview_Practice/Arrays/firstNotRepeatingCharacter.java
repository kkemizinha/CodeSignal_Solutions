char firstNotRepeatingCharacter(String s) {
    LinkedHashMap<Character, Integer> map = new LinkedHashMap<Character, Integer>();
    for (int i = 0; i < s.length(); i++){
        Integer count =  map.get(s.charAt(i));
        if (count == null) {
            map.put(s.charAt(i), 1);
        } else {
            map.put(s.charAt(i), count + 1);
        }
    }
    
    
    for (HashMap.Entry<Character, Integer> entry : map.entrySet()) {
        System.out.println(entry.getKey() + " " + entry.getValue());
        if (entry.getValue() == 1){
            return entry.getKey();
        }
    }
    
    return '_';
}