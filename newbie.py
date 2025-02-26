import math
def fibonaci(n :int):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        print(i)
        fib.append(fib[i-1] + fib[i-2])
    
    return fib

def twoSum( nums: list[int], target: int) -> list[int]:
    ans = [0,0]
    for i in range(0,len(nums)):
        for j in range(i, len(nums)):
            if(nums[i] + nums[j] == target):
                ans =[i,j]
    return ans

def longestMonotonicSubarray(nums: list[int]) -> int:
        ans = 1
        lengthI = 1
        lengthD = 1
        for i in range(0,len(nums) -1):
            if(nums[i] < nums[i+1]):
                lengthI +=1
                if(ans < lengthI):
                    ans = lengthI
                lengthD = 1

            elif(nums[i] > nums[i+1]):
                lengthD +=1
                if(ans < lengthD):
                    ans = lengthD
                lengthI = 1
            elif(nums[i] ==nums[i+1]):
                lengthD = lengthI = 1
        return ans


def ptbac2(a: int, b:int, c: int):
    d = b**2 - 4*a*c
    if d<0: print("Pt vo nghiem")
    elif d == 0: 
        x1 = -b/(2*a)
        print("Pt nghiem kep ",x1)
    else:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        print("Pt co 2 nghiem rieng biet",x1, x2)

def checkRecord(s: str):
    counta = s.count("A")
    if counta  >= 2: 
        return False
    else:
        for i in range (0, len(s)-2): 
            print(i)
            if s[i] == "L": 
                if s[i+1] == s[i+2] == "L":
                    print("k")
                    return False
        return True

# /////////////////////////////////////////////////////////////

# 1. Tìm bội số chung nhỏ nhất (LCM) và ước số chung lớn nhất (GCD)
#     * Viết hàm tính LCM và GCD của hai số nguyên dương.

def GCD(a:int, b:int):
## Thuật toán Eulic GCD(a, b) = GCD(b, a % b)
##Nếu b == 0 --> GCD(a, b) = a.
    if a == b:
        return a
    elif a < b:
        a,b = b,a

    while b != 0:
        a,b = b,a%b

    return a

def LCM(a:int, b:int):
## LCM=ab/gcd
    result = a*b/GCD(a,b)
    return result


# 2. Số nguyên tố tiếp theo
#     * Nhập một số nguyên dương n, tìm số nguyên tố nhỏ nhất lớn hơn n.

def checksonguyento(n: int):
    if n < 2:
        return False
    if n ==2:
        return True
    if n%2 == 0:
        return False
    if n%2 !=0:
        for i in range (3, int(n**0.5) + 1, 2):
            if n%i == 0:
                return False
        return True


def songuyentotieptheo(n: int):
    if n%2 ==0:
        sotieptheo = n + 1
    else:  sotieptheo = n + 2

    while not checksonguyento(sotieptheo):
        sotieptheo +=2
    return sotieptheo


# 3. Kiểm tra số đối xứng
#     * Viết hàm kiểm tra một số nguyên có phải số đối xứng hay không (ví dụ: 121, 1331).

#   * Sai đề, yêu cầu nhập vô số nguyên
#   * Nếu nhập vào string sai test case "032123"

def checkdoixung(n:int):
    s = str(n);
    for i in range (0, len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True




if __name__ == "__main__":
    a = "321"

    a[0] = "3";
    print(a.split())
    for n in a:
        print(n)


