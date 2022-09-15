// import java.util.*;
// import java.util.ArrayList;
// import java.util.Arrays;

// class CountVowels{
//     public static void main(String args[]){
//         Scanner sc = new Scanner(System.in);
//         System.out.println("Enter String : ");
//         String str = sc.nextLine();
//         // char arr[] = new char[];
//         ArrayList<Character> arr = new ArrayList<Character>();
//         ArrayList<Character> arr1 = new ArrayList<Character>();
//         str = str.toLowerCase();
//         char alp;
//         for(int i=0;i<str.length();i++){
//             alp = str.charAt(i);
//             if(alp != ' ' &&  alp=='a' || alp=='e' || alp=='i' || alp=='o' || alp=='u'){
//                 arr.add(alp);
//             }
//         }
//         arr1 = arr;
//         for(int i=0;i<arr1.size();i++){
//             int vowelCount = 0;
//             for(int j=0;j<arr1.size();j++){
//                 if(i != j){
//                     if(arr1.get(i)==arr1.get(j)){
//                         vowelCount++;
//                     }
//                 }
//             }
//             arr1.remove(i);
//             System.out.println(arr1.get(i)+": "+vowelCount);
//         }
//         sc.close();
//     }
// }


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