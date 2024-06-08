def md_nre_signle_sample(y, y_hat, n, p):
    return (y ** (1 / n) - y_hat ** (1 / n)) ** p

if __name__ == "__main__":
    y = float(input("Input y (float) = "))
    y_hat = float(input("Input y_hat (float) = "))
    n = int(input("Input n (integer) = "))
    p = int(input("Input p (integer) = "))
    print(f"md_nre_signle_sample(y, y_hat, n, p) = {md_nre_signle_sample(y, y_hat, n, p)}")