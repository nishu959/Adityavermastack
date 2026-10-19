class Solution {
    public String minWindow(String s, String t) {

        if(t.length() > s.length()){
            return "";
        }
       
        HashMap<Character, Integer> map = new HashMap<>();
        for(int i = 0; i<t.length(); i++){
            map.put(t.charAt(i), map.getOrDefault(t.charAt(i), 0) + 1);
        }

        int i =0;
        int j = 0;
        int left = 0;
        int right = 0;
        int ans = s.length();
        String res = "";
        int n = s.length();

        int count = map.size();

        while(j < n){

            if(map.containsKey(s.charAt(j))){
                int val = map.get(s.charAt(j)) - 1;
                map.put(s.charAt(j) , val);
                if(val == 0){
                    count -= 1;
                }
            }

            if(count != 0){
                j += 1;
            }

            if(count == 0){    
                while(count == 0){
                    if(map.containsKey(s.charAt(i))){
                        int val = map.get(s.charAt(i)) + 1;
                        map.put(s.charAt(i) , val);
                        if(val==1){
                            count += 1;
                        }
                        
                    } 
                    ans = Math.min(ans , j-i+1);
                    i += 1;
                }

                j += 1;
                

            }
        }
        
        map.clear();
        for(i = 0; i<t.length(); i++){
            map.put(t.charAt(i), map.getOrDefault(t.charAt(i), 0) + 1);
        }

        i = 0;
        j = 0;
        count = map.size();


        while(j < n){

            if(map.containsKey(s.charAt(j))){
                int val = map.get(s.charAt(j)) - 1;
                map.put(s.charAt(j) , val);
                if(val == 0){
                    count -= 1;
                }
            }


            if(j - i + 1 < ans){
                j += 1;
            }

            else if( j - i + 1 == ans){
                if(count == 0){
                    return s.substring(i , j+1);
                }

                if(map.containsKey(s.charAt(i))){
                    int val = map.get(s.charAt(i)) + 1;
                    map.put(s.charAt(i) , val);
                    if(val==1){
                        count += 1;
                    }
                        
                } 
                i += 1;
                j += 1;

            }
        }
        return "";
    }
}
