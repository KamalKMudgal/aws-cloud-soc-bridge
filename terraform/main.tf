terraform { required_version = ">= 1.6.0" }
provider "aws" {}
resource "aws_dynamodb_table" "correlation_state" {
  name = "soc-correlation-state"
  billing_mode = "PAY_PER_REQUEST"
  hash_key = "event_id"
  attribute { name = "event_id"; type = "S" }
  server_side_encryption { enabled = true }
}
resource "aws_iam_role" "lambda" {
  name = "soc-bridge-lambda"
  assume_role_policy = jsonencode({Version="2012-10-17",Statement=[{Effect="Allow",Principal={Service="lambda.amazonaws.com"},Action="sts:AssumeRole"}]})
}
