import math

istina = input()
pred = input()
istina_l = istina.split(" ")
pred_l = pred.split(" ")
mse_quadro_l = []
mae_difference_l = []
rsme_l = []


def mse(istina_l, pred_l):
    for i in range(len(istina_l)):
        summa = float(pred_l[i]) - float(istina_l[i])
        summa_quadro = summa ** 2
        mse_quadro_l.append(summa_quadro)
    summ_quadro_l = sum(mse_quadro_l)
    res_mse = summ_quadro_l / len(mse_quadro_l)
    res_mse = round(res_mse, 2)
    res_mse_l = str(res_mse).split('.')
    if len(res_mse_l[1]) == 1:
        res_mse = str(res_mse) + "0"
    return str(res_mse)


def mae(istina_l, pred_l):
    for i in range(len(istina_l)):
        difference = abs(float(pred_l[i]) - float(istina_l[i]))
        mae_difference_l.append(difference)
    summ_difference_l = sum(mae_difference_l)
    res_mae = summ_difference_l / len(mae_difference_l)
    res_mae = round(res_mae, 2)
    res_mae_l = str(res_mae).split('.')
    if len(res_mae_l[1]) == 1:
        res_mae = str(res_mae) + "0"
    return str(res_mae)


def rmse(istina_l, pred_l):
    for i in range(len(istina_l)):
        summ_rsme = float(pred_l[i]) - float(istina_l[i])
        summa_quadro_rsme = summ_rsme ** 2
        rsme_l.append(summa_quadro_rsme)
    summ_quadro_rsme_l = sum(rsme_l)
    res_rmse = summ_quadro_rsme_l / len(rsme_l)
    res_rmse = math.sqrt(res_rmse)
    res_rmse = round(res_rmse, 2)
    res_rmse_l = str(res_rmse).split('.')
    if len(res_rmse_l[-1]) == 1:
        res_rmse = str(res_rmse) + "0"
    return str(res_rmse)


print(f"MSE: {mse(istina_l, pred_l)}")
print(f"MAE: {mae(istina_l, pred_l)}")
print(f"RMSE: {rmse(istina_l, pred_l)}")


import numpy as np

def r2_score(y_true, y_pred):
    y_mean = np.mean(y_true)
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - y_mean) ** 2)
    if ss_tot == 0:
        return 0.0
    r2 = 1 - (ss_res / ss_tot)
    return round(r2, 2)



if __name__ == "__main__":
    y_true = list(map(float, input().split()))
    y_pred = list(map(float, input().split()))

    result = r2_score(y_true, y_pred)
    print(f"R2: {result:.2f}")