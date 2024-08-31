terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }

  backend "s3" {
    region         = "us-east-1"
    key            = "app/tocloud/terraform.state"
    bucket         = "lucca-backend"
    dynamodb_table = "lucca-lock-table"
  }
}