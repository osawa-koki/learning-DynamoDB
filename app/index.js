import AWS from "aws-sdk";

const region = "ap-northeast-1";
const client = new AWS.DynamoDB({ region });

// テーブル一覧を取得
client.listTables({}, (err, data) => {
  if (err) console.log(err, err.stack);
  else console.log(data);
});

const table_name = "learning-dynamodb-dynamodb";

const uuidv4 = () => {
  return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, (c) => {
    const r = (Math.random() * 16) | 0,
      v = c == "x" ? r : (r & 0x3) | 0x8;
    return v.toString(16);
  });
};
const names = ["test1", "test2", "test3"];
const ages = [20, 30, 40];

// データの挿入
const user_id = uuidv4();
const name = names[Math.floor(Math.random() * names.length)];
const age = ages[Math.floor(Math.random() * ages.length)];
const params_insert = {
  TableName: table_name,
  Item: {
    user_id: { S: user_id },
    name: { S: name },
    age: { N: age.toString() },
  },
};

client.putItem(params_insert, (err, data) => {
  if (err) console.log(err, err.stack);
  else console.log(data);
});

// データを全て取得
const params_scan = {
  TableName: table_name,
};
client.scan(params_scan, (err, data) => {
  if (err) console.log(err, err.stack);
  else {
    console.log("----- ----- ----- full scan ----- ----- -----");
    data.Items.forEach((item) => {
      console.log(item);
    });
  };
});

// `name`が`test1`のデータを取得
const params_condition = {
  TableName: table_name,
  FilterExpression: '#n = :value',
  ExpressionAttributeNames: {
    '#n': 'name',
  },
  ExpressionAttributeValues: {
    ':value': { S: "test1" },
  },
};
console.log('params_condition:', params_condition);
client.scan(params_condition, (err, data) => {
  if (err) {
    console.error('Error scanning table: ', err);
  } else {
    console.log("----- ----- ----- condition scan ----- ----- -----");
    data.Items.forEach((item) => {
      console.log(item);
    });
  }
});
