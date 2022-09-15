import java.util.*;
class CountVowels{
    public void mapper(String s){
        HashMap <String,Integer> map = new HashMap<>();
        map.put("a",0);
        map.put("e",0);
        map.put("i",0);
        map.put("o",0);
        map.put("u",0);
        String str = s.toLowerCase();
        for(int i=0;i<s.length();i++){
            char ch = str.charAt(i);
            if(ch =='a'){
                map.put("a",map.get("a")+1);
            }
            else if(ch == 'e'){
                map.put("e",map.get("e")+1);
            }
            else if(ch == 'i'){
                map.put("i",map.get("i")+1);
            }
            else if(ch == 'o'){
                map.put("o", map.get("o")+1);
            }
            else if(ch == 'u'){
                map.put("u", map.get("u")+1);
            }

                }
                System.out.println(Arrays.asList(map));
                
    }
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            String s = sc.nextLine();
            CountVowels obj = new CountVowels();
            obj.mapper(s);
        }
    }
}