
resource "aws_security_group" "my-table-sg" {
  name_prefix = "${var.project_name}-dynamodb-sg"
  vpc_id = aws_vpc.my_vpc.id

  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = [for ip in var.allowed_ip_addresses: "${ip}/32"]
  }

  egress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    cidr_blocks     = ["0.0.0.0/0"]
  }
}
