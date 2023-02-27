import AWS from "aws-sdk";

const region = "ap-northeast-1";
const client = new AWS.DynamoDB({ region });

// テーブル一覧を取得
client.listTables({}, (err, data) => {
  if (err) console.log(err, err.stack);
  else console.log(data);
});
