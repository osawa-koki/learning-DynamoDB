
variable "project_name" {
  type        = string
  description = "The name of the project"
}

variable "region" {
  type        = string
  description = "The AWS region"
  default = "ap-northeast-1"
}

variable "allowed_ip_addresses" {
  type        = list(string)
  description = "The list of IP addresses"
}
