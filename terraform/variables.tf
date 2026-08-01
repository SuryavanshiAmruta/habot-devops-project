variable "project_id" {
  description = "Google Cloud Project ID"
  type        = string
}

variable "region" {
  description = "Deployment Region"
  type        = string
  default     = "asia-south1"
}

variable "bucket_name" {
  description = "Raw Landing Bucket"
  type        = string
}