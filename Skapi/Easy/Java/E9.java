// https://leetcode.com/problems/palindrome-number/
// untuk mengecek apakah sebuah angka adalah palindrome, kita bisa membalik angka tersebut dan membandingkannya dengan angka asli. Jika keduanya sama, maka angka tersebut adalah palindrome. Kita juga perlu menangani kasus khusus seperti angka negatif dan angka yang berakhir dengan 0 (kecuali 0 itu sendiri) yang tidak bisa menjadi palindrome.
public class E9 {
    public static boolean isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }
        int original = x;
        int reversed = 0;
        while (x > 0) {
            int digit = x % 10;
            reversed = (reversed * 10) + digit;
            x /= 10;
        }
        return original == reversed;
    }
    public static void main(String[] args) {
        int angka = 121;
        if (isPalindrome(angka)) {
            System.out.println(angka + " adalah Palindrome");
        } else {
            System.out.println(angka + " bukan Palindrome");
        }
    }
}