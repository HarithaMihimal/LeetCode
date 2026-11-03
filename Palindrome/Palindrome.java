public class Palindrome {
    public boolean isPalindrome(int x) {
        String s = String.valueOf(x);
        String reversed = new StringBuilder(s).reverse().toString();
        if(s.equals(reversed)){
            return true;
        }
        else{
            return false;
        }

    }
    public static void main(String[] args) {
        Palindrome palindrome = new Palindrome();
        System.out.println(palindrome.isPalindrome(123));
        System.out.println(palindrome.isPalindrome(121));
        System.out.println(palindrome.isPalindrome(-123));


    }
}
