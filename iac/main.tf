locals {
  env        = terraform.workspace == "default" ? "dev" : terraform.workspace
  aws_region = lookup(var.project_config, local.env)["region"]
  name       = "${var.project_config.name}-${local.env}"
  app_port = lookup(var.project_config, local.env)["app_port"]

  tags = {
    Environment = local.env
    Project     = var.project_config.name
    ManagedBy   = "Terraform"
  }
}

module "tocloud-app" {
  source = "./terraform-base"

  cluster_name = module.ecs-cluster.cluster_name

  app_config = {
    app_name               = local.name
    region                 = local.aws_region
    desired_count          = lookup(var.project_config, local.env)["desired_count"]
    app_port               = local.app_port
    launch_type            = "FARGATE"
    enable_execute_command = lookup(var.project_config, local.env)["enable_execute_command"]
    alb_config = {
      hosts        = lookup(var.project_config, local.env)["host_header"]
      priority     = 100
      listener_arn = lookup(var.project_config, local.env)["listener_arn"]
    }
    health_check = {
      healthy_threshold   = lookup(var.project_config.health_check, local.env)["healthy_threshold"]
      unhealthy_threshold = lookup(var.project_config.health_check, local.env)["unhealthy_threshold"]
      timeout             = lookup(var.project_config.health_check, local.env)["timeout"]
      interval            = lookup(var.project_config.health_check, local.env)["interval"]
      path                = lookup(var.project_config.health_check, local.env)["path"]
      port                = lookup(var.project_config.health_check, local.env)["port"]
    }

    network_configuration = {
      vpc_id           = lookup(var.project_config, local.env)["vpc_id"]
      subnets          = lookup(var.project_config, local.env)["subnets"]
      security_groups  = lookup(var.project_config, local.env)["security_groups"]
      assign_public_ip = local.env == "prod" ? false : true
    }

    container_definitions = {
      # image                  = ""
      cpu                    = lookup(var.project_config, local.env)["cpu"]
      memory                 = lookup(var.project_config, local.env)["memory"]
      essential              = true
      command                = lookup(var.project_config, local.env)["command"]
      entryPoint             = lookup(var.project_config, local.env)["entryPoint"]
      readonlyRootFilesystem = false
      secretsManagerArn      = lookup(var.project_config, local.env)["secretsManagerArn"]
      portMappings = [
        {
          containerPort = local.app_port
          hostPort      = local.app_port
          protocol      = "tcp"
        }
      ]
    }

  }
}   