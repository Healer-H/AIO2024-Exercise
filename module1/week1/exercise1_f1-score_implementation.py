def calculate_f1_score(tp, fp, fn):
    '''
    constrains:
        - giá trị nhận vào tp, fp, fn là type int
        - tp, fp, fn phải đều lớn hơn 0
    '''
    if type(tp) != int:
        print('tp must be int')  
        return None
    if type(fp) != int:
        print('fp must be int')
        return None
    if type(fn) != int:
        print('fn must be int')
        return None
    if tp <= 0:
        print('tp must be greater than 0')
        return None
    if fp <= 0:
        print('fp must be greater than 0')
        return None
    if fn <= 0:     
        print('fn must be greater than 0')
        return None
    
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    
    print(f"precision: {precision}")
    print(f"recall: {recall}")
    print(f"f1_score: {f1_score}")

if __name__ == '__main__':
    calculate_f1_score(tp=2, fp=3, fn=4)
    calculate_f1_score(tp='a', fp=3, fn=4)
    calculate_f1_score(tp=2, fp='a', fn=4)
    calculate_f1_score(tp=2, fp=3, fn='a')
    calculate_f1_score(tp=2, fp=3, fn=0)
    calculate_f1_score(tp=2.1, fp=3, fn=0)
    
    
    