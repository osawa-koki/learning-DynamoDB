
resource "aws_dynamodb_table" "my-table" {
  name              = "${var.project_name}-dynamodb"
  billing_mode   = "PROVISIONED"
  read_capacity  = 1
  write_capacity = 1
  hash_key       = "user_id"
  range_key      = "name"

  attribute {
    name = "user_id"
    type = "S"
  }

  attribute {
    name = "name"
    type = "S"
  }

  attribute {
    name = "age"
    type = "N"
  }

  global_secondary_index {
    name               = "name_index"
    hash_key           = "name"
    range_key          = "age"
    write_capacity     = 1
    read_capacity      = 1
    projection_type    = "INCLUDE"
    non_key_attributes = ["user_id"]
  }

  tags = {
    Environment = "dev"
  }
}
