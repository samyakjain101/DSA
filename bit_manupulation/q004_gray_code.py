"""Problem Statement

https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/bit-manipulation/gray-code/ojquestion?__cf_chl_jschl_tk__=994ef1497eb312f5f68d265f43443a73b6ab5d84-1616611101-0-AYVqoyj3-3b_0gGsa21YPoJqXfviCP1v8lMbW2yJbZhVcrWHa5baA0gX8DrSqVyIrKHneMM8c6FImH-gloRRqDF2UShzXj63od4n5BG13DH8kvL-8IXDMqSoCujdrrkJB791v9z86EDxtb6AJnHa04RJKeM5a4CAJAgGXMIGeZcFJ2bKtVRC1vWY-BR2f9jUUuN-_Dw24hlrUFUqHZ4ZFTLgM-SiYm5w0-TOaaeQDcVPTZbr7yd7nEjOBaImw4Xg_wYeP-_Gp9vw9GnPL0fOlzQFHTUXUmLgVjIocBP_RWzMindb5bcImGKpnWX1_XTmMh7EIdCk_bmLbUBwjxIJHY6de4GqMMacfu_ZCouFGfVp-9OoM-973qOG7mdKiM7iuMpOfdNf2azxMKdvIUlujDkoqlkPicteFroXhSUpZz6h_p1T3HAgK0UDPdY3xBtS-w

"""


def gray_code(n):

    if n == 1:
        return ['0', '1']

    code = gray_code(n-1)
    code_reversed = code[::-1]

    for i in range(len(code)):
        code[i] = '0' + code[i]
        code_reversed[i] = '1' + code_reversed[i]

    return code + code_reversed


if __name__ == "__main__":
    n = 3
    result = gray_code(n)
    for i in range(len(result)):
        result[i] = int(result[i], 2)
    print(result)
