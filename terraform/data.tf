
resource "aws_dynamodb_table" "my-table" {
  name              = "${var.project_name}-dynamodb"
  billing_mode      = "PAY_PER_REQUEST"

  attribute {
    name = "id"
    type = "S"
  }

  key {
    hash_attribute = "id"
    type           = "HASH"
  }

  tags = {
    Environment = "dev"
  }
}
