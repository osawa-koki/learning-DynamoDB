# learning-DynamoDB

🐞🐞🐞 AWS DynamoDBについて学習するためのプログラム。  

## 実行方法

`terraform`ディレクトリに移動して、以下のコマンドを実行します。  

```shell
terraform init
terraform plan
terraform apply
```

これで、DynamoDBのテーブルが作成されます。  

---

次に、`app`ディレクトリに移動して、以下のコマンドを実行します。  

```shell
yarn dev
```

これで、作成したDynamoDBのテーブルに対して、サンプル処理が実行されます。  
