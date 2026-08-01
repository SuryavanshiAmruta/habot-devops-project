output "bucket_name" {
  value = google_storage_bucket.raw_landing.name
}

output "dataset_name" {
  value = google_bigquery_dataset.staging.dataset_id
}