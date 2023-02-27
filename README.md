# learning-DynamoDB

🐞🐞🐞 AWS DynamoDBについて学習する。  

## 実行方法

`terraform`ディレクトリに移動して、以下のコマンドを実行する。  

```shell
terraform init
terraform plan
terraform apply
```

これで、DynamoDBのテーブルが作成される。  

---

次に、`app`ディレクトリに移動して、以下のコマンドを実行する。  

```shell
yarn dev
```

これで、作成したDynamoDBのテーブルに対して、サンプル処理が実行される。  
