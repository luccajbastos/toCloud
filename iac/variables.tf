variable "project_config" {

  type = object({

    name = string
    prod = object({
      region = string
      owner  = string
      cluster_name = string
      listener_arn = string
      vpc_id = string
      subnets = list(string)
      security_groups = list(string)
      cpu = number
      memory = number
      command = list(string)
      entryPoint = list(string)
      secretsManagerArn = string
      host_header = list(string)
      app_port = number
      desired_count = number
      enable_execute_command = bool
      health_check = object({
        healthy_threshold = number
        unhealthy_threshold = number
        path = string
        port = number
        protocol = string
        timeout = number
      })
    })

    hml = object({
      region = string
      owner  = string
      cluster_name = string
      listener_arn = string
      vpc_id = string
      subnets = list(string)
      security_groups = list(string)
      cpu = number
      memory = number
      command = list(string)
      entryPoint = list(string)
      secretsManagerArn = string
      host_header = list(string)
      app_port = number
      desired_count = number
      enable_execute_command = bool
      health_check = object({
        healthy_threshold = number
        unhealthy_threshold = number
        path = string
        port = number
        protocol = string
        timeout = number
      })
    })

    dev = object({
      region = string
      owner  = string
      cluster_name = string
      listener_arn = string
      vpc_id = string
      subnets = list(string)
      security_groups = list(string)
      cpu = number
      memory = number
      command = list(string)
      entryPoint = list(string)
      secretsManagerArn = string
      host_header = list(string)
      app_port = number
      desired_count = number
      enable_execute_command = bool
      health_check = object({
        healthy_threshold = number
        unhealthy_threshold = number
        path = string
        port = number
        protocol = string
        timeout = number
      })
    })
  })

  
  default = {
    name = "tocloud"

    prod = {
      region = "us-east-1"
      owner  = "prod"
      cluster_name = "ecs-environment-dev-cluster"
      listener_arn = "arn:aws:elasticloadbalancing:us-east-1:988530097210:listener/app/ecs-environment-dev-alb/1c0ee0774fb02450/12ad4505471c9be2"
      vpc_id = "vpc-040dcaa8f2d8c2be9"
      subnets = ["subnet-0337b1c8a09eae774","subnet-032c5f6a622c7dd06"]
      security_groups = ["sg-0cf2e984881de0020"]
      cpu = 1024
      memory = 2048
      command = []
      entryPoint = ["sh", "-c", "./entrypoint.sh"]
      secretsManagerArn = string
      host_header = ["app.ljb.dev.br"]
      app_port = 8000
      desired_count = 1
      enable_execute_command = true
      health_check = object({
        healthy_threshold = 2
        unhealthy_threshold = 5
        path = "/"
        port = 8000
        protocol = "HTTP"
        timeout = 30
      })
    }

    hml = {
      region = "us-east-1"
      owner  = "prod"
      cluster_name = "ecs-environment-dev-cluster"
      listener_arn = "arn:aws:elasticloadbalancing:us-east-1:988530097210:listener/app/ecs-environment-dev-alb/1c0ee0774fb02450/12ad4505471c9be2"
      vpc_id = "vpc-040dcaa8f2d8c2be9"
      subnets = ["subnet-0337b1c8a09eae774","subnet-032c5f6a622c7dd06"]
      security_groups = ["sg-0cf2e984881de0020"]
      cpu = 1024
      memory = 2048
      command = []
      entryPoint = ["sh", "-c", "./entrypoint.sh"]
      secretsManagerArn = string
      host_header = ["app.ljb.dev.br"]
      app_port = 8000
      desired_count = 1
      enable_execute_command = true
      health_check = object({
        healthy_threshold = 2
        unhealthy_threshold = 5
        path = "/"
        port = 8000
        protocol = "HTTP"
        timeout = 30
      })
    }

    dev = {
      region = "us-east-1"
      owner  = "prod"
      cluster_name = "ecs-environment-dev-cluster"
      listener_arn = "arn:aws:elasticloadbalancing:us-east-1:988530097210:listener/app/ecs-environment-dev-alb/1c0ee0774fb02450/12ad4505471c9be2"
      vpc_id = "vpc-040dcaa8f2d8c2be9"
      subnets = ["subnet-0337b1c8a09eae774","subnet-032c5f6a622c7dd06"]
      security_groups = ["sg-0cf2e984881de0020"]
      cpu = 1024
      memory = 2048
      command = []
      entryPoint = ["sh", "-c", "./entrypoint.sh"]
      secretsManagerArn = string
      host_header = ["app.dev.ljb.dev.br"]
      app_port = 8000
      desired_count = 1
      enable_execute_command = true
      health_check = object({
        healthy_threshold = 2
        unhealthy_threshold = 5
        path = "/"
        port = 8000
        protocol = "HTTP"
        timeout = 30
      })
    }
  }
}