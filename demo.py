import os
import mlflow
import argparse

def evalute(param1, param2):
    metric  = param1**1 * param1**2
    return metric

def main(p1, p2):
    with mlflow.start_run():
        mlflow.log_param("param1", p1)
        mlflow.log_param("param2", p2)
        metric  = evalute(param1=p1, param2=p2)
        mlflow.log_metric("Somemetric", metric)

if __name__ == '__main__':
    # args = argparse.ArgumentParser()
    # args.add_argument('--param1', '-p1', type = int, default=2)
    # args.add_argument('--param2', '-p2', type = int, default=5)
    # parased_args = args.parse_args()
    main(5, 6)