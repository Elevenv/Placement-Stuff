class ReverseSentence{
    public static void main(String args[]){
        String str = "This is java";
        String[] words = str.split(" ");
        int len = words.length;

        for(int i=len-1;i>=0;i--){
            System.out.print(words[i]+" ");
        }

        // String test = "My first arg test";
        // String[] words = test.split(" ");
        // for (String word : words) System.out.println(word);

        //Reverse String 

        // String str = "abcd",temp="";
        // char ch;
        // for(int i=0;i<str.length();i++){
        //     ch = str.charAt(i);
        //     temp = ch+temp;
        // }
        // System.out.println(temp);
    }
}