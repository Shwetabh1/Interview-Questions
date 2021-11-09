'''
Find factorial of a non-negative integer.

Example 1:
Input: nums = 5
Output: 5 * 4 * 3 * 2 * 1 = 120

Example 2:
Input: nums = 0
Output: 1

Example 3:
Input: nums = 6
Output: 720
'''

https://my.newtonschool.co/playground/code/6jz65yc7dtoq/
00:00

import java.io.*; // for handling input/output 
import java.util.*; // contains Collections framework 
// don't change the name of this class // you can add inner classes if needed //class Count{ //long count=0; //} class Main { static int result=0; public static void no_of_ways(int n,int start) { if(n==0) result++; for(int i=start;i<=n;i++) no_of_ways(n-i,i+1); } public static void main (String[] args) { int t,n; Scanner s = new Scanner(System.in); t=s.nextInt(); while(t>0) { result=0; n=s.nextInt(); if(n!=0){ no_of_ways(n,1);} System.out.println(result); t--; } } }