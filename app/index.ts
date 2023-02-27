import AWS from "aws-sdk";

const region = "ap-northeast-1";
const client = new AWS.DynamoDB({ region });

client.listTables({}, (err, data) => {
  if (err) console.log(err, err.stack);
  else console.log(data);
});
