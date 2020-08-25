class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def mul(s1, s2, carry):
            ans = int(s1) * int(s2) + carry
            return str(ans % 10), ans // 10

        def add(*args):
            total = 0
            for arg in args[0]:
                total += int(arg)
            return str(total % 10), str(total // 10)

        num1 = num1[::-1]
        num2 = num2[::-1]

        carry = 0
        results = []
        for i in range(len(num1)):
            s1 = num1[i]
            r = "0" * i
            for j in range(len(num2)):
                s2 = num2[j]
                result, carry = mul(s1, s2, carry)
                r += result
            if carry != 0:
                r += str(carry)
            carry = 0
            results.append(r)
        carry = "0"
        final_result = ""
        for i in range(len(results[-1])):
            ns = [r[i] for r in results if i < len(r)] + [carry]
            result, carry = add(ns)
            final_result += result
        if carry != "0":
            final_result += carry
        final_result = final_result[::-1]
        i = 0
        while i < len(final_result) - 1 and final_result[i] == "0":
            final_result = final_result[i + 1:]
        return final_result

    # more simple solution
    def multiply2(self, num1, num2):
        product = [0] * (len(num1) + len(num2))
        pos = len(product)-1

        for n1 in reversed(num1):
            tempPos = pos
            for n2 in reversed(num2):
                product[tempPos] += int(n1) * int(n2)
                product[tempPos-1] += product[tempPos]/10
                product[tempPos] %= 10
                tempPos -= 1
            pos -= 1

        pt = 0
        while pt < len(product)-1 and product[pt] == 0:
            pt += 1

        return ''.join(map(str, product[pt:]))


s = Solution()
print(s.multiply("0", "1231231"))
