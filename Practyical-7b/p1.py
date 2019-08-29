def menu():
    print("1.String Length");
    print("2.Join String");
    print("3.Compare String");
    print("4.Reverse String");
    print("5.Check String is Palindrome or not");
    print("6.Check Word in Sentance");
    print("0.Exit");
def str_length(str):
    len=0;
    for i in str:
        len=len+1;
    return len;

def str_join(str1,str2):
    join = str1+ str2;
    return join;

def str_compare(str1,str2):
    if str1==str2:
        return "Same";
    else:
        return "Not Same";
def str_reverse(str1):
    s=str1[::-1];
    return s;
def str_palindrome(str1):
    str2=str1[::-1];
    if str1==str2:
        return "Palindrome";
    else:
        return "Not Palindrome";
def str_check(str1,str2):
    c = str2 in str1;
    if c==1:
        return "Matched";
    else:
        return "Not Matched";
ch=1;
while ch!=0:
    menu();
    ch=int(input("Enter Your Choice : "));
    if ch==1:
        s1=input("Enter a String : ");
        l=str_length(s1);
        print("Length of String is ",l);
    elif ch==2:
        s1=input("Enter a String 1 : ");
        s2=input("Enter a String 2 : ");
        join = str_join(s1,s2);
        print("Joined String is :",join);
    elif ch==3:
        s1=input("Enter a String 1 : ");
        s2=input("Enter a String 2 : ");
        com = str_compare(s1,s2);
        print(com);
    elif ch==4:
        s1=input("Enter a String to Reverse : ");
        r=str_reverse(s1);
        print("Reverse String is :",r);
    elif ch==5:
        s1=input("Enter a String :");
        c=str_palindrome(s1);
        print(c);
    elif ch==6:
        s1=input("Enter a String :");
        c1=input("Enter a Word to search :");
        a=str_check(s1,c1);
        print(a);
